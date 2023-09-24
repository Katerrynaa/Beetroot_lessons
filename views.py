from django.shortcuts import render, redirect
from django.http import HttpResponse
            
def profile_user(request):
    profile = ProfileUser.objects.all()
    return render(request, 'profile_user.html', {'profile': profile})

def message(request):
    msg = Message.objects.all()
    return render(request, 'msg.html', {'msg': msg})
