# app/routes.py
from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from app.auth.schemas import LoginRequestSchema
from app.auth.repository import UserRepository
from app.auth.service import AuthService

auth_bp = Blueprint('auth', __name__)

# Instanciación manual — esto es tu "wiring" sin contenedor DI
_repository = UserRepository()
_auth_service = AuthService(_repository)


@auth_bp.route('/login', methods=['POST'])
def login():
    # 1. Validar el body de entrada
    try:
        data = LoginRequestSchema(**request.get_json())
    except ValidationError as e:
        return jsonify({"error": "Datos inválidos", "detalles": e.errors()}), 400

    # 2. Delegar la lógica al service
    is_authenticated = _auth_service.authenticate(data.username, data.password)

    # 3. Responder según resultado
    if not is_authenticated:
        return jsonify({"error": "Credenciales incorrectas"}), 401

    return jsonify({"message": "Login exitoso", "username": data.username}), 200