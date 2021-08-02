from django.contrib import admin
from .models import Products
from .models import Order

# Register your models here.
admin.site.site_header = "Ticket MIABE CINEMA"
admin.site.site_title = "MIABE CINE"
admin.site.index_title = "Gestion de MIABE CINEMA"




class ProductAdmin(admin.ModelAdmin):

    def changer_categorie_par_defaut(self, request, queryset):
        queryset.update(categorie="Defaut")

    changer_categorie_par_defaut.short_description ="Categorie par Defaut"
    list_display = ('title', 'prix', 'categorie', 'description')
    search_fields = ('title', 'categorie')
    actions = ('changer_categorie_par_defaut',)
    list_editable = ('prix', 'description', 'categorie')

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
