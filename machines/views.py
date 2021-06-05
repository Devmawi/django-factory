from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from . import models
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='/admin/login/')
def index(request):
    machines = models.Machine.objects.all()
    logger.info("Machine count: {0}".format(machines.count()))
    return render(request,'machines/index.html', { "machine_list": machines})