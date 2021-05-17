from django.contrib import admin
from .models import Post, Enquetes

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','criado_em')
    list_filter = ('status',)
    search_fields = ['title', 'conteudo']
    prepopulated_fields = {'slug':('title',)} #isto faz:


admin.site.register(Post, PostAdmin)
admin.site.register(Enquetes)
