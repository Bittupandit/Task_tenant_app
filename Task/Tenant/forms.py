from django import forms
from django.db.models import fields

from .models import *

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['occupant','month','rent','electricity','water','food','other_bills']
