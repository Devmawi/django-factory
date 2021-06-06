from django.forms import ModelForm
from .models import Machine

class MachineForm(ModelForm):
    class Meta:
         model = Machine
         fields = ['name']
