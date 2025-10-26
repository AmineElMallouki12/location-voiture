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
        print("Connexion à MongoDB...")
        client = MongoClient('mongodb://localhost:27017/')
        
        # Créer/accéder à la base de données
        db = client['voiture_de_location']
        print("Base de données 'voiture_de_location' accessible")
        
        # Créer les collections
        collections = ['users', 'cars', 'rental_requests']
        for collection_name in collections:
            if collection_name not in db.list_collection_names():
                db.create_collection(collection_name)
                print(f"Collection '{collection_name}' créée")
            else:
                print(f"Collection '{collection_name}' existe déjà")
        
        # Créer les utilisateurs par défaut
        setup_default_users(db)
        
        # Créer des voitures d'exemple
        setup_sample_cars(db)
        
        print("\nConfiguration de la base de données terminée avec succès!")
        print("\nUtilisateurs créés:")
        print("   • Admin: admin / admin123")
        print("   • Manager: manager / manager123")
        print("   • Utilisateur: utilisateur / user123")
        print("\nAccédez à l'application sur: http://127.0.0.1:5000")
        
    except Exception as e:
        print(f"Erreur lors de la configuration: {e}")
        print("\nVérifiez que:")
        print("   1. MongoDB est démarré")
        print("   2. MongoDB est accessible sur localhost:27017")
        print("   3. Vous avez les permissions nécessaires")

def setup_default_users(db):
    """Crée les utilisateurs par défaut avec des rôles différents"""
    
    users_collection = db['users']
    
    # Vérifier si des utilisateurs existent déjà
    if users_collection.count_documents({}) > 0:
        print("Des utilisateurs existent déjà, passage de la création...")
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
            'username': 'manager',
            'password': bcrypt.hashpw('manager123'.encode('utf-8'), bcrypt.gensalt()),
            'role': 'manager',
            'email': 'manager@example.com',
            'created_at': datetime.now(),
            'is_active': True
        },
        {
            'username': 'utilisateur',
            'password': bcrypt.hashpw('user123'.encode('utf-8'), bcrypt.gensalt()),
            'role': 'utilisateur',
            'email': 'utilisateur@example.com',
            'created_at': datetime.now(),
            'is_active': True
        }
    ]
    
    # Insérer les utilisateurs
    result = users_collection.insert_many(default_users)
    print(f"{len(result.inserted_ids)} utilisateurs créés")

def setup_sample_cars(db):
    """Crée des voitures d'exemple pour tester le système"""
    
    cars_collection = db['cars']
    
    # Vérifier si des voitures existent déjà
    if cars_collection.count_documents({}) > 0:
        print("Des voitures existent déjà, passage de la création...")
        return
    
    # Voitures d'exemple
    sample_cars = [
        {
            'id': 'CAR_001',
            'designation': 'Toyota Corolla',
            'category': 'Berline',
            'marque': 'Toyota',
            'modele': 'Corolla',
            'n_serie': 'TOY123456789',
            'ancien_cab': 'CAB001',
            'nouveau_cab': 'CAB001',
            'date_inv': '2024-01-15',
            'quantite_totale': 3,
            'quantite_disponible': 2,
            'quantite_cassée': 0,
            'quantite_en_réparation': 1,
            'quantite_indisponible': 0,
            'quantite_perdue': 0,
            'status': 'Disponible',
            'condition': 'Bon état',
            'description': 'Voiture économique idéale pour la ville',
            'prix_journalier': 50,
            'carburant': 'Essence',
            'transmission': 'Manuelle',
            'image': '',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        },
        {
            'id': 'CAR_002',
            'designation': 'BMW X3',
            'category': 'SUV',
            'marque': 'BMW',
            'modele': 'X3',
            'n_serie': 'BMW789456123',
            'ancien_cab': 'CAB002',
            'nouveau_cab': 'CAB002',
            'date_inv': '2024-01-20',
            'quantite_totale': 2,
            'quantite_disponible': 1,
            'quantite_cassée': 0,
            'quantite_en_réparation': 1,
            'quantite_indisponible': 0,
            'quantite_perdue': 0,
            'status': 'Disponible',
            'condition': 'Excellent état',
            'description': 'SUV luxueux pour les familles',
            'prix_journalier': 120,
            'carburant': 'Essence',
            'transmission': 'Automatique',
            'image': '',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        },
        {
            'id': 'CAR_003',
            'designation': 'Renault Clio',
            'category': 'Citadine',
            'marque': 'Renault',
            'modele': 'Clio',
            'n_serie': 'REN456789123',
            'ancien_cab': 'CAB003',
            'nouveau_cab': 'CAB003',
            'date_inv': '2024-01-25',
            'quantite_totale': 5,
            'quantite_disponible': 4,
            'quantite_cassée': 0,
            'quantite_en_réparation': 1,
            'quantite_indisponible': 0,
            'quantite_perdue': 0,
            'status': 'Disponible',
            'condition': 'Bon état',
            'description': 'Voiture compacte parfaite pour la ville',
            'prix_journalier': 35,
            'carburant': 'Essence',
            'transmission': 'Manuelle',
            'image': '',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
    ]
    
    # Insérer les voitures
    result = cars_collection.insert_many(sample_cars)
    print(f"{len(result.inserted_ids)} voitures d'exemple créées")

def create_indexes(db):
    """Crée des index pour optimiser les performances"""
    
    try:
        # Index sur les collections
        db.users.create_index('username', unique=True)
        db.users.create_index('email', unique=True)
        db.cars.create_index('id', unique=True)
        db.cars.create_index('category')
        db.cars.create_index('status')
        db.rental_requests.create_index('user_name')
        db.rental_requests.create_index('status')
        db.rental_requests.create_index('created_at')
        
        print("Index créés pour optimiser les performances")
    except Exception as e:
        print(f"Erreur lors de la création des index: {e}")

if __name__ == '__main__':
    print("Configuration de la base de donnees MongoDB")
    print("=" * 50)
    
    setup_database()
    
    print("\n" + "=" * 50)
    print("Script termine!")
