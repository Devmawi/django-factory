from django.forms import ModelForm
from .models import Machine

# more on https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#overriding-the-default-fields
class MachineForm(ModelForm):
    class Meta:
         model = Machine
         fields = ['name']
