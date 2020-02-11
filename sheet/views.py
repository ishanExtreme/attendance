from django.shortcuts import render,redirect

from .models import Sheet
def attendance(request):
    usernames=[]
    sheets = Sheet.objects.all()
    for sheet in sheets:
        if sheet.present == "False":
            usernames.append(str(sheet.student))

    
    return render(request,'sheet/attendance.html',{'usernames':usernames})
def create(request):
    sheet = Sheet()
    sheet.student = (request.user).username 
    sheet.present = False
    sheet.save()
    return redirect('home')


