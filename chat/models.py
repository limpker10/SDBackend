from django.db import models

class Message(models.Model):
    room_name = models.TextField(max_length=50)
    text = models.TextField(max_length=300)
    Usersend = models.TextField(max_length=20, null = True)

    def __str__(self):
        return self.room_name