from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

# Create your models here.
class regmodel(models.Model):
    fullname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    gender=models.CharField(max_length=20)


class filemodel(models.Model):
    iname=models.CharField(max_length=20)
    des = models.CharField(max_length=50)
    iprice=models.IntegerField()
    image=models.FileField(upload_to="crudapp/static")


class nonmodel(models.Model):
    nitem=models.CharField(max_length=25)
    nprice=models.IntegerField()
    ndes=models.CharField(max_length=100)
    nimage=models.FileField(upload_to='foodhut_app/static/non_veg')


class vegmodel(models.Model):
    vitem=models.CharField(max_length=25)
    vprice=models.IntegerField()
    vdes=models.CharField(max_length=100)
    vimage=models.FileField(upload_to='foodhut_app/static/veg')

# Create your models here.
