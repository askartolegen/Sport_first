from django import forms
from .models import Boxing


class BoxingCreate(forms.ModelForm):
    class Meta:
        model = Boxing
        fields = '__all__'