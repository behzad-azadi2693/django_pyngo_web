from django.shortcuts import redirect, render, Http404
from .forms import ContactForm, ContactUsForm
# Create your views here.
from django.contrib import messages
from notifications.signals import notify
from django.contrib.auth import get_user_model
from notifications.models import Notification
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.conf import settings

def language(request, lang):
    path = request.GET.get('next')
    for language_cod, language_name in settings.LANGUAGES:
        if language_cod in path:
            translation.activate(lang)
            return redirect(path.replace(language_cod, lang))

    return redirect('pyngo:index')


def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        print(name, phone)
        if name is not None and phone is not None:
            data = {'name':name, 'phone':phone}
            form =ContactForm(request.POST or None, data)
            if form.is_valid():
                form.save()
                admin = get_user_model().objects.get(id=1)
                msg = f'{name}-{phone}'
                notify.send(admin, recipient=admin, verb='meessage', description=msg)
                messages.success(request, _('Your contact number has been successfully registered Our experts will contact you as soon as possible'), 'primary')
                print('ok')
                return redirect('pyngo:index')
            else:
                messages.warning(request, _('Your contact number was not registered successfully. Please try again'), 'warning')
                print('not ok')
                return redirect('pyngo:index')
        else:
            messages.warning(request, _('Please fill in the number and name field and try again'), 'warning')
            return redirect('pyngo:index')
    else:
        return redirect('pyngo:index')

def services(request):
    return render(request, 'services.html')


def all_notifications(request):
    if not (request.user.is_authenticated and request.user.is_admin):
        return Http404()
    
    else:
        admin_notify = Notification.objects.all()
        all_notify_unread = admin_notify.filter(unread=True).order_by('id')
        all_notify_read = admin_notify.filter(unread=False).order_by('-id')

        context = {
           'all_notify_unread':all_notify_unread,
            'all_notify_read':all_notify_read
        }
        
        return render(request, 'notify.html', context)

def about_us(request):
    return render(request, 'about.html')

#def portfolio(request):
#    return render(request, 'portfolio.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been sent. Wait for a call from the pyngo Web team'), 'primary')
            return redirect('pyngo:contact_us')
        else:
            form = ContactUsForm(request.POST)
            messages.success(request,_('Please be careful filling in the fields') , 'warning')
            return render(request, 'contact.html', {'form':form})
    else:
        form = ContactUsForm()
        return render(request, 'contact.html', {'form':form})
