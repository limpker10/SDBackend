import imp
from django.urls import path
from .views import UserListCreateAPIView,assistanceListCreateAPIView,assistanciaListCreateAPIView,listAsistancePDF,UserContact
urlpatterns = [
    path('listUser',UserListCreateAPIView.as_view(),name='listUser'),
    path('listContactUser',UserContact.as_view(),name='listContactUser'),
    path('assistanceUser/',assistanceListCreateAPIView.as_view(),name='assistanceUser'),
    path('assistanciaUser/',assistanciaListCreateAPIView.as_view(),name='assistanciaUser'),
    path('listAsistancePDF/',listAsistancePDF,name='listAsistancePDF'),
]
