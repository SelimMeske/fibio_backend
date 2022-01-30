from django.shortcuts import render
from .models import JobPost

# Create your views here.
def job_posts(request):
    jobs = JobPost.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, 'find_work/find_work.html', context=context)