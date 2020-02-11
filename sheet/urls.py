from django.urls import path
from sheet import views
urlpatterns = [
    
    path('attendance/',views.attendance,name = 'attendance'),
    path('create/',views.create,name = 'create'),
    
    
]