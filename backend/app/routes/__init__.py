"""
Blueprints (Rotas) da Aplicação
"""

from flask import Blueprint

# Blueprint geral da API
api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Verifica se o servidor está funcionando"""
    return {
        'status': 'ok',
        'message': 'Luniar Confeitaria API está online! 🍰'
    }, 200


@api_bp.route('/', methods=['GET'])
def index():
    """Informações da API"""
    return {
        'name': 'Luniar Confeitaria API',
        'version': '1.0.0',
        'description': 'API backend para o site da Luniar Confeitaria',
        'endpoints': {
            'products': '/api/products',
            'orders': '/api/orders',
            'reviews': '/api/reviews',
            'contact': '/api/contact',
            'newsletter': '/api/newsletter'
        }
    }, 200


# Blueprint de Produtos
products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('', methods=['GET'])
def get_products():
    """Lista todos os produtos"""
    from app.models import Product
    
    category = request.args.get('category')
    products = Product.query
    
    if category:
        products = products.filter_by(category=category)
    
    products = products.filter_by(is_available=True).all()
    
    return {
        'status': 'success',
        'data': [product.to_dict() for product in products]
    }, 200


@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Obtém um produto específico"""
    from app.models import Product
    
    product = Product.query.get_or_404(product_id)
    return {
        'status': 'success',
        'data': product.to_dict()
    }, 200


@products_bp.route('/category/<category>', methods=['GET'])
def get_products_by_category(category):
    """Lista produtos por categoria"""
    from app.models import Product
    
    products = Product.query.filter_by(
        category=category,
        is_available=True
    ).all()
    
    return {
        'status': 'success',
        'data': [product.to_dict() for product in products]
    }, 200


# Blueprint de Pedidos
orders_bp = Blueprint('orders', __name__, url_prefix='/api/orders')

@orders_bp.route('', methods=['POST'])
def create_order():
    """Cria um novo pedido"""
    from flask import request, jsonify
    from app.models import User, Order, OrderItem, Product
    from app import db
    from app.utils import send_whatsapp_message, format_order_message
    from datetime import datetime
    
    try:
        data = request.get_json()
        
        # Validação
        required_fields = ['name', 'email', 'phone', 'delivery_date', 'items']
        if not all(field in data for field in required_fields):
            return {'status': 'error', 'message': 'Campos obrigatórios faltando'}, 400
        
        # Cria ou encontra usuário
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            user = User(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                address=data.get('address', '')
            )
            db.session.add(user)
            db.session.commit()
        
        # Cria pedido
        delivery_date = datetime.strptime(data['delivery_date'], '%Y-%m-%d').date()
        total_price = 0
        
        order = Order(
            user_id=user.id,
            delivery_date=delivery_date,
            notes=data.get('notes', '')
        )
        
        # Adiciona itens
        for item in data['items']:
            product = Product.query.get(item['product_id'])
            if not product:
                return {'status': 'error', 'message': f'Produto {item["product_id"]} não encontrado'}, 404
            
            order_item = OrderItem(
                product_id=product.id,
                quantity=item['quantity'],
                price=product.price
            )
            order.items.append(order_item)
            total_price += product.price * item['quantity']
        
        order.total_price = total_price
        db.session.add(order)
        db.session.commit()
        
        # Envia WhatsApp
        message = format_order_message(order)
        send_whatsapp_message(f"+55{data['phone'].replace('-', '').replace('(', '').replace(')', '').replace(' ', '')}", message)
        
        return {
            'status': 'success',
            'message': 'Pedido criado com sucesso! ✅',
            'data': order.to_dict()
        }, 201
    
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Erro ao criar pedido: {str(e)}'
        }, 500


@orders_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Obtém um pedido específico"""
    from app.models import Order
    
    order = Order.query.get_or_404(order_id)
    return {
        'status': 'success',
        'data': order.to_dict()
    }, 200


# Blueprint de Reviews
reviews_bp = Blueprint('reviews', __name__, url_prefix='/api/reviews')

@reviews_bp.route('', methods=['POST'])
def create_review():
    """Cria um novo depoimento"""
    from flask import request
    from app.models import Review, Product, User
    from app import db
    
    try:
        data = request.get_json()
        
        # Validação
        if not all(k in data for k in ['product_id', 'user_name', 'rating', 'comment']):
            return {'status': 'error', 'message': 'Campos obrigatórios faltando'}, 400
        
        # Verifica produto
        product = Product.query.get_or_404(data['product_id'])
        
        # Cria ou encontra usuário
        user = User.query.filter_by(name=data['user_name']).first()
        if not user:
            user = User(name=data['user_name'], email='', phone='')
            db.session.add(user)
            db.session.flush()
        
        # Cria review
        review = Review(
            product_id=product.id,
            user_id=user.id,
            rating=data['rating'],
            comment=data['comment'],
            is_approved=False  # Moderação
        )
        
        db.session.add(review)
        db.session.commit()
        
        return {
            'status': 'success',
            'message': 'Depoimento enviado! Obrigado! 💕',
            'data': review.to_dict()
        }, 201
    
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Erro ao criar depoimento: {str(e)}'
        }, 500


@reviews_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product_reviews(product_id):
    """Obtém depoimentos de um produto"""
    from app.models import Review
    
    reviews = Review.query.filter_by(
        product_id=product_id,
        is_approved=True
    ).order_by(Review.created_at.desc()).all()
    
    return {
        'status': 'success',
        'data': [review.to_dict() for review in reviews]
    }, 200


# Blueprint de Contato
contact_bp = Blueprint('contact', __name__, url_prefix='/api/contact')

@contact_bp.route('', methods=['POST'])
def submit_contact():
    """Submete mensagem de contato"""
    from flask import request
    from app.models import Contact
    from app import db
    
    try:
        data = request.get_json()
        
        # Validação
        if not all(k in data for k in ['name', 'email', 'message']):
            return {'status': 'error', 'message': 'Campos obrigatórios faltando'}, 400
        
        # Cria contato
        contact = Contact(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', ''),
            subject=data.get('subject', ''),
            message=data['message']
        )
        
        db.session.add(contact)
        db.session.commit()
        
        return {
            'status': 'success',
            'message': 'Mensagem enviada! Responderemos em breve! 📧'
        }, 201
    
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Erro ao enviar mensagem: {str(e)}'
        }, 500


# Blueprint para Newsletter
newsletter_bp = Blueprint('newsletter', __name__, url_prefix='/api/newsletter')

@newsletter_bp.route('/subscribe', methods=['POST'])
def subscribe_newsletter():
    """Inscreve email na newsletter"""
    from flask import request
    from app.models import Newsletter
    from app import db
    
    try:
        data = request.get_json()
        
        if 'email' not in data:
            return {'status': 'error', 'message': 'Email é obrigatório'}, 400
        
        # Verifica se já existe
        existing = Newsletter.query.filter_by(email=data['email']).first()
        if existing:
            return {'status': 'error', 'message': 'Você já está inscrito!'}, 400
        
        # Inscreve
        newsletter = Newsletter(email=data['email'])
        db.session.add(newsletter)
        db.session.commit()
        
        return {
            'status': 'success',
            'message': 'Inscrição realizada! Obrigado! 💌'
        }, 201
    
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Erro ao inscrever: {str(e)}'
        }, 500


# Blueprint Admin (protegido)
admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@admin_bp.route('/stats', methods=['GET'])
def get_stats():
    """Estatísticas do site"""
    from app.models import Order, Review, Contact, Newsletter, User
    
    try:
        return {
            'status': 'success',
            'data': {
                'total_orders': Order.query.count(),
                'total_reviews': Review.query.count(),
                'total_contacts': Contact.query.count(),
                'total_subscribers': Newsletter.query.filter_by(is_subscribed=True).count(),
                'total_users': User.query.count()
            }
        }, 200
    
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Erro ao buscar estatísticas: {str(e)}'
        }, 500


# Importa request após definir blueprints
from flask import request
