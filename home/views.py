from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from requests import get

import ipinfo

from sheet.models import Sheet
def home(request):
    return render(request,'home/home.html')
@login_required(login_url="/account/signin")
def reset(request):
    if request.user.username == 'ishan':
        sheets = Sheet.objects.all()
        for sheet in sheets:
            sheet.present = False
            sheet.save()
        return redirect('home')
    else:
        return redirect('home')
@login_required(login_url="/account/signup")
def mark(request):
    ip = get('https://api.ipify.org').text
    access_token = 'f6ea795ded4276'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip)
    latitude = [20,21,22,23,24,25]
    longitude = [86,87,88,89,90,91,92,93]
    if int((details.latitude)[0:(details.latitude).index('.')]) in latitude and int((details.longitude)[0:(details.longitude).index('.')]) in longitude:
        sheets = Sheet.objects.all()
        for sheet in sheets:
            if sheet.student == request.user.username:
                sheet.present = True
                sheet.save()
        return redirect('home')
    else:
        return render(request,'home/home.html',{'error':'You are not in correct location to mark your attendance'})

    
        
