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
    handler_username = serializers.SerializerMethodField()

    class Meta:
        model = HelpDeskRequest
        fields = '__all__'
    
    def get_handler_username(self, obj):
        return obj.handler.username if obj.handler else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['handler_username'] = self.get_handler_username(instance)
        return representation




class AuditoriumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditorium
        fields = '__all__'