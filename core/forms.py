from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto, Forms

class FormsForm(forms.ModelForm):

    class Meta:
        model = Forms
        fields = ['nome', 'email', 'assunto', 'mensagem']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in self.fields.values():
            fields.widget.attrs.update({
                'class': 'w-full p-3 bg-white text-black rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent',
                'placeholder': fields.label, 
             
            })

'''
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = forms.CharField(
            label='Mensagem',
            max_length=500,
            widget=forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded-md text-black h-24 resize-none',
                'rows': 3,
                'placeholder': 'Digite sua mensagem...'
            })
        )
    

        conteudo = f'Nome : {nome} \nAssunto : {assunto} \nE-mail : {email} \nMensagem : {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo site',
            body=conteudo,
            from_email='z2x2p@example.com',
            to=['z2x2p@example.com','01borgesguilherme@gmail.com'],
            headers={'Reply-To': email}
        )
        mail.send()
'''

class ProdutoModelForm(forms.ModelForm):
    NOTA_CHOICES = [(i, str(i)) for i in range(0, 11)]

    nota = forms.ChoiceField(
        choices =NOTA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Nota'
    )




    class Meta:
        model = Produto
        fields = ['nome', 'preco' ,'avaliacao', 'nota','imagem']