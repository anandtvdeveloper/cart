from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.contrib import messages
def register(request):
    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        cpassword  = request.POST['cpassword']
        email = request.POST['email']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('User Created')
        else:
            print('Password not Matched')
            return redirect('register')
        return redirect('cartdataapp:allproduct')
    else:
        return render(request,'registration.html')

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not  None:
            auth.login(request,user)
            return redirect('cartdataapp:allproduct')
        else:
            messages.info(request,"invalid details")
            return redirect("login")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('cartdataapp:allproduct')