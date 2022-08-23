# Generated by Django 4.1 on 2022-08-23 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='assistance_dni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='assistance_rol',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.rol'),
        ),
    ]
