from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUp, SignIn
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import ProfileUser, Message

# lesson 38
def hello(request):
    return HttpResponse("Hello from notes app!")

# lesson 40
def profile_user(request):
    profile = ProfileUser.objects.all()
    return render(request, 'profile_user.html', {'profile': profile})

def message(request):
    msg = Message.objects.all()
    return render(request, 'msg.html', {'msg': msg})

# lesson 41, 44
def sign_up(request):
    user_form = SignUp()
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            messages.success(request, 'You created account successfully!')
            return redirect('chat.html')
        else:
            messages.error(request, 'Invalid username or password. Please try again')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'register.html', context)

def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Hi! {username}!. Welcome to the chat page!")
                return render('chat.html')
            else:
                messages.info(request, 'Account does not exist. Sign in')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'signIn.html', context)

