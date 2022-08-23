from django.db import models
from django.utils import timezone
from users.models import User

class Rol(models.Model):
    rol_name = models.CharField('Rol', max_length = 25, blank = True, null = True)
    TiempoEntrada = models.DateTimeField()
    TiempoSalida = models.DateTimeField()

    def __str__(self):
        return f'{self.rol_name}'

class assistance(models.Model):
    assistance_dni = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    assistance_rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    assistance = models.DateTimeField()
    status = models.CharField(max_length = 10)

    def __str__(self):
        return self.assistance_dni.dni
    

class assistencia(models.Model):
    assistance_dni = models.CharField(max_length = 8)
    name = models.CharField( max_length = 25, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 25, blank = True, null = True)
    rol_name = models.CharField('Rol', max_length = 25, blank = True, null = True)
    date = models.DateTimeField(default=timezone.now)
    assistance = models.DateTimeField()
    status = models.CharField(max_length = 10)

    def __str__(self):
        return self.assistance_dni