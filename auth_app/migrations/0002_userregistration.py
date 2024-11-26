# Generated by Django 5.1.3 on 2024-11-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
                ('confirm_password', models.CharField(max_length=128)),
                ('emergency_contact1', models.CharField(blank=True, max_length=15, null=True)),
                ('emergency_contact2', models.CharField(blank=True, max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
