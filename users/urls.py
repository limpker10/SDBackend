import imp
from django.urls import path
from .views import UserListCreateAPIView,assistanceListCreateAPIView
urlpatterns = [
    path('listUser',UserListCreateAPIView.as_view(),name='listUser'),
    path('assistanceUser',assistanceListCreateAPIView.as_view(),name='assistanceUser'),
]
