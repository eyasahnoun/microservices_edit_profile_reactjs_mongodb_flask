# dao/admin_dao.py
from pymongo import MongoClient
from flask import jsonify, request
from bson import ObjectId 


client = MongoClient('mongodb://localhost:27017/')
db = client['edit_profile_microservice']
collection = db['users']

def get_AllUser_for_admin(admin_id):  # Ajoutez le paramètre "admin_id"
    users = collection.find({
        "role": "user",
        "id_parent_workspace": admin_id
    })
    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])  # Convertir l'ID en chaîne
        user_list.append(user)
    return user_list


def get_user_by_id(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)})
    if user:
        user['_id'] = str(user['_id'])
        return user
    else:
        return None
    
def get_user_by_email(email):
    user = collection.find_one({'email': (email)})
    if user:
        user['email'] = str(user['email'])
        return user
    else:
        return None
   
def update_user(user_id, data):
    # Remove the '_id' field from the update data
    data.pop('_id', None)  
    collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})
    return True

def deactivate_user(user_id):
    user_object_id = ObjectId(user_id)
    user = collection.find_one({'_id': user_object_id})
    if user:
        user['role'] = 'deactivated'
        collection.update_one({'_id': user_object_id}, {'$set': user})
        return True  # Return True on successful deactivation
    else:
        return False  # Return False if the user is not found


def add_user(data):
    # Set default values and modify the provided data
    if 'role' not in data:
        data['role'] = 'user'
        
    if 'password' not in data:
        data['password'] = '123'

    if 'phone' not in data:
        data['phone'] = None  # Set phone to None if not provided
    
    if 'isVerified' not in data:
        data['isVerified'] = True  # Set isVerified to True if not provided

    try:
        new_user = collection.insert_one(data)
        user_id = str(new_user.inserted_id)
        
        return user_id, 201  # Return the user_id and the status code
    except Exception as e:
        return None, 500