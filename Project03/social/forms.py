from django import forms

from . import models

class UpdateForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['employment', 'location' ,'birthday']