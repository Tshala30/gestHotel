from django.contrib import admin
from .models import Client,Chambre  

@admin.register(Client) #
class ClientAdmin(admin.ModelAdmin):
    list_display = ('noms', 'mail', 'genre')
    search_field = ('noms', 'mail')

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
    list_display = ('numero','type_chambre','prix_par_nuit','etat')
    search_field = ('numero','type_chambre')
    list_filter = ('etat', 'type_chambre')


# Register your models here.
