from django.db import models
from django.contrib.auth.models import User

# Create your models here.


STATUS = (
    (0, "Rascunho"),
    (1, "Publicado")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    atualizado_em = models.DateTimeField(auto_now=True)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta: #insides the models contains metadata
        ordering = ['-criado_em']#classifica os resultados no campo created_on em ordem decrescente por padrão quando consultamos o banco de dados.

    def __str__(self):#human-readable representation of the object
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') #n entendi muito bem!
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = False)

    class Meta:
        ordering = ['-created_on']# o sinal de negativo é para fazer os comentários mais recentes ficarem em cima da busca(do d.b.)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Enquetes(models.Model):#implementar posteriormente a classe enquetes
    nome_enquete = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enquetes')
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    #--> Pesquisar como implementar uma enquete!

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome_enquete
