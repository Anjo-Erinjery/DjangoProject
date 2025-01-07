from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

# Use the custom user model
User = get_user_model()

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'register.html')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'register.html')

        # Create and save the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('guide')  # Replace 'login' with the name of your login URL

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def guide(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('profile')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')
from django.shortcuts import render
from django.contrib import messages

def profile(request):
    pincode_valid = False  # Default state; procedure hidden until pincode is verified

    if request.method == 'POST':
        pincode = request.POST.get('pincode')

        # Example validation logic: Check if pincode is a 6-digit number
        if len(pincode) == 6 and pincode=='680026':
        
            
            pincode_valid = True
        
        else:
            messages.error(request, "Invalid pincode! Please enter a Valid pincode.")

    context = {
        'pincode_valid': pincode_valid,
    }
    return render(request, 'profile.html', context)


"""def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('guide')
    user = get_object_or_404(User, id=user_id)
    return render(request, 'profile.html', {'user': user})"""
def logout(request):
    return render(request,'login.html')
def edit_profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.full_name = request.POST.get('full_name')
        user.email = request.POST.get('email')
        
        user.year_of_study = request.POST.get('year_of_study')
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')

    return render(request, 'edit_profile.html', {'user': user})
from django.shortcuts import render



def about(request):
    """
    Renders the about page.
    """
    return render(request, 'about.html')

def contact(request):
    """
    Renders the contact page.
    """
    return render(request, 'contact.html')

def terms(request):
    """
    Renders the terms and conditions page.
    """
    return render(request, 'terms.html')
