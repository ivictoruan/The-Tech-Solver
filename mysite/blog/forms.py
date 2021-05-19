

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:# pesquisar: sobre a classe Meta Django
        model = Comment
        fields = ('name', 'email', 'body') #pode-se definir dinamicamente o campo fields
