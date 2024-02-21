from django import forms
from message.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nim', 'name', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 40, 'placeholder': 'Enter your message'}),
        }