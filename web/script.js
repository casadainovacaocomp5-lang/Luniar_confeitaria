// Dados dos produtos com imagens corretas
const produtos = [
    {
        nome: 'Brownie',
        descricao: 'Brownie delicioso e cremoso',
        preco: 'R$ 8,00',
        categoria: 'doces-finos',
        imagem: 'brownie recheado.jpg'
    },
    {
        nome: 'Torta Cookie de Ninho com Nutela',
        descricao: 'Torta deliciosa com cookies, ninho crocante e cobertura de nutela',
        preco: 'R$ 16,00',
        categoria: 'tortas',
        imagem: 'pastel de ninho com nutella.jpg'
    },
    {
        nome: 'Torta Cookie',
        descricao: 'Torta crocante com cookies premium e recheio delicioso',
        preco: 'R$ 16,00',
        categoria: 'tortas',
        imagem: 'torta de cookie.jpg'
    },
    {
        nome: 'Torta Cookie de Brigadeiro',
        descricao: 'Torta deliciosa com cookies crocantes e recheio cremoso de brigadeiro',
        preco: 'R$ 16,00',
        categoria: 'tortas',
        imagem: 'Brigadeiro-de-Gorgonzola.jpg'
    },
    {
        nome: 'Torta Cookie de Doce de Leite',
        descricao: 'Torta crocante com cookies e doce de leite cremoso',
        preco: 'R$ 16,00',
        categoria: 'tortas',
        imagem: 'pudim.jpeg'
    },
    {
        nome: 'Palha Italiana',
        descricao: 'Doce crocante e delicado feito com calda de açúcar caramelizada',
        preco: 'R$ 8,00',
        categoria: 'doces-finos',
        imagem: 'escondidinho de brownie.jpeg'
    },
    {
        nome: 'Sanduíche Natural',
        descricao: 'Sanduíche fresco e saudável com ingredientes selecionados',
        preco: 'R$ 10,00',
        categoria: 'salgados',
        imagem: 'sanduiche natural.jpeg'
    }
];

// Emoji para galeria
const galeriaEmojis = ['🎂', '🕯️', '🧁', '🍬', '🧁', '🍦'];

// Estado do filtro
let filtroAtual = 'todos';

// Inicializar quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', function() {
    renderizarProdutos();
    renderizarGaleria();
    setupMenuMobile();
    setupFormulario();
    setupFiltros();
});

// Renderizar produtos
function renderizarProdutos() {
    const grid = document.getElementById('produtosGrid');
    const produtosFiltrados = filtroAtual === 'todos' 
        ? produtos 
        : produtos.filter(p => p.categoria === filtroAtual);

    grid.innerHTML = produtosFiltrados.map(produto => `
        <div class="produto-card">
            <div class="produto-image">
                <img src="${produto.imagem}" alt="${produto.nome}" onerror="this.style.display='none'">
            </div>
            <div class="produto-info">
                <h3 class="produto-nome">${produto.nome}</h3>
                <p class="produto-descricao">${produto.descricao}</p>
                <p class="produto-preco">${produto.preco}</p>
            </div>
        </div>
    `).join('');
}

// Renderizar galeria
function renderizarGaleria() {
    const grid = document.getElementById('galeriaGrid');
    grid.innerHTML = galeriaEmojis.map(emoji => `
        <div class="galeria-item">
            ${emoji}
        </div>
    `).join('');
}

// Setup do menu mobile
function setupMenuMobile() {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');

    menuToggle.addEventListener('click', function() {
        navMenu.classList.toggle('active');
    });

    // Fechar menu ao clicar em um link
    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
        });
    });
}

// Setup dos filtros
function setupFiltros() {
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            // Remover ativo de todos os botões
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            
            // Adicionar ativo ao botão clicado
            this.classList.add('active');
            
            // Atualizar filtro
            filtroAtual = this.dataset.filter;
            
            // Renderizar produtos filtrados
            renderizarProdutos();
        });
    });
}

// Setup do formulário
function setupFormulario() {
    const form = document.getElementById('encomendaForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Coletar dados
            const nome = form.querySelector('input[type="text"]').value;
            const email = form.querySelector('input[type="email"]').value;
            const telefone = form.querySelector('input[type="tel"]').value;
            const pedido = form.querySelector('textarea').value;
            
            // Criar mensagem WhatsApp
            const mensagem = `Olá! Gostaria de fazer uma encomenda.%0A%0ANome: ${nome}%0AEmail: ${email}%0ATelefone: ${telefone}%0A%0APedido: ${pedido}`;
            
            // Redirecionar para WhatsApp
            window.open(`https://wa.me/5511999999999?text=${mensagem}`, '_blank');
            
            // Limpar formulário
            form.reset();
        });
    }
}

// Scroll suave para seções
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Fechar menu ao fazer scroll
window.addEventListener('scroll', function() {
    const navMenu = document.getElementById('navMenu');
    if (navMenu && navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
    }
});
