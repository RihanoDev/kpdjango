from django import forms
from addusers.models import Addusers, Position

class AddUserForm(forms.ModelForm):
    class Meta:
        model = Addusers
        fields = ['name', 'position', 'mobile', 'email', 'password']  # Add more fields if necessary
        # You can also exclude fields using: exclude = ['field_name']
        position = forms.ModelChoiceField(queryset=Position.objects.all(), empty_label=None)

