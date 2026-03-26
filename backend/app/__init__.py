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
        
        # Inicializa dados padrão
        _init_default_data()
    
    return app


def _init_default_data():
    """Inicializa dados padrão no banco de dados"""
    from app.models import Product
    
    # Se já tem produtos, não cria novamente
    if Product.query.first():
        return
    
    default_products = [
        # Bolos
        Product(
            name='Bolo de Chocolate Belga',
            category='bolos',
            description='Bolo intenso e delicado com três camadas de chocolate premium',
            price=45.00,
            image='assets/images/bolo-chocolate.jpg'
        ),
        Product(
            name='Bolo de Morango e Rafinose',
            category='bolos',
            description='Leveza e frescor em cada porção, com morangos selecionados',
            price=50.00,
            image='assets/images/bolo-morango.jpg'
        ),
        Product(
            name='Bolo Red Velvet',
            category='bolos',
            description='Clássico sofisticado com cobertura de cream cheese artesanal',
            price=55.00,
            image='assets/images/bolo-redvelvet.jpg'
        ),
        # Cupcakes
        Product(
            name='Cupcake Baunilha Premium',
            category='cupcakes',
            description='Macio e perfumado com calda de baunilha francesa',
            price=8.50,
            image='assets/images/cupcake-baunilha.jpg'
        ),
        Product(
            name='Cupcake Chocolate Trufa',
            category='cupcakes',
            description='Intenso e cremoso com calda de trufa belga',
            price=9.00,
            image='assets/images/cupcake-chocolate.jpg'
        ),
        Product(
            name='Cupcake Limão Siciliano',
            category='cupcakes',
            description='Fresco e aromático com cobertura de merengue suíço',
            price=9.00,
            image='assets/images/cupcake-limao.jpg'
        ),
        # Doces Finos
        Product(
            name='Macaron Premium',
            category='doces-finos',
            description='Macarons artesanais em 5 sabores diferentes',
            price=4.50,
            image='assets/images/macaron.jpg'
        ),
        Product(
            name='Brigadeiro Gourmet',
            category='doces-finos',
            description='Diversos sabores: chocolate, pistache, cappuccino',
            price=3.50,
            image='assets/images/brigadeiro.jpg'
        ),
        Product(
            name='Petit Fours',
            category='doces-finos',
            description='Confeitaria francesa minimalista e elegante',
            price=5.00,
            image='assets/images/petitfours.jpg'
        ),
        # Sobremesas
        Product(
            name='Pavê Artesanal',
            category='sobremesas',
            description='Leve e refrescante, perfeito para celebrações',
            price=35.00,
            image='assets/images/pave.jpg'
        ),
        Product(
            name='Mousse de Chocolate',
            category='sobremesas',
            description='Cremosa e aérea com chocolate 70% cacau',
            price=30.00,
            image='assets/images/mousse.jpg'
        ),
        Product(
            name='Ninho com Calda de Caramelo',
            category='sobremesas',
            description='Doce, crocante e irresistivelmente cremoso',
            price=22.00,
            image='assets/images/ninho.jpg'
        ),
    ]
    
    for product in default_products:
        db.session.add(product)
    
    db.session.commit()
    print('✅ Produtos padrão criados com sucesso!')
