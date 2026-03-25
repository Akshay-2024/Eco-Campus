from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Student

def home(request):
    return render(request, 'main.html')

def sign(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        pnr = request.POST.get("pnr", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        department = request.POST.get("department", "").strip()
        semester = request.POST.get("semester", "").strip()

        # Check all fields filled
        if not all([name, phone, pnr, email, password, department, semester]):
            messages.error(request, "All fields are required!")
            return render(request, "signup.html")

        # Check duplicates
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, "signup.html")

        if Student.objects.filter(pnr=pnr).exists():
            messages.error(request, "PNR already registered!")
            return render(request, "signup.html")

        # Create User with hashed password
        user = User.objects.create(
            username=email,  # Using email as username
            email=email,
            password=make_password(password),
            first_name=name,
        )

        # Create Student profile linked to User
        Student.objects.create(
            user=user,
            phone=phone,
            pnr=pnr,
            department=department,
            semester=semester,
        )

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')  # Or render login page

    return render(request, "signup.html")

def log(request):
    if request.method == "POST":
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        # Find user by email
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")
            return render(request, 'login.html')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:  # or use request.user.is_superuser for superuser only
        # Show admin page or admin dashboard
                return render(request, 'admin.html')
            else:
        # Show regular user page
            
                return redirect('home')
        else:
            messages.error(request, "Invalid password.")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
def profile(request):
    return render(request,'profile.html')
def leader(request):
    return render(request,'leader.html')
def admin(request):
    return render(request,'admin.html')
def event(request):
    return render(request,'events.html')