// ========== Elementos do DOM ==========
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');
const whatsappBtn = document.getElementById('whatsappBtn');
const formularioEncomenda = document.getElementById('formularioEncomenda');
const filtroBtns = document.querySelectorAll('.filtro-btn');
const cardsProdutos = document.querySelectorAll('.card-produto');
const navLinksArray = document.querySelectorAll('.nav-link');

// ========== Menu Mobile ==========
menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    menuToggle.classList.toggle('active');
});

// Fechar menu ao clicar em um link
navLinksArray.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        menuToggle.classList.remove('active');
    });
});

// ========== Botão WhatsApp Flutuante ==========
whatsappBtn.addEventListener('click', () => {
    const phone = '5511999999999'; // Substituir com o número real
    const message = encodeURIComponent('Olá! Gostaria de fazer uma encomenda na Luniar Confeitaria.');
    window.open(`https://wa.me/${phone}?text=${message}`, '_blank');
});

// ========== Formulário de Encomendas ==========
formularioEncomenda.addEventListener('submit', (e) => {
    e.preventDefault();

    // Obter dados do formulário
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const telefone = document.getElementById('telefone').value;
    const data = document.getElementById('data').value;
    const tipoDoce = document.getElementById('tipo-doce').value;
    const observacoes = document.getElementById('observacoes').value;

    // Validação básica
    if (!nome || !email || !telefone || !data || !tipoDoce) {
        alert('Por favor, preencha todos os campos obrigatórios.');
        return;
    }

    // Criar mensagem para WhatsApp
    const mensagem = `
*NOVA ENCOMENDA - LUNIAR CONFEITARIA*

*Nome:* ${nome}
*Email:* ${email}
*Telefone:* ${telefone}
*Data da Encomenda:* ${formatarData(data)}
*Tipo de Doce:* ${tipoDoce}
*Observações:* ${observacoes || 'Nenhuma'}

Obrigado por escolher a Luniar Confeitaria!
    `.trim();

    // Enviar via WhatsApp
    const phone = '5511999999999'; // Substituir com o número real
    const mensagemCodificada = encodeURIComponent(mensagem);
    window.open(`https://wa.me/${phone}?text=${mensagemCodificada}`, '_blank');

    // Limpar formulário
    formularioEncomenda.reset();
    
    // Mostrar mensagem de sucesso
    mostrarMensagemSucesso();
});

// Função para formatar data
function formatarData(date) {
    const d = new Date(date + 'T00:00:00');
    const dias = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'];
    const meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
    
    return `${dias[d.getDay()]}, ${d.getDate()} de ${meses[d.getMonth()]} de ${d.getFullYear()}`;
}

// Função para mostrar mensagem de sucesso
function mostrarMensagemSucesso() {
    const mensagem = document.createElement('div');
    mensagem.className = 'sucesso-toast';
    mensagem.innerHTML = '✓ Encomenda enviada com sucesso!';
    mensagem.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #25d366;
        color: white;
        padding: 15px 25px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 9999;
        animation: slideInRight 0.4s ease-out;
    `;

    document.body.appendChild(mensagem);

    setTimeout(() => {
        mensagem.style.animation = 'slideOutRight 0.4s ease-out';
        setTimeout(() => {
            mensagem.remove();
        }, 400);
    }, 3000);
}

// ========== Filtro de Cardápio ==========
filtroBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // Remover classe ativo de todos os botões
        filtroBtns.forEach(b => b.classList.remove('ativo'));
        
        // Adicionar classe ativo ao botão clicado
        btn.classList.add('ativo');

        // Obter filtro
        const filtro = btn.getAttribute('data-filtro');

        // Filtrar cards
        cardsProdutos.forEach(card => {
            if (filtro === 'todos') {
                card.style.display = 'block';
                card.classList.add('fade-in');
            } else {
                const categoria = card.getAttribute('data-categoria');
                if (categoria === filtro) {
                    card.style.display = 'block';
                    card.classList.add('fade-in');
                } else {
                    card.style.display = 'none';
                }
            }
        });
    });
});

// ========== Scroll Animations ==========
function observarElementos() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    });

    // Observar todos os cards de produtos
    cardsProdutos.forEach(card => {
        observer.observe(card);
    });

    // Observar items da galeria
    document.querySelectorAll('.galeria-item').forEach(item => {
        observer.observe(item);
    });

    // Observar items de contato
    document.querySelectorAll('.info-item').forEach(item => {
        observer.observe(item);
    });

    // Observar valores
    document.querySelectorAll('.valor').forEach(item => {
        observer.observe(item);
    });
}

// ========== Passive Event Listener para Scroll ==========
document.addEventListener('DOMContentLoaded', () => {
    observarElementos();

    // Adicionar animação ao navbar ao fazer scroll
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
        const scroll = window.scrollY;
        
        if (scroll > 50) {
            navbar.style.boxShadow = '0 8px 32px rgba(0, 0, 0, 0.15)';
        } else {
            navbar.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.08)';
        }

        lastScroll = scroll;
    }, { passive: true });
});

// ========== Botões "Faça seu pedido" e "Orçamento" ==========
document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        if (btn.textContent.includes('Faça seu pedido') || btn.textContent.includes('Orçamento')) {
            e.preventDefault();
            
            const tipoDoce = btn.closest('.card-produto')?.querySelector('h3')?.textContent || 'Solicitação de Orçamento';
            
            const phone = '5511999999999'; // Substituir com o número real
            const mensagem = encodeURIComponent(`Olá! Gostaria de saber mais sobre: ${tipoDoce}`);
            
            window.open(`https://wa.me/${phone}?text=${mensagem}`, '_blank');
        }
    });
});

// ========== Animação de Digitação para o Título ==========
function efeitorDigitacao() {
    const title = document.querySelector('.hero-title');
    if (!title) return;

    const text = title.textContent;
    title.textContent = '';
    let index = 0;

    const interval = setInterval(() => {
        if (index < text.length) {
            title.textContent += text.charAt(index);
            index++;
        } else {
            clearInterval(interval);
        }
    }, 100);
}

// Inicializar efeito de digitação quando a página carregar
window.addEventListener('load', () => {
    efeitorDigitacao();
});

// ========== Prevenção de Flash de Conteúdo ==========
document.addEventListener('DOMContentLoaded', () => {
    document.body.style.opacity = '1';
});

// ========== Melhorar Performance do Menu Mobile ==========
const handleNavigation = (e) => {
    if (!e.target.closest('.nav-wrapper')) {
        navLinks.classList.remove('active');
        menuToggle.classList.remove('active');
    }
};

document.addEventListener('click', handleNavigation, { passive: true });

// ========== Suavizar Scroll para Links Âncora ==========
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        e.preventDefault();

        const target = document.querySelector(href);
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ========== Validação em Tempo Real do Telefone ==========
const inputTelefone = document.getElementById('telefone');
if (inputTelefone) {
    inputTelefone.addEventListener('input', (e) => {
        let value = e.target.value.replace(/\D/g, '');
        
        if (value.length > 0) {
            if (value.length <= 2) {
                value = `(${value}`;
            } else if (value.length <= 7) {
                value = `(${value.slice(0, 2)}) ${value.slice(2)}`;
            } else {
                value = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7, 11)}`;
            }
        }

        e.target.value = value;
    });
}

// Adicionar style da animação ao documento
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes slideOutRight {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(30px);
        }
    }

    body {
        opacity: 1;
        transition: opacity 0.3s ease;
    }
`;
document.head.appendChild(style);
