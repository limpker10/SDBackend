
from rest_framework import serializers
from .models import assistance,Rol
from  users.serializers import UserAssistanceSerializer

class rolSerializer(serializers.ModelSerializer):
    class Meta:
      model = Rol
      fields = '__all__'

class assistanceSerializer(serializers.ModelSerializer):
    assistance_dni = UserAssistanceSerializer(required=True)
    assistance_rol = serializers.RelatedField(source='rol_name', read_only=True)
    class Meta:
        model = assistance
        fields = "__all__"