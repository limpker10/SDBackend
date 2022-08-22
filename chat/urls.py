from chat.views import MessagesListView
from django.urls.conf import path
from django.views.generic import TemplateView

urlpatterns = [
   
    path("api/messages/<room_name>/", MessagesListView.as_view()),
]