# Generated by Django 5.1.1 on 2025-03-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('MP', 'Matière Première'), ('PF', 'Produit Fini')], max_length=2)),
                ('stock', models.IntegerField()),
                ('seuil_min', models.IntegerField()),
            ],
        ),
    ]
