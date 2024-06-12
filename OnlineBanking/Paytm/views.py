from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect("login")

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect("register")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,email=email, password=password)
                messages.info(request,'accepted')
                user.save()
                return redirect("login")
            print('successfully_created')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        DOB = request.POST['DOB']
        Age = request.POST['Age']
        Gender = request.POST['Gender']
        PhoneNumber = request.POST['PhoneNumber']
        Email = request.POST['Email']
        Adress = request.POST['Adress']
        District = request.POST['District']
        Account_Type = request.POST['Account Type']
        Payment_Methode = request.POST['Payment Methode']

        user = User.objects.create_user(first_name=first_name, DOB=DOB, Age=Age,Gender=Gender,PhoneNumber=PhoneNumber,Email=Email,Adress=Adress,District=District,
                                        Account_Type=Account_Type,Payment_Methode=Payment_Methode)
        user.save()
        messages.info(request, "Application Successfully Accepted")
        # print('Application Successfully Accepted')
        return redirect('/')
    return render(request, 'form.html')
