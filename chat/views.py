from chat.serializers import MessageSerializer
from rest_framework import generics
from .models import Message


class MessagesListView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(room_name=self.kwargs["room_name"])