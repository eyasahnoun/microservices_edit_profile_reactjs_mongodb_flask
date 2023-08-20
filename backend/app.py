from controller.admin_controller import admin_controller
from flask_cors import CORS
from flask import Flask,request
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
import logging


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "SDEFfsdA45sdze4AF44hdf8e"  # Clé secrète pour signer le token
app.config["JWT_TOKEN_LOCATION"] = ["headers"]    # Localisation du token (dans les en-têtes)
app.config["JWT_HEADER_TYPE"] = "Bearer"          # Type d'en-tête pour le token

logging.basicConfig(level=logging.DEBUG)

jwt = JWTManager(app)
CORS(app, origins="http://localhost:3000")  # Enable CORS for requests from http://localhost:3000

# Configuration de la connexion MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'edit_profile_microservice',  # Nom de la base de données MongoDB
    'host': 'mongodb://localhost:27017',  # URL de connexion à MongoDB (vous pouvez remplacer par votre URL si nécessaire)
}

# Initialiser l'extension MongoEngine avec l'application Flask
db = MongoEngine(app)
app.register_blueprint(admin_controller)

@app.before_request
def log_request_info():
    # Journalisation des informations sur la requête
    app.logger.debug(f"Request: {request.method} {request.url} - Headers: {request.headers}")
    if request.method == 'POST' or request.method == 'PUT':
        app.logger.debug(f"Request Data: {request.data.decode('utf-8')}")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
