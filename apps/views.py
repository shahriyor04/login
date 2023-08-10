from django.shortcuts import render,HttpResponse,redirect
from  django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login,logout
# Create your views here.

def CustomerPage(request):
    return render(request, 'New_customer_list.html')


def RegisterPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        ful = request.POST.get('Furs_name')
        pass1 = request.POST.get('paasword')
        my_user = User.objects.create_user(uname,ful, pass1)
        my_user.save()
        return redirect('login')

    return render(request, 'register.html' )

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password = password)
        if user is not None:
            login(request,user)
            return redirect('navbar')
        else:
            return HttpResponse("username yoki password ni noto'gri kiriddingiz ")
    return render(request, 'login.html')


def ProfilePage(request):
    return render(request , 'Profile.html')

def NavbarPage(request):
    return render(request, 'navbar.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def Profile(request):
    logout(request)
    return redirect('profile')