from werkzeug.security import generate_password_hash ,check_password_hash
from app.auth.repository import UserRepository

def hash_password(plain_password: str) -> str:
    return generate_password_hash(plain_password)

class AuthService:

    def __init__(self, repository: UserRepository):
        """Genera el hash de un password en texto plano."""
        self.repository = repository

    def authenticate(self, username: str, password: str) -> bool:
        """
        Retorna True si el username existe y el password coincide.
        Retorna False en cualquier otro caso (usuario no existe o password incorrecto).
        """
        user = self.repository.find_by_username(username)

        if user is None:
            # Importante: no revelamos si el error fue "usuario no existe"
            # o "password incorrecto" — por seguridad, siempre la misma respuesta.
            return False

        return check_password_hash(user.password_hash, password)