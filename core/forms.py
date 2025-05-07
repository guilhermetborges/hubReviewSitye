from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto, Forms
from django import forms
from .models import Usuario

class UsuarioRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    class Meta:
        model = Usuario
        fields = ['username', 'password']


    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem")
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # 🔐 Criptografa a senha
        if commit:
            user.save()
        return user

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