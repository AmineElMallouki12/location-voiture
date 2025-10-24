# 🏢 Système de Gestion d'Inventaire - Flask

Un système complet de gestion d'inventaire développé avec Flask, MongoDB et Bootstrap 5.

## ✨ Fonctionnalités

- 🔐 **Authentification multi-rôles** (Admin, Technicien, Professeur, Étudiant)
- 📦 **Gestion d'inventaire** avec catégorisation
- 📅 **Système de réservations** avec approbation en deux étapes
- 📊 **Rapports et exports** (PDF, Excel)
- 🖼️ **Gestion d'images** pour les équipements
- 📱 **Interface responsive** avec Bootstrap 5
- 🔍 **Recherche et filtres** avancés

## 🚀 Installation Rapide

### Prérequis Système

- **Python 3.8+** (recommandé: Python 3.11 ou 3.12)
- **MongoDB** (version 4.4+ ou 5.0+)
- **Git** (optionnel, pour cloner le projet)

### 1. Installation de Python

#### Windows
```bash
# Télécharger depuis python.org
# Ou utiliser winget
winget install Python.Python.3.11
```

#### macOS
```bash
# Avec Homebrew
brew install python@3.11

# Ou télécharger depuis python.org
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3.11-pip python3.11-venv
```

### 2. Installation de MongoDB

#### Windows
```bash
# Télécharger MongoDB Community Server depuis mongodb.com
# Installer avec l'installateur MSI
```

#### macOS
```bash
# Avec Homebrew
brew tap mongodb/brew
brew install mongodb-community

# Démarrer MongoDB
brew services start mongodb-community
```

#### Linux (Ubuntu)
```bash
# Importer la clé publique MongoDB
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

# Ajouter le repository MongoDB
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Installer MongoDB
sudo apt update
sudo apt install mongodb-org

# Démarrer MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod
```

### 3. Configuration du Projet

```bash
# 1. Extraire le fichier ZIP dans un dossier
# 2. Ouvrir un terminal dans ce dossier
# 3. Créer un environnement virtuel
python -m venv venv

# 4. Activer l'environnement virtuel
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 5. Installer les dépendances
pip install -r requirements.txt
```

### 4. Configuration de la Base de Données

```bash
# 1. Démarrer MongoDB
# Windows: MongoDB Compass ou service Windows
# macOS: brew services start mongodb-community
# Linux: sudo systemctl start mongod

# 2. Créer la base de données et les utilisateurs
python setup_database.py
```

### 5. Lancement de l'Application

```bash
# Démarrer l'application
python app.py

# L'application sera accessible sur: http://127.0.0.1:5000
```

## 📋 Dépendances Python

Le fichier `requirements.txt` contient toutes les dépendances nécessaires :

- **Flask** - Framework web
- **Flask-PyMongo** - Intégration MongoDB
- **Flask-Bcrypt** - Chiffrement des mots de passe
- **Flask-Login** - Gestion des sessions utilisateur
- **openpyxl** - Génération de fichiers Excel
- **reportlab** - Génération de fichiers PDF
- **Werkzeug** - Utilitaires web
- **PyMongo** - Driver MongoDB

## ⚙️ Configuration

### Variables d'Environnement

Créez un fichier `.env` à la racine du projet :

```env
# Clé secrète Flask (changez-la en production!)
SECRET_KEY=votre-cle-secrete-tres-longue-et-aleatoire

# Configuration MongoDB
MONGO_URI=mongodb://localhost:27017/inventory_db

# Configuration des uploads
MAX_CONTENT_LENGTH=2097152
UPLOAD_FOLDER=static/uploads
```

### Structure des Dossiers

```
projet_materielle/
├── app.py                 # Application principale
├── requirements.txt       # Dépendances Python
├── setup_database.py      # Script de configuration DB
├── .env                   # Variables d'environnement
├── static/                # Fichiers statiques
│   ├── CSS/              # Styles CSS
│   ├── JS/               # JavaScript
│   └── uploads/          # Images uploadées
├── templates/             # Templates HTML
└── README.md             # Ce fichier
```

## 🔧 Dépannage

### Erreur "MongoDB connection failed"
- Vérifiez que MongoDB est démarré
- Vérifiez l'URI de connexion dans `app.py`

### Erreur "Module not found"
- Vérifiez que l'environnement virtuel est activé
- Réinstallez les dépendances : `pip install -r requirements.txt`

### Erreur "Permission denied" (Linux/macOS)
- Vérifiez les permissions du dossier `static/uploads`
- `chmod 755 static/uploads`

### Port 5000 déjà utilisé
- Changez le port dans `app.py` : `app.run(port=5001)`
- Ou tuez le processus : `lsof -ti:5000 | xargs kill -9`

## 👥 Utilisateurs par Défaut

Après avoir exécuté `setup_database.py`, vous aurez accès à :

- **Admin** : `admin` / `admin123`
- **Technicien** : `technicien` / `tech123`
- **Professeur** : `professeur` / `prof123`
- **Étudiant** : `etudiant` / `etud123`

## 📞 Support

Pour toute question ou problème :
1. Vérifiez ce README
2. Consultez les logs de l'application
3. Vérifiez la console du navigateur pour les erreurs JavaScript

## 🚀 Déploiement en Production

⚠️ **ATTENTION** : Ce projet est conçu pour le développement. Pour la production :

- Changez `SECRET_KEY`
- Utilisez un serveur WSGI (Gunicorn, uWSGI)
- Configurez un reverse proxy (Nginx, Apache)
- Activez HTTPS
- Configurez la journalisation
- Utilisez une base de données MongoDB sécurisée

---

**Développé avec ❤️ pour la gestion d'inventaire** 