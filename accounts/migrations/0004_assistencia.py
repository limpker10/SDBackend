# Generated by Django 4.1 on 2022-08-23 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_assistance_assistance_rol'),
    ]

    operations = [
        migrations.CreateModel(
            name='assistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistance_dni', models.CharField(max_length=8)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='Apellidos')),
                ('rol_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='Rol')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('assistance', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
