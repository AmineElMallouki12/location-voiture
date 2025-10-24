# 🚀 Déploiement Netlify - Guide Complet

## ⚠️ IMPORTANT - Limitation Netlify

**ATTENTION**: Netlify est principalement conçu pour les sites statiques et les fonctions serverless. Votre application Flask avec MongoDB nécessite des ajustements significatifs.

## 🎯 Recommandations

Pour une application Flask avec MongoDB, nous recommandons fortement :

1. **Railway** - Excellent support Flask/Python
2. **Vercel** - Bon support pour les applications Python
3. **Heroku** - Option classique et fiable
4. **DigitalOcean App Platform** - Alternative robuste

## 📋 Fichiers Créés pour Netlify

Les fichiers suivants ont été créés pour tenter un déploiement sur Netlify :

- `netlify.toml` - Configuration Netlify
- `_redirects` - Règles de redirection
- `index.html` - Page d'accueil statique
- `env.example` - Variables d'environnement
- `build.sh` - Script de build
- `package.json` - Configuration Node.js
- `runtime.txt` - Version Python
- `Procfile` - Configuration pour Heroku
- `DEPLOYMENT.md` - Guide de déploiement complet

## 🚀 Étapes de Déploiement Netlify

### 1. Préparation

```bash
# Assurez-vous que tous les fichiers sont présents
ls -la
```

### 2. Configuration MongoDB Atlas

1. Créez un compte sur [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Créez un cluster gratuit
3. Configurez l'accès réseau (0.0.0.0/0)
4. Créez un utilisateur de base de données
5. Obtenez la chaîne de connexion

### 3. Déploiement

1. Allez sur [Netlify](https://netlify.com)
2. Connectez votre repository GitHub
3. Configurez les variables d'environnement
4. Déployez

### 4. Variables d'Environnement

Dans Netlify Dashboard > Site settings > Environment variables :

```
SECRET_KEY=votre-cle-secrete-tres-longue-et-aleatoire
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/inventory_db?retryWrites=true&w=majority
FLASK_ENV=production
FLASK_DEBUG=False
MAX_CONTENT_LENGTH=2097152
UPLOAD_FOLDER=static/uploads
```

## 🔄 Alternatives Recommandées

### Option 1: Railway (Recommandé)

```bash
# Installation Railway CLI
npm install -g @railway/cli

# Déploiement
railway login
railway init
railway up
```

### Option 2: Vercel

```bash
# Installation Vercel CLI
npm install -g vercel

# Déploiement
vercel --prod
```

### Option 3: Heroku

```bash
# Installation Heroku CLI
# Déploiement
heroku create votre-app-name
git push heroku main
```

## 🛠️ Dépannage Netlify

### Problèmes Courants

1. **Build Failed**: Vérifiez les variables d'environnement
2. **Database Connection**: Vérifiez l'URI MongoDB Atlas
3. **Static Files**: Vérifiez les chemins dans templates

### Logs de Déploiement

- Netlify Dashboard > Deploys > [Deploy] > Deploy log

## 📞 Support

Si vous rencontrez des problèmes avec Netlify :

1. Consultez `DEPLOYMENT.md` pour plus de détails
2. Considérez les alternatives mentionnées
3. Contactez le support Netlify

## 🎯 Conclusion

Bien que les fichiers de configuration Netlify aient été créés, nous recommandons fortement d'utiliser **Railway** ou **Vercel** pour une meilleure expérience de déploiement avec Flask.

---

**Développé avec ❤️ pour la gestion d'inventaire**
