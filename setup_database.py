#!/usr/bin/env python3
"""
Script de configuration de la base de données MongoDB
pour le système de gestion d'inventaire Flask
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
import bcrypt
from datetime import datetime

def setup_database():
    """Configure la base de données MongoDB avec les utilisateurs et données par défaut"""
    
    try:
        # Connexion à MongoDB
        print("🔌 Connexion à MongoDB...")
        client = MongoClient('mongodb://localhost:27017/')
        
        # Créer/accéder à la base de données
        db = client['inventory_db']
        print("✅ Base de données 'inventory_db' accessible")
        
        # Créer les collections
        collections = ['users', 'equipment', 'rental_requests']
        for collection_name in collections:
            if collection_name not in db.list_collection_names():
                db.create_collection(collection_name)
                print(f"✅ Collection '{collection_name}' créée")
            else:
                print(f"ℹ️  Collection '{collection_name}' existe déjà")
        
        # Créer les utilisateurs par défaut
        setup_default_users(db)
        
        # Créer des équipements d'exemple
        setup_sample_equipment(db)
        
        print("\n🎉 Configuration de la base de données terminée avec succès!")
        print("\n👥 Utilisateurs créés:")
        print("   • Admin: admin / admin123")
        print("   • Technicien: technicien / tech123")
        print("   • Professeur: professeur / prof123")
        print("   • Étudiant: etudiant / etud123")
        print("\n🌐 Accédez à l'application sur: http://127.0.0.1:5000")
        
    except Exception as e:
        print(f"❌ Erreur lors de la configuration: {e}")
        print("\n🔧 Vérifiez que:")
        print("   1. MongoDB est démarré")
        print("   2. MongoDB est accessible sur localhost:27017")
        print("   3. Vous avez les permissions nécessaires")

def setup_default_users(db):
    """Crée les utilisateurs par défaut avec des rôles différents"""
    
    users_collection = db['users']
    
    # Vérifier si des utilisateurs existent déjà
    if users_collection.count_documents({}) > 0:
        print("ℹ️  Des utilisateurs existent déjà, passage de la création...")
        return
    
    # Définir les utilisateurs par défaut
    default_users = [
        {
            'username': 'admin',
            'password': bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt()),
            'role': 'admin',
            'email': 'admin@example.com',
            'created_at': datetime.now(),
            'is_active': True
        },
        {
            'username': 'technicien',
            'password': bcrypt.hashpw('tech123'.encode('utf-8'), bcrypt.gensalt()),
            'role': 'technicien laboratoire',
            'email': 'technicien@example.com',
            'created_at': datetime.now(),
            'is_active': True
        },
        {
            'username': 'professeur',
            'password': bcrypt.hashpw('prof123'.encode('utf-8'), bcrypt.gensalt()),
            'role': 'professeur',
            'email': 'professeur@example.com',
            'created_at': datetime.now(),
            'is_active': True
        },
        {
            'username': 'etudiant',
            'password': bcrypt.hashpw('etud123'.encode('utf-8'), bcrypt.gensalt()),
            'role': 'etudiant',
            'email': 'etudiant@example.com',
            'created_at': datetime.now(),
            'is_active': True
        }
    ]
    
    # Insérer les utilisateurs
    result = users_collection.insert_many(default_users)
    print(f"✅ {len(result.inserted_ids)} utilisateurs créés")

def setup_sample_equipment(db):
    """Crée des équipements d'exemple pour tester le système"""
    
    equipment_collection = db['equipment']
    
    # Vérifier si des équipements existent déjà
    if equipment_collection.count_documents({}) > 0:
        print("ℹ️  Des équipements existent déjà, passage de la création...")
        return
    
    # Équipements d'exemple
    sample_equipment = [
        {
            'id': 'ITEM_001',
            'designation': 'Ordinateur portable HP',
            'category': 'Informatique',
            'marque': 'HP',
            'modele': 'Pavilion 15',
            'n_serie': 'HP123456789',
            'ancien_cab': 'CAB001',
            'nouveau_cab': 'CAB001',
            'date_inv': '2024-01-15',
            'quantite_totale': 5,
            'quantite_disponible': 3,
            'quantite_cassée': 1,
            'quantite_en_réparation': 1,
            'quantite_indisponible': 0,
            'quantite_perdue': 0,
            'status': 'Disponible',
            'condition': 'Bon état',
            'description': 'Ordinateurs portables pour les étudiants en informatique',
            'image': '',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        },
        {
            'id': 'ITEM_002',
            'designation': 'Microscope optique',
            'category': 'Laboratoire',
            'marque': 'Olympus',
            'modele': 'CX23',
            'n_serie': 'OLY789456123',
            'ancien_cab': 'CAB002',
            'nouveau_cab': 'CAB002',
            'date_inv': '2024-01-20',
            'quantite_totale': 10,
            'quantite_disponible': 8,
            'quantite_cassée': 1,
            'quantite_en_réparation': 1,
            'quantite_indisponible': 0,
            'quantite_perdue': 0,
            'status': 'Disponible',
            'condition': 'Bon état',
            'description': 'Microscopes pour les cours de biologie',
            'image': '',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        },
        {
            'id': 'ITEM_003',
            'designation': 'Projecteur vidéo',
            'category': 'Audiovisuel',
            'marque': 'Epson',
            'modele': 'EB-X41',
            'n_serie': 'EPS456789123',
            'ancien_cab': 'CAB003',
            'nouveau_cab': 'CAB003',
            'date_inv': '2024-01-25',
            'quantite_totale': 3,
            'quantite_disponible': 2,
            'quantite_cassée': 0,
            'quantite_en_réparation': 1,
            'quantite_indisponible': 0,
            'quantite_perdue': 0,
            'status': 'Disponible',
            'condition': 'Bon état',
            'description': 'Projecteurs pour les salles de cours',
            'image': '',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
    ]
    
    # Insérer les équipements
    result = equipment_collection.insert_many(sample_equipment)
    print(f"✅ {len(result.inserted_ids)} équipements d'exemple créés")

def create_indexes(db):
    """Crée des index pour optimiser les performances"""
    
    try:
        # Index sur les collections
        db.users.create_index('username', unique=True)
        db.users.create_index('email', unique=True)
        db.equipment.create_index('id', unique=True)
        db.equipment.create_index('category')
        db.equipment.create_index('status')
        db.rental_requests.create_index('user_name')
        db.rental_requests.create_index('status')
        db.rental_requests.create_index('created_at')
        
        print("✅ Index créés pour optimiser les performances")
    except Exception as e:
        print(f"⚠️  Erreur lors de la création des index: {e}")

if __name__ == '__main__':
    print("🚀 Configuration de la base de données MongoDB")
    print("=" * 50)
    
    setup_database()
    
    print("\n" + "=" * 50)
    print("✅ Script terminé!")
