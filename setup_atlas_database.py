#!/usr/bin/env python3
"""
Script to set up the car rental database in MongoDB Atlas
Run this script with your MongoDB Atlas connection string to create the database and populate it with sample data.
"""

import os
import sys
from pymongo import MongoClient
from datetime import datetime
import bcrypt

def setup_atlas_database(connection_string):
    """Set up the car rental database in MongoDB Atlas"""
    
    try:
        # Connect to MongoDB Atlas
        client = MongoClient(connection_string)
        
        # Test connection
        client.admin.command('ping')
        print("✅ Successfully connected to MongoDB Atlas!")
        
        # Create/access the database
        db = client['voiture_de_location']
        print("✅ Database 'voiture_de_location' accessible")
        
        # Create collections
        collections = ['users', 'cars', 'rental_requests']
        for collection_name in collections:
            if collection_name not in db.list_collection_names():
                db.create_collection(collection_name)
                print(f"✅ Created collection '{collection_name}'")
            else:
                print(f"✅ Collection '{collection_name}' already exists")
        
        # Define default users
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
        
        # Insert default users
        users_collection = db['users']
        for user in default_users:
            existing_user = users_collection.find_one({'username': user['username']})
            if not existing_user:
                users_collection.insert_one(user)
                print(f"✅ Created user: {user['username']}")
            else:
                print(f"✅ User {user['username']} already exists")
        
        # Create sample cars
        sample_cars = [
            {
                'id': 'CAR001',
                'quantity': 2,
                'prix_journalier': 45.0,
                'carburant': 'Essence',
                'transmission': 'Manuelle',
                'designation': 'Renault Clio',
                'category': 'Compacte',
                'marque': 'Renault',
                'modele': 'Clio',
                'n_serie': 'RC001',
                'ancien_cab': 'OLD001',
                'nouveau_cab': 'NEW001',
                'status': 'Disponible',
                'date_inv': '2024-01-15',
                'description': 'Voiture compacte idéale pour la ville',
                'quantite_totale': 2,
                'quantite_cassée': 0,
                'quantite_en_réparation': 0,
                'quantite_disponible': 2,
                'image': 'renaultclio.png',
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            },
            {
                'id': 'CAR002',
                'quantity': 1,
                'prix_journalier': 65.0,
                'carburant': 'Hybride',
                'transmission': 'Automatique',
                'designation': 'Toyota Corolla',
                'category': 'Berline',
                'marque': 'Toyota',
                'modele': 'Corolla',
                'n_serie': 'TC002',
                'ancien_cab': 'OLD002',
                'nouveau_cab': 'NEW002',
                'status': 'Disponible',
                'date_inv': '2024-01-20',
                'description': 'Berline hybride économique et fiable',
                'quantite_totale': 1,
                'quantite_cassée': 0,
                'quantite_en_réparation': 0,
                'quantite_disponible': 1,
                'image': 'toyotacorolla.png',
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            },
            {
                'id': 'CAR003',
                'quantity': 1,
                'prix_journalier': 120.0,
                'carburant': 'Essence',
                'transmission': 'Automatique',
                'designation': 'BMW X3',
                'category': 'SUV',
                'marque': 'BMW',
                'modele': 'X3',
                'n_serie': 'BX003',
                'ancien_cab': 'OLD003',
                'nouveau_cab': 'NEW003',
                'status': 'Disponible',
                'date_inv': '2024-01-25',
                'description': 'SUV premium avec toutes les options',
                'quantite_totale': 1,
                'quantite_cassée': 0,
                'quantite_en_réparation': 0,
                'quantite_disponible': 1,
                'image': 'BMWX3.png',
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }
        ]
        
        # Insert sample cars
        cars_collection = db['cars']
        for car in sample_cars:
            existing_car = cars_collection.find_one({'id': car['id']})
            if not existing_car:
                cars_collection.insert_one(car)
                print(f"✅ Created car: {car['designation']}")
            else:
                print(f"✅ Car {car['designation']} already exists")
        
        # Create indexes for better performance
        try:
            db.users.create_index('username', unique=True)
            db.users.create_index('email', unique=True)
            db.cars.create_index('id', unique=True)
            db.cars.create_index('category')
            db.cars.create_index('status')
            db.rental_requests.create_index('user_name')
            db.rental_requests.create_index('status')
            db.rental_requests.create_index('created_at')
            print("✅ Indexes created for better performance")
        except Exception as e:
            print(f"⚠️  Warning: Some indexes already exist: {e}")
        
        print("\n🎉 Database setup completed successfully!")
        print("\n📋 Default login credentials:")
        print("   Admin: username=admin, password=admin123")
        print("   Manager: username=manager, password=manager123")
        print("   User: username=utilisateur, password=user123")
        
        return True
        
    except Exception as e:
        print(f"❌ Error setting up database: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python setup_atlas_database.py <MONGODB_CONNECTION_STRING>")
        print("\nExample:")
        print("python setup_atlas_database.py 'mongodb+srv://username:password@cluster.mongodb.net/'")
        sys.exit(1)
    
    connection_string = sys.argv[1]
    
    # Add database name to connection string if not present
    if not connection_string.endswith('/voiture_de_location'):
        if connection_string.endswith('/'):
            connection_string += 'voiture_de_location'
        else:
            connection_string += '/voiture_de_location'
    
    print("🚀 Setting up MongoDB Atlas database...")
    print(f"📡 Connection string: {connection_string.replace(connection_string.split('@')[0].split('//')[1], '***:***')}")
    
    success = setup_atlas_database(connection_string)
    
    if success:
        print("\n✅ Database setup completed!")
        print("🔗 You can now use this connection string in Railway:")
        print(f"MONGO_URI={connection_string}")
    else:
        print("\n❌ Database setup failed!")
        sys.exit(1)
