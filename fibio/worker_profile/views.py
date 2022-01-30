from django.shortcuts import render

from .forms import WorkerProfile
from .models import Worker
from django.contrib.auth import get_user_model
from categories.models import Category      

User = get_user_model()

# Create your views here.
def register(request):
    form = WorkerProfile(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            image = form.cleaned_data.get('image')
            roles = form.cleaned_data.get('role')
            location = form.cleaned_data.get('location')
            phone_number = form.cleaned_data.get('phone_number')

            try:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                worker = Worker(user=user, image=image, location=location, phone_number=phone_number)
                worker.save()
                roles_to_int = []
                for role in roles:
                    role = Category.objects.get(pk=int(role))
                    worker.role.add(role)
                    worker.save()
            except Exception as e:
                print(e)
                user = None
        else:
            context = {
                'form': form
            }
            return render(request, 'register/register.html', context)

    form = WorkerProfile()

    context = {
        'form': form
    }
    
    return render(request, 'register/register.html', context)