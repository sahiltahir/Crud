from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import StudentData

# Create your views here.
def home(request):
    if request.user.is_authenticated:
            std=StudentData.objects.all()
            return render(request,'home.html',{'std':std})
    else:
        return redirect('/home/signin')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/home')
        else:
            return render(request,'sign_up.html',{'form':form})
    else:
        form=UserCreationForm()
        return render(request,'sign_up.html',{'form':form})
def signin(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            form=AuthenticationForm()
            return render(request,'sign_in.html',{'form':form})
    else:
        form=AuthenticationForm()
        return render(request,'sign_in.html',{'form':form})

def signout(request):
    logout(request)
    return redirect('/home/signin')