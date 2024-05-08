from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Lecturer, HelpDeskRequest, HelpDeskUser, Auditorium

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    

class HelpDeskUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = HelpDeskUser
        fields = ('user', 'username')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        heldeskuser = HelpDeskUser.objects.create(user=user, **validated_data)
        return heldeskuser



class LecturerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Lecturer
        fields = ('user', 'full_name')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        lecturer = Lecturer.objects.create(user=user, **validated_data)
        return lecturer


class HelpDeskRequestSerializer(serializers.ModelSerializer):
    auditorium_number_display = serializers.CharField(source='auditorium_number.number', read_only=True)

    class Meta:
        model = HelpDeskRequest
        fields = '__all__'  # Убедитесь, что auditorium_number также включен, если нужно сохранять это поле

    def get_handler_username(self, instance):
        # Возвращаем username handler'а, если он существует
        return instance.handler.username if instance.handler else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['handler'] = self.get_handler_username(instance)
        return representation



class AuditoriumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditorium
        fields = '__all__'