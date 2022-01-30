from django.shortcuts import render
from .forms import CreateJob
from .models import JobPost

# Create your views here.
def create(request):
    form = CreateJob()

    if request.method == 'POST':
        job_post = CreateJob.object.create()

    context = {
        'form': form
    }

    return render(request, 'create_job/create_job.html', context)