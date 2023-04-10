from django.shortcuts import render, redirect, HttpResponse
from app.models import *
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


def HOME(request):
    
  
    
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')

@csrf_protect
def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)

        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('local_dashboard')
            elif user_type == '3':
                return redirect('patrol_home')

            else:
                messages.error(request, "Email and Password are Invalid")
                return redirect('login')
        else:
            messages.error(request, "Email and Password are Invalid")
            return redirect('login')

    return None


def doLogout(request):
    logout(request)
    return redirect('login')
    
    

def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user
    }

    return render(request, 'profile.html', context)


def PROFILE_UPDATE(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name

            if profile_pic != None and profile_pic != '':
                customuser.profile_pic = profile_pic

            if password != None and password != '':
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "your profile updated successfully")
            return redirect('profile')

        except:
            messages.error(request, "Your profile not updated")

    return render(request, 'profile.html')


def LOAD_DISTRICT(request):
    province_id = request.GET.get('provinceid')

    district = District.objects.filter(province_id=province_id).all()

    context = {
        "district": district,
    }
    return render(request, 'Hod/district_drop_down.html', context)


def LOAD_LOCAL_LEVEL(request):
    district_id = request.GET.get('district_id')

    local_level = Local_Level.objects.filter(district_id=district_id).all()

    context = {
        "local_level": local_level
    }
    return render(request, 'Hod/local_level_drop_down.html', context)
