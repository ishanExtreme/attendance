from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password1'] and request.POST['password2']:   
            if request.POST['password1'] == request.POST['password2']:
                try:
                    User.objects.get(username=request.POST['username'])
                    return render(request,'accounts/signup.html',{'error':'Username Already Taken!!'})
                except User.DoesNotExist:
                    user =  User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                    auth.login(request,user)
                    return redirect('create')
            else:
                return render(request,'accounts/signup.html',{'error':'Passwords Doesnot Match!!'})
        else:
            return render(request,'accounts/signup.html',{'error':'One or More Field(s) are missing'})
    else:
        return render(request,'accounts/signup.html')
def signout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
   
def signin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/signin.html',{'error':'Username or Password is Incorrect'})
    else:
        return render(request,'accounts/signin.html')
