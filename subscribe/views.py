from django.shortcuts import render,redirect
from . import forms
from django.core.mail import send_mail
from django .conf import settings

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'HEY'
        message = 'Hope you are enjoying your Day'
        EMAIL_HOST_USER = 'priyanshs762@gmail.com '
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})



    #note for mass email
    '''
    just change send_mail to send_mass_mail
    and give a tupple=('subject','message','from',['to->1','to->2'])
    send_mass_mail((tupple name), fail_silently=False)
    '''