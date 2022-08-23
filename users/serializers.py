from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name','dni','password')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('dni' ,'name', 'email','last_name','image','is_active')

class UserAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('dni' ,'name','last_name')

class UserContact(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'last_name')