"""
Factory para criar a aplicação Flask
"""

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config
import os

# Inicializar extensões
db = SQLAlchemy()

def create_app(config_name=None):
    """
    Cria e configura a aplicação Flask
    
    Args:
        config_name: Nome da configuração (development, production, testing)
    """
    
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__, static_folder='../', static_url_path='/', instance_relative_config=True)
    
    # Carrega configuração
    app.config.from_object(config[config_name])
    
    # Inicializa extensões
    db.init_app(app)
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # Cria contexto de aplicação
    with app.app_context():
        # Importa models
        from app.models import (
            User, Product, Order, OrderItem, 
            Review, Contact, Newsletter
        )
        
        # Registra blueprints
        from app.routes import (
            api_bp, products_bp, orders_bp, 
            reviews_bp, contact_bp, admin_bp
        )
        
        app.register_blueprint(api_bp)
        app.register_blueprint(products_bp)
        app.register_blueprint(orders_bp)
        app.register_blueprint(reviews_bp)
        app.register_blueprint(contact_bp)
        app.register_blueprint(admin_bp)
        
        # Rota para servir o frontend
        @app.route('/')
        def index():
            return send_from_directory(app.static_folder, 'index.html')
        
        # Cria tabelas
        db.create_all()
    
    return app
