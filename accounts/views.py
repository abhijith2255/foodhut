
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


# Create your views here.


def register(request):
    if request.method=="POST":
        fristname = request.POST['fristname']
        username = request.POST['username']
        email = request.POST['email']
        pasw1 = request.POST['password1']
        pasw2 = request.POST['password2']
        if pasw1==pasw2:    
            if User.objects.filter(username=username) .exists():
                messages.info(request,"username alredy taken")
                return redirect('register')
            elif User.objects.filter(email=email) .exists():
                messages.info(request, "email alredy taken")
                return redirect('register')
            else:                   
                user=User.objects.create_user(username=username,password=pasw1,email=email,last_name=fristname)
                user.save()
                print('user created')
        else:
            print('password not matched')
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('login')
    else:      
        print('user not created')
        return render(request,'registration.html')
    
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('user login')
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    