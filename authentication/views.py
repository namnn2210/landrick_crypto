from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log in the user
            login(request, user)

            # Redirect to a success page or another page after login.
            return redirect('index')  # Replace with the actual URL name or path

        else:
            # Authentication failed, display an error message.
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, template_name='auth-bs-login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']

        # You may want to add validation and error handling here.

        # Create a new User instance and save it to the database.
        User.objects.create_user(username=email, email=email, password=password, first_name=first_name)

        return redirect('index')  # Replace with the actual URL name or path
    return render(request, template_name='auth-bs-signup.html')


def reset(request):
    return render(request, template_name='auth-bs-reset.html')
