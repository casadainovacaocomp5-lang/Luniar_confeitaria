# 🍰 Luniar Confeitaria - Website

Um site moderno, elegante e responsivo para a Luniar Confeitaria, desenvolvido com HTML5, CSS3 e JavaScript vanilla.

## 📋 Características

✨ **Design Sofisticado**
- Paleta de cores pastel (rosa claro, bege, branco)
- Tipografia elegante com Playfair Display e Montserrat
- Elementos minimalistas e florais
- Layout 100% responsivo

📱 **Totalmente Responsivo**
- Mobile-first design
- Funciona perfeitamente em todos os dispositivos
- Menu hamburger adaptativo

🚀 **Funcionalidades**
- Página inicial com banner atraente
- Página "Sobre nós" com história da confeitaria
- Cardápio com filtros por categoria
- Galeria de trabalhos
- Formulário de encomendas personalizadas
- Seção de contato com informações
- Botão flutuante de WhatsApp
- Integração com WhatsApp para pedidos
- Animações suaves ao rolar a página

## 📂 Estrutura do Projeto

```
Luniar_confeitaria/
├── index.html           # Página principal
├── css/
│   └── style.css       # Estilos completos
├── js/
│   └── script.js       # Interatividades e funcionalidades
└── assets/
    └── images/         # Pasta para suas imagens
```

## 🎨 Cores Utilizadas

- **Primária**: `#f4d4e6` (Rosa Claro)
- **Secundária**: `#ffeef8` (Rosa muito claro)
- **Acentuada**: `#d8a89e` (Bege/Mauve)
- **Gold**: `#d4af6a` (Dourado)
- **Dark**: `#2d2d2d` (Cinza escuro)

## 📝 Como Personalizar

### 1. Número do WhatsApp
Substitua `5511999999999` nos seguintes arquivos:

**js/script.js** (linhas aproximadamente 30, 42, 108, 153):
```javascript
const phone = '5511999999999'; // Substitua pelo seu número
```

### 2. Links das Redes Sociais
**index.html** (seção de contato):
```html
<!-- WhatsApp -->
<a href="https://wa.me/5511999999999">Enviar Mensagem</a>

<!-- Instagram -->
<a href="https://instagram.com/luniar_confeitaria">Seguir</a>
```

### 3. Localização e Horário
**index.html** (seção de contato):
```html
<h3>Localização</h3>
<p>São Paulo - SP</p> <!-- Altere para sua localização -->

<h3>Horário</h3>
<p>Seg-Sex: 10h às 19h<br>Sáb: 10h às 18h<br>Dom: Fechado</p>
```

### 4. Adicionar Imagens
Coloque suas imagens na pasta `assets/images/` e substitua os placeholders:

```html
<div class="produto-imagem">
    <img src="assets/images/seu-bolo.jpg" alt="Descrição">
</div>
```

### 5. Personalizar Cardápio
No `index.html`, seção "Cardápio", edite:
- Nomes dos produtos
- Descrições
- Preços
- Categorias (data-categoria)

### 6. Adicionar Mais Produtos
Copie um card de produto e cole antes do fechamento da div `produtos-grid`:
```html
<div class="card-produto" data-categoria="bolos">
    <div class="produto-imagem">
        <i class="fas fa-cake-candles"></i>
    </div>
    <h3>Seu Produto</h3>
    <p>Descrição do seu produto</p>
    <div class="preco">Preço</div>
    <button class="btn btn-outline">Orçamento</button>
</div>
```

## 🎯 Seções do Site

### Home
- Banner com chama para ação
- Gradiente elegante
- Frase de destaque impactante

### Sobre Nós
- História da confeitaria
- Valores (Amor, Qualidade, Excelência)
- Imagem de destaque

### Cardápio
- Filtros por categoria
- Cards dos produtos com ícones
- Botão de orçamento com integração WhatsApp

### Galeria
- Grid responsivo de fotos
- Efeito hover elegante

### Encomendas
- Formulário completo
- Validação de campos
- Envio automático via WhatsApp

### Contato
- Informações de contato
- Redes sociais
- Horário de funcionamento
- Maps placeholder

## 🔧 Funcionalidades JavaScript

### Menu Mobile
Hamburger menu que se abre e fecha responsivamente

### Filtro de Cardápio
Filtra produtos por categoria em tempo real

### Formulário de Encomendas
- Validação de campos
- Formatação automática de telefone
- Envio via WhatsApp com dados préenchidos

### Animações
- Fade-in ao scroll (Intersection Observer)
- Slide up no carregamento
- Efeito hover nos cards

### Scroll Suave
Links de navegação com scroll suave

## 📱 Responsividade

- **Desktop**: Layout completo com navegação horizontal
- **Tablet**: Ajustes de tamanho de fonte e espaçamento
- **Mobile**: Menu hamburger, layout em coluna única

## 🌐 Como Usar

1. **Abra `index.html` em seu navegador**
2. **Personalize os dados** seguindo as instruções acima
3. **Teste em diferentes dispositivos**
4. **Publique no seu servidor**

## 📦 Dependências Externas

- **Font Awesome 6.4**: Ícones
- **Google Fonts**: Playfair Display e Montserrat

## 🚀 Deploy

### GitHub Pages
1. Crie um repositório no GitHub
2. Faça upload dos arquivos
3. Ative GitHub Pages nas configurações
4. Seu site estará em `https://seu-usuario.github.io/seu-repositorio`

### Hospedagem Compartilhada
1. Faça upload dos arquivos via FTP
2. Configure o `index.html` como arquivo padrão
3. Pronto!

### Vercel/Netlify (Recomendado)
1. Conecte seu repositório GitHub
2. Deploy automático a cada push

## ✅ Checklist de Customização

- [ ] Alterar número do WhatsApp
- [ ] Alterar links do Instagram
- [ ] Alterar localização
- [ ] Alterar horários
- [ ] Adicionar fotos do seu cardápio
- [ ] Atualizar nomes dos produtos
- [ ] Atualizar preços
- [ ] Testar em mobile
- [ ] Deploy do site
- [ ] Compartilhar com clientes

## 🎓 Notas de Desenvolvimento

- Código limpo e comentado
- Progressive Enhancement
- Acessibilidade básica implementada
- Performance otimizada
- Sem dependências pesadas

## 📞 Suporte

Para personalizações avançadas, considere:
- Adicionar formulário de contato email
- Integração com sistema de agendamento
- Carrinho de compras
- Blog/notícias
- Chat ao vivo

## 📄 Licença

Este projeto é livre para uso pessoal e comercial.

---

**Feito com 💖 para a Luniar Confeitaria**

✨ Transformando momentos em doces memórias ✨
