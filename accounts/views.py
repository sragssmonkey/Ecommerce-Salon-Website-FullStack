from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login,logout
from core.views import home
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method=='POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

