from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Avaliador)
admin.site.register(Autor)
admin.site.register(Nota)
admin.site.register(Avaliacao)
admin.site.register(Artigo)
admin.site.register(ArtigoAutor)
admin.site.register(AvaliacaoAvaliador)
admin.site.register(AvaliacaoNota)
