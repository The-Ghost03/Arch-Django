# Generated by Django 5.1.1 on 2025-03-22 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_client_fournisseur_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lignecommandeclient',
            old_name='prix_unitaire',
            new_name='montant_recu',
        ),
    ]
