from django import forms

from .models import InPut, Balance, OutPut

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
            # 'status'
        ]

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = [
            'user',
            'input',
            'output',
            'currency'
        ]
class OutPutForm(forms.ModelForm):
    class Meta:
        model = OutPut
        fields = [
            'recipient',
            'amount',
            'payment_method',
            # 'status'
        ]

# class RawInputForm(forms.Form):
#     user = forms.