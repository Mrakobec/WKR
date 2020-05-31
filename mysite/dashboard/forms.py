from django import forms

from .models import InPut

class InputForm(forms.ModelForm):
    # date = forms.DateTimeField()
    class Meta:
        model = InPut
        fields = [
            'user',
            'name',
            'amount',
            'currency',
            'text',
            'status'
        ]

# class RawInputForm(forms.Form):
#     user = forms.