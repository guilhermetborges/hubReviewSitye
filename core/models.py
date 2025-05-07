from django.db import models
from django.contrib.auth.models import AbstractUser

from stdimage.models import StdImageField


from django.db.models import signals
from django.template.defaultfilters import slugify

class Usuario(AbstractUser):
    username = models.CharField('Usuário', max_length=30, unique=True)


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)  
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2,null=True, blank=True)
    avaliacao = models.CharField('Avaliação', max_length=400, default=None)
    nota = models.IntegerField('Nota', default=0)
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': {'width': 124, 'height': 124}})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome    
    
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)

class Forms(Base):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100, blank=True)
    assunto = models.CharField('Assunto', max_length=120)
    mensagem = models.TextField('Mensagem', max_length=400)


    def __str__(self):
        return self.nome