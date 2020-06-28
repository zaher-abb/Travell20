from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



def register(request):

    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        re_password= request.POST['re_password']
        if(password==re_password):
            if(User.objects.filter(username=username).exists()):
               messages.info(request,'Username is Taken')
               return redirect('account:register')
            elif(User.objects.filter(email=email).exists()):
               messages.info(request,"Email is already Taken")
               return redirect('account:register')
            else:
              user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
              user.save();
        else:
            messages.info(request, 'password not matched')
            return redirect('account:register')
        return redirect('account:login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('Booking:index')
        else :
            messages.info(request,"invaliad login")
            return redirect('account:login')
    return render(request,'login.html')




def logout(request):

    auth.logout(request)
    return render(request,'index.html')

