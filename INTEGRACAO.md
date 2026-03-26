# 🔗 Integração Frontend + Backend

Guia completo para conectar seu site frontend com o backend Python.

## 📁 Estrutura do Projeto Atualizada

```
Luniar_confeitaria/
├── index.html                    (Frontend)
├── css/style.css
├── js/script.js
│
└── backend/                      (Backend Python/Flask)
    ├── run.py
    ├── config.py
    ├── requirements.txt
    ├── manage.py
    ├── README.md
    ├── INICIO_RAPIDO.md
    │
    ├── app/
    │   ├── __init__.py
    │   ├── utils.py
    │   ├── models/
    │   └── routes/
    │
    └── instance/
        └── luniar_confeitaria.db
```

---

## 🚀 Como Rodar Tudo

### Terminal 1: Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Backend rodará em: `http://localhost:5000`

### Terminal 2: Frontend

```bash
# Abra o index.html no navegador
```

Frontend em: `http://localhost` (ou abra arquivo diretamente)

---

## 🔌 API Endpoints Disponíveis

### **CORE Endpoints**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api` | Info da API |
| GET | `/api/health` | Health check |

### **PRODUTOS**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/products` | Listar todos (com filtro obrigatório) |
| GET | `/api/products/<id>` | Obter produto |
| GET | `/api/products/category/<cat>` | Listar por categoria |

### **PEDIDOS**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/orders` | Criar pedido |
| GET | `/api/orders/<id>` | Obter pedido |

### **DEPOIMENTOS**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/reviews` | Criar depoimento |
| GET | `/api/reviews/product/<id>` | Depoimentos do produto |

### **CONTATO**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/contact` | Enviar mensagem |

### **NEWSLETTER**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/newsletter/subscribe` | Inscrever |

### **ADMIN**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/admin/stats` | Estatísticas |

---

## 💻 Código JavaScript para Integração

### 1. Adicione no início de `js/script.js`

```javascript
// ========== CONFIGURAÇÃO DA API ==========
const API_URL = 'http://localhost:5000/api';

// Função auxiliar para requisições
async function fazerRequisicao(endpoint, metodo = 'GET', dados = null) {
    const opcoes = {
        method: metodo,
        headers: {
            'Content-Type': 'application/json'
        }
    };

    if (dados) {
        opcoes.body = JSON.stringify(dados);
    }

    try {
        const resposta = await fetch(`${API_URL}${endpoint}`, opcoes);
        const resultado = await resposta.json();
        return resultado;
    } catch (erro) {
        console.error('Erro na requisição:', erro);
        return { status: 'error', message: 'Erro de conexão' };
    }
}
```

### 2. Carregrar produtos dinâmicamente

```javascript
// Carregar produtos ao iniciar
async function carregarProdutos(categoria = null) {
    let endpoint = '/products';
    if (categoria && categoria !== 'todos') {
        endpoint = `/products/category/${categoria}`;
    }

    const resultado = await fazerRequisicao(endpoint);
    
    if (resultado.status === 'success') {
        atualizarGridProdutos(resultado.data);
    } else {
        console.error('Erro ao carregar produtos:', resultado.message);
    }
}

function atualizarGridProdutos(produtos) {
    const grid = document.querySelector('.produtos-grid');
    grid.innerHTML = '';

    if (produtos.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center;">Nenhum produto disponível</p>';
        return;
    }

    produtos.forEach(produto => {
        const estrelas = gerarEstrelas(produto.rating);
        const html = `
            <div class="card-produto" data-categoria="${produto.category}">
                <div class="produto-imagem">
                    ${produto.image ? `<img src="${produto.image}" alt="${produto.name}">` : '<i class="fas fa-cake-candles"></i>'}
                </div>
                <h3>${produto.name}</h3>
                <p>${produto.description}</p>
                <div class="preco">R$ ${produto.price.toFixed(2)}</div>
                <div class="rating">${estrelas} (${produto.reviews_count} avaliações)</div>
                <button class="btn btn-outline" onclick="abrirFormularioPedido(${produto.id}, '${produto.name}')">
                    Orçamento
                </button>
            </div>
        `;
        grid.innerHTML += html;
    });
}

function gerarEstrelas(rating) {
    if (rating === 0) return '⭐ Sem avaliações';
    const cheias = Math.floor(rating);
    const meia = rating % 1 > 0.5 ? 1 : 0;
    const vazias = 5 - cheias - meia;
    
    let estrelas = '⭐'.repeat(cheias);
    if (meia) estrelas += '✨';
    
    return `${estrelas} ${rating.toFixed(1)}`;
}

// Atualizar filtros
document.querySelectorAll('.filtro-btn').forEach(btn => {
    btn.addEventListener('click', async () => {
        document.querySelectorAll('.filtro-btn').forEach(b => b.classList.remove('ativo'));
        btn.classList.add('ativo');

        const categoria = btn.getAttribute('data-filtro');
        await carregarProdutos(categoria);
    });
});

// Carregar on page load
document.addEventListener('DOMContentLoaded', () => {
    carregarProdutos();
});
```

### 3. Enviar formulário de pedido para API

```javascript
formularioEncomenda.addEventListener('submit', async (e) => {
    e.preventDefault();

    const dadosPedido = {
        name: document.getElementById('nome').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('telefone').value,
        delivery_date: document.getElementById('data').value,
        address: document.getElementById('endereco')?.value || '',
        items: [
            {
                product_id: 1,  // Será melhorado depois
                quantity: 1
            }
        ],
        notes: document.getElementById('observacoes').value
    };

    const resultado = await fazerRequisicao('/orders', 'POST', dadosPedido);

    if (resultado.status === 'success') {
        mostrarMensagemSucesso(resultado.message);
        formularioEncomenda.reset();
        
        // Opcional: Redirecionar para WhatsApp
        const phone = dadosPedido.phone.replace(/\D/g, '');
        setTimeout(() => {
            window.open(`https://wa.me/55${phone}`, '_blank');
        }, 1000);
    } else {
        alert('Erro: ' + resultado.message);
    }
});
```

### 4. Enviar depoimentos

```javascript
async function enviarDepoimento(produto_id, usuario_nome, rating, comentario) {
    const resultado = await fazerRequisicao('/reviews', 'POST', {
        product_id: produto_id,
        user_name: usuario_nome,
        rating: rating,
        comment: comentario
    });

    if (resultado.status === 'success') {
        console.log('✅ Depoimento enviado!');
        carregarDepoimentosProduto(produto_id);
    } else {
        alert('Erro: ' + resultado.message);
    }
}

async function carregarDepoimentosProduto(produto_id) {
    const resultado = await fazerRequisicao(`/reviews/product/${produto_id}`);
    
    if (resultado.status === 'success') {
        console.log('Depoimentos:', resultado.data);
        // Atualizar UI com depoimentos
    }
}
```

### 5. Contato

```javascript
async function enviarContato(nome, email, telefone, assunto, mensagem) {
    const resultado = await fazerRequisicao('/contact', 'POST', {
        name: nome,
        email: email,
        phone: telefone,
        subject: assunto,
        message: mensagem
    });

    if (resultado.status === 'success') {
        console.log('✅ Mensagem enviada!');
        return true;
    } else {
        console.error('Erro:', resultado.message);
        return false;
    }
}
```

### 6. Newsletter

```javascript
async function inscreverNewsletter(email) {
    const resultado = await fazerRequisicao('/newsletter/subscribe', 'POST', {
        email: email
    });

    if (resultado.status === 'success') {
        console.log('✅ Inscrito!');
        return true;
    } else {
        console.error('Erro:', resultado.message);
        return false;
    }
}
```

---

## 🧪 Testando Integração

### Teste 1: Verificar API Funcionando

```javascript
// No console do navegador (F12)
fetch('http://localhost:5000/api/products')
    .then(r => r.json())
    .then(d => console.log(d));
```

### Teste 2: Criar Pedido

```javascript
fetch('http://localhost:5000/api/orders', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        name: 'Teste',
        email: 'teste@email.com',
        phone: '11999999999',
        delivery_date: '2024-04-20',
        items: [{product_id: 1, quantity: 1}]
    })
})
.then(r => r.json())
.then(d => console.log(d));
```

---

## 🐛 Troubleshooting

### CORS Error
**Erro:** `Access to XMLHttpRequest blocked by CORS policy`

**Solução:** Backend já tem CORS habilitado. Se não funcionar:
```python
# Edite app/__init__.py
CORS(app, origins=["*"])  # Permite tudo em desenvolvimento
```

### API retorna 404
**Erro:** `404 Not Found`

**Solução:** Verifique:
1. Backend está rodando? (`python run.py`)
2. URL correta? (http://localhost:5000)
3. Endpoint existe?

### Banco vazio
**Erro:** Produtos não aparecem

**Solução:**
```bash
# Delete banco e recrie
rm instance/luniar_confeitaria.db
python run.py
```

---

## 📊 Próximas Melhorias

- [ ] Autenticação (login de usuários)
- [ ] Carrinho de compras persiste
- [ ] Rastreamento de pedido
- [ ] Painel admin web
- [ ] Pagamento online
- [ ] Notificações em tempo real

---

## 📚 Documentação Completa

- **Backend:** `/backend/README.md`
- **Frontend:** `/README.md`
- **Início Rápido:** `/backend/INICIO_RAPIDO.md`

---

**🎉 Frontend + Backend pronto para usar!**
