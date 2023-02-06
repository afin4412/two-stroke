
from django.db import models
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.core.mail import send_mail
from .models import *
from rxpro.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from django.conf import settings
from django.contrib.auth import authenticate

# Create your views here.

def register(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['username']
            fn=a.cleaned_data['fullname']
            em=a.cleaned_data['email']
            pn= a.cleaned_data['phone']
            gd = a.cleaned_data['gender']
            ps=a.cleaned_data['password']
            cp=a.cleaned_data['cpassword']
            if ps==cp:
                b=regmodel(username=un,fullname=fn,email=em,phone=pn,gender=gd,password=ps)
                b.save()
                return HttpResponse("reg success")
            else:
                return HttpResponse("password  doesnt match")

    else:
        return render(request,"registration.html")


def index(request):
    return render(request,'index.html')



def login123(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['username']
            ps=a.cleaned_data['password']
            b=regmodel.objects.all()
            for i in b:
                if un==i.username and ps==i.password:
                    return HttpResponse("login success")
            else:
                return HttpResponse("login failed")
    else:
        return render(request,"login.html")







def regis(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(username=username).first():
            messages.success(request,'username already taken')
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already exist')
            return redirect(regis)
        user_obj=User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        auth_token=str(uuid.uuid4())
        profile_obj=profile.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)
        return render(request,'success.html')
    return render(request,'user_reg.html')




def send_mail_regis(email,token):
    subject="your account has been verified"
    message=f'paste the link to verify your account  http://127.0.0.1:8000/rx/verify/{token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)



def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account is already verified')
            return redirect(login)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(login)
    else:
        return redirect(error)


def login(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user_obj= User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'user not found')
            return redirect(login) #login
        profile_obj = profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check your mail')
            return redirect(login)
        user = authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(login)
        return HttpResponse('success')
    return render(request,'user_login.html')


def nav(request):
    return render(request,'profile.html')


# def file(request):
#     if request.method=='POST':
#         a=fileform(request.POST,request.FILES)
#         if a.is_valid():
#             nm=a.cleaned_data['iname']
#             des = a.cleaned_data['des']
#             pr=a.cleaned_data['iprice']
#             im=a.cleaned_data['image']
#             b=filemodel(iname=nm,iprice=pr,des=des,image=im)
#             b.save()
#             return redirect(filedisplay)
#         else:
#             return HttpResponse("file uplaod failed")
#     else:
#         return render(request,"show.html")
#
#
#
# def nfile(request):
#     if request.method=='POST':
#         a=nonform(request.POST,request.FILES)
#         if a.is_valid():
#             nm=a.cleaned_data['nitem']
#             np=a.cleaned_data['nprice']
#             de=a.cleaned_data['ndes']
#             im=a.cleaned_data['nimage']
#             b=nonmodel(nitem=nm,nprice=np,ndes=de,nimage=im)
#             b.save()
#             return redirect(nondisplay)
#         else:
#             return HttpResponse("file upload failed")
#     else:
#         return render(request,"nondisplay.html")
#
#
# def vfile(request):
#     if request.method=='POST':
#         a=vegform(request.POST,request.FILES)
#         if a.is_valid():
#             nm=a.cleaned_data['vitem']
#             np=a.cleaned_data['vprice']
#             de=a.cleaned_data['vdes']
#             im=a.cleaned_data['vimage']
#             b=vegmodel(vitem=nm,vprice=np,vdes=de,vimage=im)
#             b.save()
#             return redirect(vegdisplay)
#         else:
#             return HttpResponse("file upload failed")
#     else:
#         return render(request,"display.html")

# Create your views here.
