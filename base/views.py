from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.reverse import reverse

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = LecturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            # Включаем ID пользователя в ответ
            return Response({
                "token": token.key,
                "userId": user.id  # Добавляем ID пользователя
            }, status=status.HTTP_200_OK)
        return Response({"error": "Неверные учетные данные"}, status=status.HTTP_400_BAD_REQUEST)
    

class HelpDeskRequestViewSet(viewsets.ModelViewSet):
    queryset = HelpDeskRequest.objects.all()
    serializer_class = HelpDeskRequestSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('register-user', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'helpdesk-requests': reverse('helpdeskrequest-list', request=request, format=format),
    })
