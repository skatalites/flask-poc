# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/health', methods=['GET'])
    def health_check():
        return {"status": "ok"}, 200

    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from app.auth.database import seed
    seed()

    return app