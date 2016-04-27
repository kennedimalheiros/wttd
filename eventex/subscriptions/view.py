from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionsForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionsForm(request.POST)

        if form.is_valid():
            body = render_to_string('subscriptions/subscripion_email.txt', form.cleaned_data)
            mail.send_mail('Confirmação de inscrição',
                           body,
                           'appagendamoc@gmail.com',
                           ['appagendamoc@gmail.com', form.cleaned_data['email']])

            messages.success(request, 'Inscrição realizada com sucesso!')

            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})
    else:
        context = {'form' : SubscriptionsForm()}
        return render(request, 'subscriptions/subscription_form.html', context)
