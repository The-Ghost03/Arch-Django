from django.db import models

class Produit(models.Model):
    TYPE_CHOICES = [
        ('MP', 'Matière Première'),
        ('PF', 'Produit Fini'),
        ('EM', 'Emballage'),
        ('OT', 'Autre'),
    ]
    
    nom = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    stock_actuel = models.IntegerField(null=True, blank=True)
    seuil_minimum = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_expiration = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nom


class Fournisseur(models.Model):
    nom = models.CharField(max_length=255)
    contact = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    adresse = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom


class Client(models.Model):
    nom = models.CharField(max_length=255)
    contact = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom


class CommandeFournisseur(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date_commande = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=50, default="En attente")

    def __str__(self):
        return f"Commande Fournisseur #{self.id}"


class LigneCommandeFournisseur(models.Model):
    commande = models.ForeignKey(CommandeFournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite}"

    
class CommandeClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=50, default="En attente")

    def __str__(self):
        return f"Commande Client #{self.id}"
    
    @property
    def montant_total(self):
        lignes = self.lignecommandeclient_set.all()
        return sum([ligne.prix_total for ligne in lignes])

    def save(self, *args, **kwargs):
        # Sauvegarde de base pour que la commande existe (et donc ait un ID)
        super().save(*args, **kwargs)

        # On récupère les lignes liées à cette commande
        lignes = self.lignecommandeclient_set.all()

        if lignes.exists():
            total_attendu = sum([ligne.prix_total for ligne in lignes])
            total_recu = sum([ligne.montant_recu for ligne in lignes])

            if total_recu >= total_attendu and self.statut != "Traité":
                self.statut = "Traité"
                super().save(update_fields=['statut'])

class LigneCommandeClient(models.Model):
    commande = models.ForeignKey(CommandeClient, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    montant_recu = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def prix_total(self):
        return self.quantite * self.produit.prix_unitaire

    @property
    def monnaie(self):
        return self.montant_recu - self.prix_total

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite}"


class MouvementStock(models.Model):
    TYPE_CHOICES = [
        ('ENTREE', 'Entrée'),
        ('SORTIE', 'Sortie'),
        ('TRANSFERT', 'Transfert'),
        ('RETOUR', 'Retour'),
    ]

    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    quantite = models.IntegerField()
    date_mouvement = models.DateTimeField(auto_now_add=True)
    commentaire = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.produit.nom} ({self.quantite})"
