# 💼 Système de Gestion de Stock - Django

Ce projet est une application web développée avec Django, conçue pour gérer les stocks d'une entreprise avec plusieurs rôles : administrateur, responsable de stock et vendeur. 

## 🚀 Fonctionnalités principales

- Gestion des produits, clients et fournisseurs
- Saisie des ventes et des approvisionnements
- Mise à jour automatique du stock
- Rôles utilisateurs avec permissions (Opérateur, Gestionnaire)
- Interface d'administration centralisée

## 🛠️ Installation du projet

1. **Cloner le dépôt :**

```bash
git clone https://github.com/The-Ghost03/Arch-Django.git
cd Arch-Django
```

2. **Créer et activer un environnement virtuel :**

```bash
python -m venv env
env\Scripts\activate  # sous Windows
```

3. **Installer les dépendances :**

```bash
pip install -r requirements.txt
```

4. **Lancer les migrations :**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Lancer le serveur de test :**

```bash
python manage.py runserver
```

## 🔐 Accès utilisateurs

| Rôle            | Nom d'utilisateur | Mot de passe           |
|-----------------|-------------------|------------------------|
| Super Admin     | `admin`           | `admin`                |
| Boss (admin)    | `boss`            | `cabinet-aurelis.com` |
| Vendeur         | `vendeur`         | `cabinet-aurelis.com` |

👉 Accédez au **back-office Django** ici :  
📍 [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## 📁 Contenu du projet

- `models.py` → Modèles des entités (produits, commandes, utilisateurs…)
- `admin.py` → Interface d’administration personnalisée
- `migrations/` → Historique de la base
- `uml/` → Diagrammes UML au format PlantUML
- `README.md` → Ce fichier
- `requirements.txt` → Dépendances

## 📌 À savoir

- Ce projet est lié au **devoir 2** d’Architecture des Systèmes d’Information.
- Les syntaxes PlantUML utilisées pour générer les diagrammes sont disponibles dans le dossier `/uml`.
- Visualisation possible des diagrammes sur [PlantText](https://www.planttext.com/)

## 📜 Licence

Projet académique – tous droits réservés à Yao Konan Franck Schalôm © 2025.
