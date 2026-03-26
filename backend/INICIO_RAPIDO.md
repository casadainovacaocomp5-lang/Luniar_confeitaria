# 🚀 Guia Rápido - Backend Python

## ⚡ Instalação em 5 Minutos

### Passo 1: Abrir PowerShell na pasta backend

```powershell
cd C:\Users\Aluno\Documents\Luniar_confeitaria\backend
```

### Passo 2: Criar ambiente virtual

```powershell
python -m venv venv
venv\Scripts\activate
```

Você verá: `(venv) PS C:\...>` na frente do prompt

### Passo 3: Instalar dependências

```powershell
pip install -r requirements.txt
```

Vai demorar alguns minutos...

### Passo 4: Configurar arquivo .env (opcional)

```powershell
# Copie o arquivo de exemplo
Copy-Item .env.example .env

# Ou crie um arquivo .env vazio (aproveita padrões)
```

### Passo 5: Rodar o servidor

```powershell
python run.py
```

O servidor estará em: **http://localhost:5000**

---

## ✅ Testes Rápidos

### 1. Verificar se está online
```
Abra no navegador: http://localhost:5000/api
```

Deve mostrar:
```json
{
  "name": "Luniar Confeitaria API",
  "version": "1.0.0",
  ...
}
```

### 2. Listar produtos
```
http://localhost:5000/api/products
```

### 3. Listar produtos por categoria
```
http://localhost:5000/api/products/category/bolos
```

### 4. Testar com Postman

Importe estas requisições no Postman:

**GET** - Obter todos os produtos
```
GET http://localhost:5000/api/products
```

**POST** - Criar novo pedido
```
POST http://localhost:5000/api/orders

Body (JSON):
{
  "name": "Teste",
  "email": "teste@email.com",
  "phone": "(11) 99999-9999",
  "delivery_date": "2024-04-20",
  "items": [
    {"product_id": 1, "quantity": 1}
  ]
}
```

---

## 🔗 Conectar Frontend com Backend

Edite o arquivo `js/script.js` no seu frontend:

### API Base URL

Adicione no topo:
```javascript
const API_URL = 'http://localhost:5000/api';
```

### Função para criar pedido via API

Substitua a função atual por:
```javascript
formularioEncomenda.addEventListener('submit', async (e) => {
    e.preventDefault();

    const dados = {
        name: document.getElementById('nome').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('telefone').value,
        delivery_date: document.getElementById('data').value,
        items: [
            {
                product_id: 1,  // Fixo por enquanto
                quantity: 1
            }
        ],
        notes: document.getElementById('observacoes').value || ''
    };

    try {
        const response = await fetch(`${API_URL}/orders`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        });

        const result = await response.json();

        if (result.status === 'success') {
            mostrarMensagemSucesso(result.message);
            formularioEncomenda.reset();
        } else {
            alert('Erro: ' + result.message);
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao enviar pedido');
    }
});
```

### Function para carregar produtos

```javascript
async function carregarProdutos(categoria = 'todos') {
    try {
        let url = `${API_URL}/products`;
        if (categoria !== 'todos') {
            url += `?category=${categoria}`;
        }

        const response = await fetch(url);
        const data = await response.json();

        if (data.status === 'success') {
            atualizarGridProdutos(data.data);
        }
    } catch (error) {
        console.error('Erro ao carregar produtos:', error);
    }
}

function atualizarGridProdutos(produtos) {
    const grid = document.querySelector('.produtos-grid');
    grid.innerHTML = '';

    produtos.forEach(produto => {
        const card = `
            <div class="card-produto" data-categoria="${produto.category}">
                <div class="produto-imagem">
                    <i class="fas fa-cake-candles"></i>
                </div>
                <h3>${produto.name}</h3>
                <p>${produto.description}</p>
                <div class="preco">R$ ${produto.price.toFixed(2)}</div>
                <div class="rating">⭐ ${produto.rating} (${produto.reviews_count})</div>
                <button class="btn btn-outline" onclick="adicionarAoCarrinho(${produto.id})">Orçamento</button>
            </div>
        `;
        grid.innerHTML += card;
    });
}

// Carregar produtos ao abrir página
document.addEventListener('DOMContentLoaded', () => {
    carregarProdutos();
    
    // Atualizar filtros
    document.querySelectorAll('.filtro-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const categoria = btn.getAttribute('data-filtro');
            carregarProdutos(categoria);
        });
    });
});
```

---

## 🛑 Problemas Comuns

### Erro: "Module not found"
```
pip install -r requirements.txt
```

### Erro: "Port already in use"
```
# Mude a porta em run.py:
app.run(host='0.0.0.0', port=5001, debug=True)
```

### CORS Error (frontend não conecta)
- Verifique se está em `development`
- Edite `config.py` se necessário

### Banco de dados vazio
- Delete `instance/luniar_confeitaria.db`
- Rode novamente, será criado com produtos padrão

---

## 📊 Verificando o Banco de Dados

### Instale SQLBrowser (opcional)

```powershell
pip install db-browser
```

Depois abra: `instance/luniar_confeitaria.db` com DB Browser

---

## 🚀 Deploy Rápido (Opcional)

### Usando Railway (Recomendado)

1. Crie conta em [railway.app](https://railway.app)
2. Clique "New Project" → "GitHub Repo"
3. Selecione seu repositório
4. Railway detecta automaticamente e faz deploy
5. Configure variáveis em Settings

### Usando Heroku

```powershell
# Instale Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

heroku login
heroku create luniar-api
git push heroku main
heroku logs --tail
```

---

## 📱 Teste Completo Frontend + Backend

1. ✅ Backend rodando: `python run.py`
2. ✅ Frontend aberto: abra `index.html`
3. ✅ Teste o formulário
4. ✅ Veja resposta em http://localhost:5000/api/orders

---

## 🎓 Próximos Passos

- [ ] Instalar e rodar backend
- [ ] Testar endpoints com Postman
- [ ] Conectar frontend ao backend
- [ ] Adicionar autenticação (opcional)
- [ ] Fazer deploy em produção

---

**Dica:** Deixe o terminal aberto com `python run.py` rodando enquanto testa o frontend!

Qualquer erro? Verifique os logs no console do PowerShell.
