from django import forms
# import
from .models import InPut, Balance, OutPut

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'username'
#         ]
#         # widgets = {
#         #     'username': forms.TextInput(attrs={'class': 'form-control'})
#         # }
#     def _clean_fields(self):
#         username = self.cleaned_data.get("username")
#         if "CFE" in username:
#             return username
#         else:
#             return forms.ValidationError("This is not a valid title")
#
class InputForm(forms.ModelForm):
    # date = forms.DateTimeField()
    # user = forms.
    class Meta:
        model = InPut
        fields = [
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