from django import forms
from django.forms import ClearableFileInput
from .models import * 


# Create your forms here.
class TrainerForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = '__all__'
        # widgets = {
        #     'trainer_attachment': ClearableFileInput(attrs={'multiple': True}),
        
        # }