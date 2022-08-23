
from django.views.generic import View
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse
from .utils import render_to_pdf
from .models import User
from accounts.models import assistencia
from .serializers import UserSerializer,UserProfileSerializer,UserContact
from accounts.serializers import assistanceSerializer,asistenciaList

class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserProfileSerializer.Meta.model.objects.filter(is_active = True)

    def post(self,request):
        
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class assistanceListCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = assistanceSerializer
    queryset = assistanceSerializer.Meta.model.objects.all()


class assistanciaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = asistenciaList
    def get_queryset(self):
        name = self.request.query_params.get('name')
        queryset = asistenciaList.Meta.model.objects.filter(name = name)
        return queryset
    

def listAsistancePDF(request):

    if request.method == 'GET':
        name = request.GET.get('name')
        empleados = assistencia.objects.filter(name = name)
        data = {
            'count': empleados.count(),
            'empleados': empleados
        }
        pdf = render_to_pdf('home/lista.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class UserContact(generics.ListCreateAPIView):
    serializer_class = UserContact
    queryset = UserContact.Meta.model.objects.filter(is_active = True)


    
