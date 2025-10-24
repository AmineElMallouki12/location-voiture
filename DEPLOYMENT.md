# 🚀 Guide de Déploiement Netlify

Ce guide vous explique comment déployer votre application Flask sur Netlify.

## ⚠️ Important - Limitations Netlify

**ATTENTION**: Netlify est principalement conçu pour les sites statiques et les fonctions serverless. Votre application Flask avec MongoDB nécessite quelques ajustements pour fonctionner correctement.

## 📋 Prérequis

1. **Compte Netlify** (gratuit)
2. **MongoDB Atlas** (pour la base de données en production)
3. **GitHub/GitLab/Bitbucket** (pour le déploiement continu)

## 🔧 Configuration MongoDB Atlas

### 1. Créer un cluster MongoDB Atlas

1. Allez sur [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Créez un compte gratuit
3. Créez un nouveau cluster
4. Configurez l'accès réseau (0.0.0.0/0 pour Netlify)
5. Créez un utilisateur de base de données

### 2. Obtenir la chaîne de connexion

```
mongodb+srv://username:password@cluster.mongodb.net/inventory_db?retryWrites=true&w=majority
```

## 🚀 Déploiement sur Netlify

### Méthode 1: Déploiement via Git (Recommandé)

1. **Poussez votre code sur GitHub/GitLab**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/votre-username/votre-repo.git
   git push -u origin main
   ```

2. **Connectez Netlify à votre repository**
   - Allez sur [Netlify](https://netlify.com)
   - Cliquez sur "New site from Git"
   - Connectez votre repository

3. **Configurez les paramètres de build**
   - **Build command**: `pip install -r requirements.txt`
   - **Publish directory**: `static`
   - **Python version**: `3.11`

### Méthode 2: Déploiement manuel

1. **Zippez votre projet** (sans le dossier `__pycache__` et `.git`)
2. **Glissez-déposez sur Netlify**
3. **Configurez les variables d'environnement**

## ⚙️ Variables d'Environnement

Dans le dashboard Netlify, ajoutez ces variables :

```
SECRET_KEY=votre-cle-secrete-tres-longue-et-aleatoire
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/inventory_db?retryWrites=true&w=majority
FLASK_ENV=production
FLASK_DEBUG=False
MAX_CONTENT_LENGTH=2097152
UPLOAD_FOLDER=static/uploads
```

## 🔄 Déploiement Continu

Une fois connecté à Git, Netlify redéploiera automatiquement à chaque push.

## 🛠️ Solutions Alternatives

### Option 1: Vercel (Recommandé pour Flask)

Vercel supporte mieux les applications Python/Flask :

1. Allez sur [Vercel](https://vercel.com)
2. Importez votre repository
3. Configurez le build command
4. Déployez

### Option 2: Railway

Railway est excellent pour les applications Flask :

1. Allez sur [Railway](https://railway.app)
2. Connectez votre GitHub
3. Sélectionnez votre repository
4. Configurez les variables d'environnement
5. Déployez

### Option 3: Heroku

Heroku est une option classique :

1. Créez un compte Heroku
2. Installez Heroku CLI
3. Créez une application
4. Configurez les variables d'environnement
5. Déployez

## 🔍 Dépannage

### Erreur "Build failed"

- Vérifiez que `requirements.txt` est présent
- Vérifiez la version Python (3.11 recommandée)
- Vérifiez les variables d'environnement

### Erreur "Database connection failed"

- Vérifiez l'URI MongoDB Atlas
- Vérifiez les permissions de l'utilisateur
- Vérifiez l'accès réseau (0.0.0.0/0)

### Erreur "Static files not found"

- Vérifiez que le dossier `static` existe
- Vérifiez les chemins dans vos templates

## 📞 Support

Si vous rencontrez des problèmes :

1. Vérifiez les logs de déploiement dans Netlify
2. Consultez la documentation Netlify
3. Considérez les alternatives mentionnées ci-dessus

## 🎯 Recommandation

Pour une application Flask avec MongoDB, nous recommandons **Railway** ou **Vercel** plutôt que Netlify, car ils offrent un meilleur support pour les applications Python/Flask.
