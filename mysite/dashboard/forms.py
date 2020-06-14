from django import forms
from django.contrib.auth.models import User
from .models import *


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = [""]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
    def _clean_fields(self):
        username = self.cleaned_data.get("username")
        if "CFE" in username:
            return username
        else:
            return forms.ValidationError("This is not a valid title")
#
# class BankForm(forms.Form):
#     card_number = forms.CharField(min_length=16, max_length=16, error_messages={'required': 'Введите номер Вашей карты'})
#     name = forms.CharField(max_length=30)
#     month = forms.ChoiceField('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
#     year = forms.ChoiceField('15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26')
#     cvc = forms.IntegerField(max_value=999, min_value=000)

class InputForm(forms.ModelForm):
    # date = forms.DateTimeField()
    # user = forms.
    text = forms.CharField(label='', required = False, max_length=255,
                           widget=forms.Textarea(
                               attrs={
                                   "placeholder": "Ваше сообщение",
                                   "class": "new-class-name two",
                                   "rows": 8,
                                   "cols": 60,
                               }
                           ))
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Ваше имя"
        }
    )
                          )
    amount = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            "placeholder": "Сумма"
        }
    ))

    class Meta:
        model = InPut
        fields = [
            'name',
            'amount',
            'currency',
            'text',
            # 'status'
        ]
    # def clean_amount(self):
    #     amount = self.cleaned_data.get("amount")
    #     if amount <= 0:
    #         raise forms.ValidationError("Вы ввели сумму меньше или равную 0")
    #     return amount

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = [

        ]
class OutPutForm(forms.ModelForm):
    recipient = forms.CharField(label='Id пользователя VK',)
    amount = forms.DecimalField(label='Сумма вывода',)
    # payment_method = forms.ChoiceField(label='Способ вывода',)

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