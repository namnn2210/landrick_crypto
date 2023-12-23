from django.shortcuts import render


# Create your views here.
def login(request):
    if request.method == 'POST':
        pass
    return render(request, template_name='auth-bs-login.html')


def signup(request):
    return render(request, template_name='auth-bs-signup.html')


def reset(request):
    return render(request, template_name='auth-bs-reset.html')
