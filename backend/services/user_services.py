# services.py

from dao.admin_dao import get_AllUser_for_admin, get_user_by_id, update_user, deactivate_user, add_user ,get_user_by_email
from models.user import User

class UserService:

    def get_AllUser_for_admin(self, admin_id):  # Ajoutez le paramètre "self"
        return get_AllUser_for_admin(admin_id)

    def get_user_by_email(self, email):
        return get_user_by_email(email)
    
    def get_user_by_id(self, user_id):
        return get_user_by_id(user_id)

    def update_user(self, user_id, data):
        return update_user(user_id,data)

    def deactivate_user(self, user_id):
        return deactivate_user(user_id)

    
    def add_user(self, data):
        return add_user(data)  # Return the result of the add_user function

