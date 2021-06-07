from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm, widgets, Form, TextInput
from django.forms.fields import CharField
from django.forms.models import ModelFormMetaclass
from .models import Machine, Product

# more on https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#overriding-the-default-fields
class MachineForm(ModelForm):
    class Meta:
         model = Machine
         fields = ['name']

class ProductForm(Form):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}), required=True)
