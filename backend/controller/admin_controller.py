# controller/admin_controller.py
from flask import Blueprint, jsonify, request
from services.user_services import UserService
from controller.auth_utils import token_required 
from functools import wraps
import os
from flask_jwt_extended import jwt_required ,get_jwt_identity
from dto.dto import ProfileUpdateDTO  


admin_controller = Blueprint("admin_controller", __name__)
user_service = UserService()


SECRET_KEY = os.environ.get('SECRET_KEY', 'SDEFfsdA45sdze4AF44hdf8e')

@admin_controller.route("/users", methods=["GET"])
@token_required
@jwt_required()
def get_AllUser():
    admin_id = get_jwt_identity()  # Obtenez l'ID de l'administrateur à partir du token
    users = user_service.get_AllUser_for_admin(admin_id)
    
    if users:
        return jsonify(users), 200
    return jsonify({"message": "No users found"}), 404



@admin_controller.route("/admin", methods=["POST"])
@token_required
@jwt_required()
def create_user():
    data = request.get_json()
    admin_id = get_jwt_identity()

    # Vérifier si l'email est unique
    existing_user = user_service.get_user_by_email(data['email'])
    if existing_user:
        return jsonify({"message": "Email already exists"}), 400

    # Ajouter l'ID de l'administrateur parent si non fourni
    if 'id_parent_workspace' not in data:
        data['id_parent_workspace'] = admin_id

    result = user_service.add_user(data)
    return jsonify(result)


@admin_controller.route("/admin/<user_id>", methods=["PUT"])
@token_required
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    result = user_service.update_user(user_id, data)
    if result:
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"message": "User not found"}), 404

@admin_controller.route("/admin/<user_id>/deactivate", methods=["PUT"])
@token_required
@jwt_required()
def deactivate_user_route(user_id):
    result = user_service.deactivate_user(user_id)
    if result:
        return jsonify({"message": "User deactivated successfully"}), 200
    return jsonify({"message": "User not found"}), 404



@admin_controller.route('/edit-profile', methods=['POST'])
@token_required
@jwt_required()
def edit_profile():
    data = request.get_json()
    
    # Créez un objet DTO à partir des données reçues
    profile_update_dto = ProfileUpdateDTO(name=data.get('name'), email=data.get('email'))
    
    # Vous pouvez ensuite utiliser l'objet DTO pour la suite du traitement,
    # par exemple pour valider et effectuer la mise à jour du profil
    
    return jsonify({'message': 'Profil mis à jour avec succès'})
