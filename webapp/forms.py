from django import forms
from .models import UserProfile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'first_name', 'middle_name', 'last_name',
                  'phone_number', 'brgy', 'city', 'province', 'birthdate', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = self.cleaned_data["password"]  # Store password as plain text
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

'''
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transactionType', 'amount']
'''