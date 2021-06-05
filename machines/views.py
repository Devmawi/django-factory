from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from . import models

@login_required(login_url='/admin/login/')
def index(request):
    machines = models.Machine.objects.all()
    return render(request,'machines/index.html', { "machine_list": machines})