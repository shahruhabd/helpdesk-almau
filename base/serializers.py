from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Lecturer, HelpDeskRequest

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
    creator_full_name = serializers.CharField(source='creator.full_name', read_only=True)
    
    class Meta:
        model = HelpDeskRequest
        fields = '__all__'  

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['creator'] = instance.creator.full_name
        return representation