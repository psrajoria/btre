from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User # from postgres


# Create your views here.



def register(request):
    if request.method =='POST':
        # print('SUBMITTED REG')
        # return redirect('register')
        #register USer
        # messages.error(request,'Testing Error Message')
        # return redirect('register')

        #Get from value
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check password
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('register')

                else:
                    #Looks Good
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    #messages.success(request,'Account Created')
                    ## Login after register
                    # auth.login(request,user)
                    # messages.success(request,'You are now logged in')
                    # return redirect('index')

                    user.save()
                    messages.success(request,'You are now regsitered and can login')
                    return redirect ('login')
            return redirect('register')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method =='POST':
        # print('SUBMITTED REG')
        # return redirect('login')
        #login USer
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')    
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')

        
    else:
        return render(request,'accounts/login.html')


def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request,'You are now logout')
        return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')