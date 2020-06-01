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

        ]
class OutPutForm(forms.ModelForm):
    recipient = forms.CharField(label='Id пользователя VK',)
    amount = forms.DecimalField(label='Сумма вывода',)
    payment_method = forms.ChoiceField(label='Способ вывода',)

    class Meta:
        model = OutPut
        fields = [
            'recipient',
            'amount',
            'payment_method',
            # 'status'
        ]
# class newUser(forms.ModelForm):
#     UniqueConstraint
#     user =
#     class Meta:
#         constraints = [

        # ]
# class RawInputForm(forms.Form):
#     user = forms.