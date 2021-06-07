from machines.forms import MachineForm, ProductForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse, HttpRequest
from . import models
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='/admin/login/')
def index(request):
    machines = models.Machine.objects.all()
    logger.info("Machine count: {0}".format(machines.count()))
    return render(request,'machines/index.html', { "machine_list": machines})

@login_required(login_url='/admin/login/')
def details(request: HttpRequest, id:int):
    machine = get_object_or_404(models.Machine, pk=id)
    return render(request, 'machines/details.html', { 'machine': machine })

@login_required(login_url='/admin/login/')
def delete(request: HttpRequest, id:int):
    machine = get_object_or_404(models.Machine, pk=id)
    machine.delete()
    return redirect("/machines/")

@login_required(login_url='/admin/login/')
def create(request: HttpRequest):
    if request.method.upper() == "GET":
        return render(request, 'machines/create.html', { 'machine': models.Machine() })
    else:
        machineForm = MachineForm(request.POST)
        if machineForm.is_valid():
            machineForm.save()
        return redirect("/machines/")

def create_product(request:HttpRequest):
    form = ProductForm(request.GET or request.POST)
    form.add_error('name', 'ERROR')
    return render(request, 'products/create.html', { 'form': form })