from django import forms

class ContactForm(forms.Form):
    Email = forms.EmailField(required=True)
    Assunto = forms.CharField(required=True)
    Mensagem = forms.CharField(widget=forms.Textarea, required=True)
