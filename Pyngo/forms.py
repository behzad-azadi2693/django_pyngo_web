from django import forms
from django.db.models import fields
from .models import Contact, ContactUs
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','phone')


class ContactUsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
            self.fields['name'].widget.attrs['placeholder']= _('your name...')
            self.fields['email'].widget.attrs['placeholder']= _('your email...')
            self.fields['subject'].widget.attrs['placeholder']= _('subjecct...')
            self.fields['message'].widget.attrs['placeholder']=_('message...')

    class Meta:
        model = ContactUs
        fields = ('name','email','subject','message')