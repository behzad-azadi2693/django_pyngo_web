from django import forms
from django.db.models import fields
from .models import Contact, ContactUs

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','phone')


class ContactUsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
            self.fields['name'].widget.attrs['placeholder']='نام...'
            self.fields['email'].widget.attrs['placeholder']='ایمیل...'
            self.fields['subject'].widget.attrs['placeholder']='موضوع...'
            self.fields['message'].widget.attrs['placeholder']='پیغام...'

    class Meta:
        model = ContactUs
        fields = ('name','email','subject','message')