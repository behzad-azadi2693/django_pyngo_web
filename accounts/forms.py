from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

messages = {
    'required':_('this field is required'),
    'invalid':_('this field is incorrect'),
    'max_length':_('field size larger than allowed'),
    'min_length':_('field size less than allowed'),
}

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label=_('password'), widget=forms.PasswordInput)
    password_confierm = forms.CharField(label=_('password confierm'), widget=forms.PasswordInput)

    class Meta:
        models = get_user_model()
        fields = ('phone', 'password', 'password_confierm')

    def clean_password_confierm(self):
        cd = self.cleaned_data
        if cd['password'] and cd['password_confierm'] and cd['password'] != cd['password_confierm']:
            raise forms.ValidationError('Password and password are not the same')

        return cd['password_confierm']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        models = get_user_model()
        fields = ('phone', 'password')

    def clean_password(self):
        return self.initial['password']