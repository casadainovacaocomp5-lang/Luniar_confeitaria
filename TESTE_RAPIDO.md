# ✅ TESTE RÁPIDO - Luniar Confeitaria

## 🚀 Como Visualizar o Site Localmente (Sem Servidor)

### Opção 1: Abrir Diretamente no Navegador (Mais Fácil) ⭐

1. **Navegue até a pasta do projeto:**
   ```
   C:\Users\Aluno\Documents\Luniar_confeitaria
   ```

2. **Clique duas vezes em `index.html`**
   - Seu navegador padrão abrirá o site
   - Você verá a página inicial completa

3. **Pronto! Teste as funcionalidades:**
   - ✓ Clique nos links de navegação
   - ✓ Teste o menu mobile (redimensione a janela)
   - ✓ Clique em "Faça seu pedido"
   - ✓ Teste os filtros do cardápio
   - ✓ Role a página para ver animações
   - ✓ Preencha o formulário
   - ✓ Clique no botão WhatsApp flutuante

---

## 💻 Opção 2: Usar um Servidor Local (Recomendado para Testes Avançados)

### Windows - Com Python (Mais Fácil)

**Se tem Python instalado:**
```bash
# Abra PowerShell na pasta do projeto
cd C:\Users\Aluno\Documents\Luniar_confeitaria

# Execute um dos comandos abaixo (depende da versão do Python)
python -m http.server 8000
# ou
python3 -m http.server 8000

# Acesse http://localhost:8000 no navegador
```

### Windows - Com Node.js

**Se tem Node.js instalado:**
```bash
# Instale http-server globalmente
npm install -g http-server

# Na pasta do projeto
cd C:\Users\Aluno\Documents\Luniar_confeitaria

# Inicie o servidor
http-server

# Acesse http://localhost:8080
```

### macOS/Linux

```bash
cd ~/Luniar_confeitaria

# Python 3
python3 -m http.server 8000

# Acesse http://localhost:8000
```

---

## 🧪 Checklist de Testes

### Testes Visuais
- [ ] Navegação aparenta profissional
- [ ] Cores combinam bem (tons pastel)
- [ ] Fonte é elegante e legível
- [ ] Imagens carregam corretamente
- [ ] Espaçamento é consistente

### Testes de Responsividade
- [ ] Desktop (1920x1080): Tudo centralizado
- [ ] Tablet (768x1024): Layout se adapta
- [ ] Mobile (375x667): Menu hamburger funciona
- [ ] Extra pequeno (320x568): Tudo legível

**Como testar:**
1. Abra F12 (Developer Tools)
2. Clique em "Toggle device toolbar" (Ctrl+Shift+M)
3. Selecione diferentes dispositivos no dropdown
4. Teste interações

### Testes de Navegação
- [ ] Clique em "Início" → scroll para home
- [ ] Clique em "Sobre" → vai para seção sobre
- [ ] Clique em "Cardápio" → vai para cardápio
- [ ] Clique em "Galeria" → vai para galeria
- [ ] Clique em "Encomendas" → vai para formulário
- [ ] Clique em "Contato" → vai para contato
- [ ] Links de redes sociais funcionam

### Testes de Cardápio
- [ ] Clique em "Todos" → mostra 12 produtos
- [ ] Clique em "Bolos" → mostra 3 bolos
- [ ] Clique em "Cupcakes" → mostra 3 cupcakes
- [ ] Clique em "Doces Finos" → mostra 3 doces
- [ ] Clique em "Sobremesas" → mostra 3 sobremesas
- [ ] Botões mostram/ocultam com suavidade

### Testes de Formulário
- [ ] Tente enviar vazio → mostra erro
- [ ] Preencha todos os campos
- [ ] Selecione uma data futura
- [ ] Clique em "Enviar Encomenda"
- [ ] WhatsApp abre com mensagem pré-preenchida ✅
- [ ] Formulário limpa após envio

### Testes de WhatsApp
- [ ] Botão verde aparece no canto inferior direito
- [ ] Ao passar o mouse, botão cresce (hover)
- [ ] Clique abre WhatsApp
- [ ] Mensagens têm formatação correta

### Testes de Animações
- [ ] Role a página → elementos vão perdendo opacidade
- [ ] Transições são suaves (sem travamentos)
- [ ] Hover em cards mostra efeito (sobe um pouco)
- [ ] Menu hamburger tem transição (X animado)

### Testes de Performance
- [ ] Página carrega rápido (< 3 segundos)
- [ ] Sem erros no console (F12 → Console)
- [ ] Sem avisos de blocked resources
- [ ] Scroll suave sem lag

---

## 🐛 Problemas Comuns e Soluções

### "Página é exibida em branco"
✓ Certifique-se de que `index.html`, `style.css` e `script.js` estão na pasta correta
✓ Verifique se os caminhos dos arquivos estão relativos

### "Ícones não aparecem"
✓ Verifique sua conexão de internet (Font Awesome é de CDN)
✓ Abra F12 → Console e procure por erros

### "WhatsApp não abre"
✓ Você tem WhatsApp instalado?
✓ Verifique se o número tem o código de país (55)
✓ Teste em outro navegador

### "Formulário não envia"
✓ Confirme que tem WhatsApp Desktop ou no navegador
✓ Verifique se o número de telefone está preenchido
✓ Limpe cache (Ctrl+Shift+Delete)

### "Menu mobile não funciona"
✓ Redimensione a janela (< 768px)
✓ Clique no menu hambúrguer (3 linhas)
✓ Verifique no console se há erros de JS

---

## 📊 Teste de Performance (Google Lighthouse)

1. Abra o site em Chrome
2. F12 → Aba "Lighthouse"
3. Clique "Analyze page load"

**Resultados esperados:**
- Performance: > 80
- Acessibilidade: > 80
- SEO: > 80
- Best Practices: > 80

---

## 🎯 Teste de SEO Rápido

1. **Meta tags**: Abra F12 → Elements → procure por `<meta>`
2. **Título**: Deve ser "Luniar Confeitaria - Doces Artesanais"
3. **Descrição**: Deve estar preenchida no meta description
4. **Estrutura de títulos**: H1 → H2 → H3 (hierarquia correta)

---

## ✅ Teste Completo (Checklist Final)

Antes de publicar, execute este teste completo:

```
TESTES VISUAIS
- [ ] Cores corretas (tons pastel)
- [ ] Tipografia elegante
- [ ] Espaçamento uniforme
- [ ] Sem elementos quebrados

TESTES FUNCIONAIS
- [ ] Links navegam corretamente
- [ ] Menu mobile funciona
- [ ] Filtros de cardápio funcionam
- [ ] Formulário envia via WhatsApp
- [ ] Botão flutuante funciona

TESTES DE RESPONSIVIDADE
- [ ] Desktop: tudo centralizado
- [ ] Tablet: layout adaptado
- [ ] Mobile: menu hamburger
- [ ] Extra pequeno: tudo legível

TESTES DE PERFORMANCE
- [ ] Carrega em < 3 segundos
- [ ] Sem erros no console
- [ ] Scroll suave
- [ ] Animações fluidas

TESTES DE QUALIDADE
- [ ] Sem quebras de layout
- [ ] Sem imagens faltantes
- [ ] Sem links mortos
- [ ] Sem typos ou erros

PRONTO PARA PUBLICAR?
- [ ] Todos os testes passaram
- [ ] Número WhatsApp correto
- [ ] Links sociais corretos
- [ ] Localização correta
```

---

## 🎬 Teste de Vídeo

**Registre um vídeo de teste:**
1. Acesse o site localmente
2. Navegue por todas as seções
3. Teste mobile (F12 → device toolbar)
4. Mostre o formulário funcionando
5. Mostre o WhatsApp integrando

Este vídeo pode ser compartilhado com clientes!

---

## 📱 Teste em Dispositivos Reais

1. **Em seu computador:**
   - Windows: Abra em Chrome, Firefox, Edge
   - macOS: Abra em Chrome, Safari
   - Linux: Abra em Chrome, Firefox

2. **Em seu telefone:**
   - Abra o arquivo via USB ou QR code
   - Teste toque em botões
   - Teste scroll e animações

3. **Em tablet:**
   - Teste responsividade
   - Verifique se menu hamburger aparece

---

## 🎉 Tudo Testado? Você é o Campeão!

Parabéns! Seu site está funcionando perfeito. Agora é hora de:

1. ✅ Adicionar imagens reais
2. ✅ Atualizar números/links
3. ✅ Fazer deploy (veja DEPLOY.md)
4. ✅ Compartilhar com clientes!

---

**Próximo passo:** Veja o arquivo **DEPLOY.md** para publicar seu site online em minutos!

---

*Dúvidas? Consulte os outros arquivos de documentação:*
- 📖 **README.md** - Visão geral
- ⚙️ **CONFIGURACAO.md** - Personalização rápida
- 🎨 **GUIA_AVANCADO.md** - Design e SEO
- 🚀 **DEPLOY.md** - Como publicar
