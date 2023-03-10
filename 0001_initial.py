# Generated by Django 4.1.3 on 2022-11-27 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='filemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=20)),
                ('des', models.CharField(max_length=50)),
                ('iprice', models.IntegerField()),
                ('image', models.FileField(upload_to='crudapp/static')),
            ],
        ),
        migrations.CreateModel(
            name='nonmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nitem', models.CharField(max_length=25)),
                ('nprice', models.IntegerField()),
                ('ndes', models.CharField(max_length=100)),
                ('nimage', models.FileField(upload_to='foodhut_app/static/non_veg')),
            ],
        ),
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='vegmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vitem', models.CharField(max_length=25)),
                ('vprice', models.IntegerField()),
                ('vdes', models.CharField(max_length=100)),
                ('vimage', models.FileField(upload_to='foodhut_app/static/veg')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
