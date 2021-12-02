from django.shortcuts import redirect, render, Http404
from .forms import ContactForm, ContactUsForm
# Create your views here.
from django.contrib import messages
from notifications.signals import notify
from django.contrib.auth import get_user_model
from notifications.models import Notification

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
                messages.success(request, 'شماره تماس شما با موفقیت ثبت شد کارشناسان ما در اسرع وقت با شما تماس خواهند گرفت', 'primary')
                print('ok')
                return redirect('pyngo:index')
            else:
                messages.warning(request, 'شماره تماس شما با موفقیت ثبت نشد لطفا مجدد اقدام نمایید', 'warning')
                print('not ok')
                return redirect('pyngo:index')
        else:
            messages.warning(request, 'لطفا فیلد شماره و نام را پرکنید و مجدد اقدام نمایید', 'warning')
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
            messages.success(request, 'پیغام شما ارسال شد منتظر تماس از جانب تیم پیمگو وب باشید', 'primary')
            return redirect('pyngo:contact_us')
        else:
            form = ContactUsForm(request.POST)
            messages.success(request, 'لطفا در پر کردن فیلدها دقت فرمایید', 'warning')
            return render(request, 'contact.html', {'form':form})
    else:
        form = ContactUsForm()
        return render(request, 'contact.html', {'form':form})
