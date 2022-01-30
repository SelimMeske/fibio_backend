from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def worker_login(request):
    pass

def client_login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/customer-profile')
            else:
                errors = {}
                context = {
                    'form': form,
                    'errors': errors
                }
                return render(request, 'login/client_login.html', context=context)

    context = {
        'form': form
    }

    return render(request, 'login/client_login.html', context=context)