from django import forms

class regform(forms.Form):
    fullname= forms.CharField(max_length=20)
    username=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone = forms.IntegerField()
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)
    gender=forms.CharField(max_length=20)




class logform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)

class fileform(forms.Form):
    iname=forms.CharField(max_length=20)
    des = forms.CharField(max_length=50)
    iprice=forms.IntegerField()
    image=forms.FileField()


class nonform(forms.Form):
    nitem=forms.CharField(max_length=25)
    nprice=forms.IntegerField()
    ndes=forms.CharField(max_length=100)
    nimage=forms.FileField()


class vegform(forms.Form):
    vitem = forms.CharField(max_length=25)
    vprice = forms.IntegerField()
    vdes = forms.CharField(max_length=100)
    vimage = forms.FileField()