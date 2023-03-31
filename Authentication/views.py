from django.shortcuts import render, redirect
from Authentication.models import User_Info, Contact_Us, About_Us, Services, Restaurant_Info, Gallary, Features, Form_Info, Job_Info
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def HomePage(request):
    # About Us
    food_info = About_Us.objects.all()

    # Services
    service_info = Services.objects.all()

    # Restaurant Information
    restaurant_details = Restaurant_Info.objects.all()

    # Gallary
    gallary_images = Gallary.objects.all()

    # Features
    feature_details = Features.objects.all()

    # Passing database details to index page
    return render(request, 'index.html', {'service_info':service_info, 'food_info':food_info, 
    'restaurant_details':restaurant_details, 'gallary_images':gallary_images, 'feature_details':feature_details})

    return render(request, 'index.html')

def SignupPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                # print('Username Taken')
                messages.info(request, 'Username Already Taken', extra_tags='user_name')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                # print('Email Taken')
                messages.info(request, 'Email Already Taken', extra_tags='user_email')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            # print('Password not match')
            messages.info(request, 'Password Not Matched', extra_tags='user_password')
            return redirect('signup')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            if username == "" or password == "":
                messages.info(request, 'Please Enter Username and Password', extra_tags='empty_field')
                return redirect('login')

            user_name = User.objects.filter(username=username).only('username')
            user_password = User.objects.filter(username=username).only('password')

            if username != user_name or password != user_password:
                messages.info(request, 'Invalid Username or Password', extra_tags='user_field')
                return redirect('login') 

    return render(request, 'login.html')

def UserProfilePage(request):
    current_user = request.user
    user_data = {
        'user_name':current_user.username,
        'user_email':current_user.email,
        'user_password':current_user.password,
    }
    return render(request, 'user-profile.html', {'user_data':user_data})

def ChefApplicationPage(request):
    if request.method == 'POST':
        job_type = request.POST.get('job_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        city = request.POST.get('city')
        state = request.POST.get('state')
        aadhar_card = request.POST.get('aadhar_card')
        pan_card = request.POST.get('pan_card')
        availability = request.POST.get('availability')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')
        add_info = request.POST.get('add_info')
        user_resume = request.FILES['resume']

        chef_info = Job_Info(job_type=job_type, first_name=first_name, last_name=last_name, contact_no=contact_no, email_id=email, dob=dob,
        address=address, zip_code=zip_code, city=city, state=state, aadhar_card=aadhar_card, pan_card=pan_card, 
        availability=availability, salary=salary, experience=experience, add_info=add_info, user_resume=user_resume)

        chef_info.save()

        return redirect('index')

    form_fields = Form_Info.objects.filter(form_title="Application Form for Chef")
    return render(request, 'chef-application.html', {'form_fields':form_fields})

def ManagerApplicationPage(request):
    if request.method == 'POST':
        job_type = request.POST.get('job_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        city = request.POST.get('city')
        state = request.POST.get('state')
        aadhar_card = request.POST.get('aadhar_card')
        pan_card = request.POST.get('pan_card')
        availability = request.POST.get('availability')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')
        add_info = request.POST.get('add_info')
        user_resume = request.FILES['resume']

        chef_info = Job_Info(job_type=job_type, first_name=first_name, last_name=last_name, contact_no=contact_no, email_id=email, dob=dob,
        address=address, zip_code=zip_code, city=city, state=state, aadhar_card=aadhar_card, pan_card=pan_card, 
        availability=availability, salary=salary, experience=experience, add_info=add_info, user_resume=user_resume)

        chef_info.save()

        return redirect('index')

    form_fields = Form_Info.objects.filter(form_title="Application Form for Manager")
    return render(request, 'manager-application.html', {'form_fields':form_fields})

def WaiterApplicationPage(request):
    if request.method == 'POST':
        job_type = request.POST.get('job_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        city = request.POST.get('city')
        state = request.POST.get('state')
        aadhar_card = request.POST.get('aadhar_card')
        pan_card = request.POST.get('pan_card')
        availability = request.POST.get('availability')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')
        add_info = request.POST.get('add_info')
        user_resume = request.FILES['resume']

        chef_info = Job_Info(job_type=job_type, first_name=first_name, last_name=last_name, contact_no=contact_no, email_id=email, dob=dob,
        address=address, zip_code=zip_code, city=city, state=state, aadhar_card=aadhar_card, pan_card=pan_card, 
        availability=availability, salary=salary, experience=experience, add_info=add_info, user_resume=user_resume)

        chef_info.save()

        return redirect('index')

    form_fields = Form_Info.objects.filter(form_title="Application Form for Waiter")
    return render(request, 'waiter-application.html', {'form_fields':form_fields})

def ContactUsPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('message')

        contact_us = Contact_Us()
        contact_us.name = name
        contact_us.email = email
        contact_us.description = description
        contact_us.save()

    return redirect('index')

def LogoutPage(request):
    logout(request)
    return render(request, 'index.html')