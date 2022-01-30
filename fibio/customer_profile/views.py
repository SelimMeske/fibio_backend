from django.shortcuts import render
from .models import Customer

# Create your views here.
def profile_page(request):

    if request.user:
        user = Customer.objects.get(id=request.user.id)
        context = {
            'user': user
        }
    else:
        print(request.user)
        context = {
            'user': request.user
        }

    return render(request, 'profile_page/customer_profile/profile_page.html', context=context)

def register(request):
    

