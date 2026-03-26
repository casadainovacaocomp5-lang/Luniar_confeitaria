# 🚀 Backend - Luniar Confeitaria

Backend Python/Flask para o site da Luniar Confeitaria com gerenciamento de produtos, pedidos, depoimentos e contatos.

## 📋 Características

✅ **API RESTful Completa**
- Gerenciamento de produtos
- Criação e rastreamento de pedidos
- Depoimentos/avaliações de clientes
- Sistema de contato
- Newsletter

✅ **Banco de Dados**
- SQLite (desevolvimento)
- PostgreSQL (produção)
- Modelos bem estruturados

✅ **Integração com WhatsApp e Email**
- Envio automático de confirmação de pedidos via WhatsApp
- Notificações por email

✅ **Admin API**
- Estatísticas do site
- Moderação de depoimentos
- Gerenciamento de pedidos

## 🛠️ Instalação

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)

### Passo 1: Criar ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Passo 2: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 3: Configurar variáveis de ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env com suas informações
# Necessário alterar:
# - SECRET_KEY
# - Credenciais de email (opcional)
# - Twilio (opcional para WhatsApp)
```

### Passo 4: Inicizar banco de dados

```bash
python run.py
# O banco será criado automaticamente na primeira execução
```

## 🚀 Rodar o Servidor

```bash
python run.py
```

O servidor estará disponível em: **http://localhost:5000**

## 📚 Documentação da API

### Base URL
```
http://localhost:5000/api
```

---

## 🔌 Endpoints

### 1. **PRODUTOS** (`/api/products`)

#### Listar todos os produtos
```
GET /api/products

Query Parameters:
- category: bolos, cupcakes, doces-finos, sobremesas (opcional)

Exemplo:
GET /api/products?category=bolos
```

**Response:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "Bolo de Chocolate Belga",
      "category": "bolos",
      "description": "...",
      "price": 45.00,
      "image": "assets/images/bolo-chocolate.jpg",
      "is_available": true,
      "rating": 4.8,
      "reviews_count": 15
    }
  ]
}
```

#### Obter produto específico
```
GET /api/products/<id>

Exemplo:
GET /api/products/1
```

#### Produtos por categoria
```
GET /api/products/category/<categoria>

Exemplo:
GET /api/products/category/bolos
```

---

### 2. **PEDIDOS** (`/api/orders`)

#### Criar novo pedido
```
POST /api/orders

Content-Type: application/json

Body:
{
  "name": "João Silva",
  "email": "joao@email.com",
  "phone": "(11) 99999-9999",
  "delivery_date": "2024-04-15",
  "notes": "Sem ovos, por favor",
  "address": "Rua X, 123",
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 5,
      "quantity": 1
    }
  ]
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Pedido criado com sucesso! ✅",
  "data": {
    "id": 1,
    "user_id": 1,
    "status": "pending",
    "total_price": 95.50,
    "items": [...],
    "created_at": "2024-03-19T10:30:00"
  }
}
```

#### Obter pedido específico
```
GET /api/orders/<id>

Exemplo:
GET /api/orders/1
```

---

### 3. **DEPOIMENTOS** (`/api/reviews`)

#### Criar novo depoimento
```
POST /api/reviews

Content-Type: application/json

Body:
{
  "product_id": 1,
  "user_name": "Maria Santos",
  "rating": 5,
  "comment": "Delicioso! Entrega rápida e perfeita!"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Depoimento enviado! Obrigado! 💕",
  "data": {
    "id": 1,
    "product_id": 1,
    "user_name": "Maria Santos",
    "rating": 5,
    "comment": "...",
    "is_approved": false,
    "created_at": "2024-03-19T10:30:00"
  }
}
```

#### Obter depoimentos de um produto
```
GET /api/reviews/product/<product_id>

Exemplo:
GET /api/reviews/product/1
```

---

### 4. **CONTATO** (`/api/contact`)

#### Enviar mensagem de contato
```
POST /api/contact

Content-Type: application/json

Body:
{
  "name": "João Silva",
  "email": "joao@email.com",
  "phone": "(11) 99999-9999",
  "subject": "Dúvida sobre personalização",
  "message": "Vocês fazem bolos sem glúten?"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Mensagem enviada! Responderemos em breve! 📧"
}
```

---

### 5. **NEWSLETTER** (`/api/newsletter`)

#### Inscrever na newsletter
```
POST /api/newsletter/subscribe

Content-Type: application/json

Body:
{
  "email": "cliente@email.com"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Inscrição realizada! Obrigado! 💌"
}
```

---

### 6. **ADMIN** (`/api/admin`)

#### Obter estatísticas
```
GET /api/admin/stats
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "total_orders": 45,
    "total_reviews": 120,
    "total_contacts": 30,
    "total_subscribers": 200,
    "total_users": 150
  }
}
```

---

## 📊 Estructura do Banco de Dados

### Tabelas

**users** - Usuários/Clientes
```
- id (PK)
- name
- email (UNIQUE)
- phone
- address
- created_at
- updated_at
```

**products** - Produtos
```
- id (PK)
- name
- category (bolos, cupcakes, doces-finos, sobremesas)
- description
- price
- image
- is_available
- created_at
- updated_at
```

**orders** - Pedidos
```
- id (PK)
- user_id (FK)
- status (pending, confirmed, preparing, ready, delivered, cancelled)
- order_date
- delivery_date
- total_price
- notes
- created_at
- updated_at
```

**order_items** - Itens dos Pedidos
```
- id (PK)
- order_id (FK)
- product_id (FK)
- quantity
- price
```

**reviews** - Depoimentos
```
- id (PK)
- product_id (FK)
- user_id (FK)
- rating (1-5)
- comment
- is_approved
- created_at
```

**contacts** - Mensagens de Contato
```
- id (PK)
- name
- email
- phone
- subject
- message
- is_read
- created_at
```

**newsletters** - Inscrições Newsletter
```
- id (PK)
- email (UNIQUE)
- is_subscribed
- created_at
```

---

## 🔑 Variáveis de Ambiente

Edite o arquivo `.env`:

```
# Essencial
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta

# Email (Opcional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=seu-email@gmail.com
MAIL_PASSWORD=sua-app-password

# WhatsApp com Twilio (Opcional)
TWILIO_ACCOUNT_SID=seu-sid
TWILIO_AUTH_TOKEN=seu-token
TWILIO_WHATSAPP_NUMBER=+5511999999999
```

### Como obter credenciais:

**Email Gmail:**
1. Ative 2FA em sua conta Google
2. Crie uma [App Password](https://myaccount.google.com/apppasswords)
3. Use a senha gerada no `.env`

**WhatsApp (Twilio):**
1. Crie conta em [Twilio](https://www.twilio.com)
2. Obtenha Account SID e Auth Token
3. Configure um número WhatsApp

---

## 🔌 Integração com Frontend

No seu `script.js`, faça requisições assim:

```javascript
// Criar pedido
const criarPedido = async (dados) => {
  const response = await fetch('http://localhost:5000/api/orders', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(dados)
  });
  return response.json();
};

// Obter produtos
const obterProdutos = async (categoria = null) => {
  let url = 'http://localhost:5000/api/products';
  if (categoria) url += `?category=${categoria}`;
  
  const response = await fetch(url);
  return response.json();
};

// Enviar depoimento
const enviarDepoimento = async (dados) => {
  const response = await fetch('http://localhost:5000/api/reviews', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(dados)
  });
  return response.json();
};
```

---

## 📝 Estrutura de Pastas

```
backend/
├── run.py                  # Arquivo principal
├── config.py              # Configurações
├── requirements.txt       # Dependências
├── .env.example           # Template de variáveis
│
├── app/
│   ├── __init__.py        # Factory da app
│   ├── utils.py           # Utilitários
│   │
│   ├── models/
│   │   └── __init__.py    # Modelos do banco (User, Product, Order, etc)
│   │
│   └── routes/
│       └── __init__.py    # Blueprints/Rotas da API
│
└── instance/
    └── luniar_confeitaria.db  # Banco de dados (criado automaticamente)
```

---

## 🧪 Testando a API

### Usando cURL

```bash
# Listar produtos
curl http://localhost:5000/api/products

# Obter produto
curl http://localhost:5000/api/products/1

# Criar pedido
curl -X POST http://localhost:5000/api/orders \
  -H "Content-Type: application/json" \
  -d '{
    "name": "João",
    "email": "joao@email.com",
    "phone": "(11) 99999-9999",
    "delivery_date": "2024-04-15",
    "items": [{"product_id": 1, "quantity": 1}]
  }'
```

### Usando Postman

1. Importe a URL base: `http://localhost:5000/api`
2. Configure requisições como nos exemplos acima
3. Teste cada endpoint

---

## 🌐 Deploy em Produção

### Usando Gunicorn + Nginx

```bash
# Instale Gunicorn
pip install gunicorn

# Rode
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Usando Heroku

```bash
# Login
heroku login

# Crie app
heroku create luniar-confeitaria-api

# Configure variáveis
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=sua-chave

# Deploy
git push heroku main
```

### Usando Railway/Render

1. Conecte seu repositório GitHub
2. Configure variáveis de ambiente
3. Deploy automático

---

## 📞 Suporte

Se tiver problemas:

1. Verifique arquivo `run.py`
2. Confirme que `requirements.txt` foi instalado
3. Veja logs no console
4. Teste endpoints com cURL ou Postman

---

## 📄 Licença

Este projeto é livre para uso pessoal e comercial.

---

**Última atualização:** Março 2024
**Versão:** 1.0
**Status:** ✅ Pronto para usar
