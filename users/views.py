from email import message
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from accounts.serializers import assistanceSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.filter(is_active = True)
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class assistanceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = assistanceSerializer
    queryset = assistanceSerializer.Meta.model.objects.all()
    
