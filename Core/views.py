from django.shortcuts import render,redirect


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
# Create your views here.

def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Assunto = form.cleaned_data['Assunto']
            Email = form.cleaned_data['Email']
            Mensagem = "{0} te enviou uma mensagem:\n\nAssunto:\n{1}\n\nMensagem:\n{2}".format(Email,Assunto, form.cleaned_data['Mensagem'])
            try:
                send_mail(Assunto, Mensagem, Email, ['hybrid.cercas@gmail.com','ramalho.andre33@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "Core/index.html")
    return render(request, "Core/index.html", {'form': form})
