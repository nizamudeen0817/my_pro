from django.shortcuts import render,redirect
from django.contrib.auth.models  import User,auth
from django.contrib import messages

# Create your views here.
def creatac(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('c-password')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username alreadt exists")
                return redirect("http://127.0.0.1:8000/userapp")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect("http://127.0.0.1:8000/userapp")
            else:
                user_reg=User.objects.create_user(username=username,password=password,email=email)
                user_reg.save()
                messages.info(request,"user is created")
                return redirect("http://127.0.0.1:8000")
    else:               
        return render(request,'creatac.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"username or password doesnt match")
            return redirect('http://127.0.0.1:8000')
            
        
    
    
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000')
