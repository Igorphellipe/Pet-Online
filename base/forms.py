# Criando um django forms para validar dados e transformar em liguagem Python
# Através de dados enviados pelo usário no formulário

#Metodo form.is_valid() -> Verfica se os campos são validos
#Metodo form.as_p() -> gera um HTML desse formulário em forma de TAG p.

from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
