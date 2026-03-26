"""
Utilitários para enviar emails e mensagens WhatsApp
"""

import requests
from flask import current_app


def send_whatsapp_message(phone_number, message):
    """
    Envia mensagem via WhatsApp usando Twilio
    
    Args:
        phone_number: Número de telefone com código do país (ex: +55119999999)
        message: Mensagem a enviar
    """
    try:
        account_sid = current_app.config.get('TWILIO_ACCOUNT_SID')
        auth_token = current_app.config.get('TWILIO_AUTH_TOKEN')
        from_number = current_app.config.get('TWILIO_WHATSAPP_NUMBER')
        
        if not all([account_sid, auth_token, from_number]):
            print('⚠️  Twilio não configurado. Mensagem não enviada.')
            return False
        
        url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
        
        data = {
            'From': f'whatsapp:{from_number}',
            'To': f'whatsapp:{phone_number}',
            'Body': message
        }
        
        response = requests.post(
            url,
            auth=(account_sid, auth_token),
            data=data
        )
        
        return response.status_code == 201
    
    except Exception as e:
        print(f'❌ Erro ao enviar WhatsApp: {str(e)}')
        return False


def send_email(recipient, subject, body, html=None):
    """
    Envia email (implementar com Flask-Mail em produção)
    
    Args:
        recipient: Email do destinatário
        subject: Assunto do email
        body: Corpo do email em texto
        html: Corpo do email em HTML (opcional)
    """
    try:
        # Por enquanto, apenas loga
        print(f'''
        📧 Email enviado para {recipient}
        Assunto: {subject}
        Mensagem: {body}
        ''')
        return True
    except Exception as e:
        print(f'❌ Erro ao enviar email: {str(e)}')
        return False


def format_order_message(order):
    """
    Formata pedido como mensagem WhatsApp
    
    Args:
        order: Objeto Order
        
    Returns:
        String formatada para WhatsApp
    """
    message = f"""
*PEDIDO CONFIRMADO!* 🎉

📦 *Pedido #{order.id}*
📅 *Data de Entrega:* {order.delivery_date.strftime('%d/%m/%Y')}
💰 *Total:* R$ {order.total_price:.2f}

*Itens:*
"""
    
    for item in order.items:
        message += f"\n• {item.product.name} x{item.quantity} - R$ {item.price:.2f}"
    
    if order.notes:
        message += f"\n\n📝 *Observações:* {order.notes}"
    
    message += f"""

Obrigado por escolher a Luniar Confeitaria! 💕
Você receberá atualizações neste chat.
"""
    
    return message
