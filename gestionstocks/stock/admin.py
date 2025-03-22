from django.contrib import admin
from .models import (
    Produit,
    Fournisseur,
    Client,
    CommandeFournisseur,
    LigneCommandeFournisseur,
    CommandeClient,
    LigneCommandeClient,
    MouvementStock,
)

# 💰 Affichage personnalisé dans la liste des lignes de commande client
class LigneCommandeClientAdmin(admin.ModelAdmin):
    list_display = ['commande', 'produit', 'quantite', 'montant_recu', 'affiche_prix_total', 'affiche_monnaie']

    def affiche_prix_total(self, obj):
        return f"{obj.prix_total} FCFA"
    affiche_prix_total.short_description = 'Total'

    def affiche_monnaie(self, obj):
        return f"{obj.monnaie} FCFA"
    affiche_monnaie.short_description = 'Monnaie'

# 🧾 Inline pour créer les lignes de commande directement dans le formulaire commande

class LigneCommandeClientInline(admin.TabularInline):
    model = LigneCommandeClient
    extra = 1
    fields = ['produit', 'quantite', 'montant_recu', 'affiche_monnaie']
    readonly_fields = ['affiche_monnaie']

    def affiche_monnaie(self, obj):
        if obj.pk:
            return f"{obj.monnaie} FCFA"
        return "-"
    affiche_monnaie.short_description = "Monnaie"

# 📋 Commande Client avec inline
class CommandeClientAdmin(admin.ModelAdmin):
    inlines = [LigneCommandeClientInline]

# ✅ Enregistrement des modèles
admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Client)
admin.site.register(CommandeFournisseur)
admin.site.register(LigneCommandeFournisseur)
admin.site.register(MouvementStock)

admin.site.register(CommandeClient, CommandeClientAdmin)
admin.site.register(LigneCommandeClient, LigneCommandeClientAdmin)
