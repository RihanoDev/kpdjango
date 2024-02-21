from django import forms
from .models import WorkplaceUserNetwork, Department, Division

class WorkplaceUserNetworkForm(forms.ModelForm):
    class Meta:
        model = WorkplaceUserNetwork
        fields = '__all__'