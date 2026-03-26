# 🚀 Guia de Deploy - Luniar Confeitaria

## Opção 1: GitHub Pages (GRÁTIS e FÁCIL) ⭐ Recomendado

### Passo a passo:

1. **Crie uma conta no GitHub**
   - Acesse: https://github.com
   - Clique em "Sign up"

2. **Crie um novo repositório**
   - Clique em "New repository"
   - Nome: `luniar-confeitaria` (ou similar)
   - Descrição: "Website da Luniar Confeitaria"
   - Deixe como "Public"
   - Clique "Create repository"

3. **Faça upload dos arquivos**
   ```
   Option A: Usar GitHub Desktop (interface gráfica - mais fácil)
   Option B: Terminal (mais rápido se já usa Git)
   ```

   **Usando GitHub Desktop:**
   - Baixe: https://desktop.github.com
   - Open repository → seu repositório
   - Arraste os arquivos do projeto
   - Escreva a mensagem: "Initial commit"
   - Clique em "Commit to main"
   - Clique em "Publish repository"

   **Usando Terminal:**
   ```bash
   cd seu-projeto-folder
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/seu-usuario/luniar-confeitaria.git
   git push -u origin main
   ```

4. **Ative GitHub Pages**
   - Vá para: Settings → Pages
   - Selecione "main" em "Branch"
   - Clique "Save"
   - Seu site estará em: `https://seu-usuario.github.io/luniar-confeitaria`

5. **Compartilhe o link**
   - Copie a URL do GitHub Pages
   - Compartilhe com clientes!

---

## Opção 2: Netlify (GRÁTIS com funcionalidades adicionais)

### Passo a passo:

1. **Acesse o Netlify**
   - https://www.netlify.com
   - Clique "Sign up"
   - Autentique com GitHub

2. **Crie um novo site**
   - Clique "Add new site"
   - "Import an existing project"
   - Selecione seu repositório GitHub

3. **Configure o deploy**
   - Build command: (deixe em branco)
   - Publish directory: (deixe em branco ou `.`)
   - Clique "Deploy site"

4. **Personalize domínio**
   - Seu site terá um URL automático
   - Você pode comprar um domínio ou usar um subdomínio

---

## Opção 3: Vercel (Performance otimizada)

### Passo a passo:

1. **Acesse Vercel**
   - https://vercel.com
   - Clique "Sign Up"
   - Escolha "Continue with GitHub"

2. **Importe seu projeto**
   - "New Project"
   - Selecione seu repositório

3. **Deploy em 1 clique**
   - Vercel detecta automaticamente
   - Clique "Deploy"

---

## Opção 4: Hospedagem Compartilhada (Hostinger, Locaweb, etc)

### Passo a passo:

1. **Contrate a hospedagem**
   - Escolha provedora: Hostinger, Locaweb, Bluehost
   - Plano: Compartilhada (mais barato, suficiente)
   - Registre seu domínio

2. **Acesse via FTP/cPanel**
   - Receba credenciais do provedor
   - Acesse via cPanel
   - Vá para "File Manager"

3. **Faça upload dos arquivos**
   - Navegue até pasta `public_html`
   - Faça upload de todos os arquivos
   - Coloque `index.html` na raiz

4. **Configure domínio**
   - O provedor direcionará automaticamente
   - Seu site estará ativo em poucas horas

---

## Opção 5: Sua Própria Aplicação Web (Avançado)

### Com Node.js + Express:

```javascript
// app.js
const express = require('express');
const app = express();

app.use(express.static('public'));

app.listen(3000, () => {
    console.log('Site rodando em http://localhost:3000');
});
```

```bash
npm install express
node app.js
```

### Com Python + Flask:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

---

## ✅ Checklist Pré-Deploy

- [ ] Todos os números WhatsApp corretos
- [ ] Links Instagram atualizados
- [ ] Localização correta
- [ ] Horários de funcionamento atualizados
- [ ] Imagens carregadas e otimizadas
- [ ] Testado no desktop (Chrome, Firefox, Safari)
- [ ] Testado no mobile (iPhone, Android)
- [ ] Formulário enviando corretamente
- [ ] Botão WhatsApp flutuante funcionando
- [ ] Animações carregam suavemente
- [ ] Velocidade do site aceitável (< 3s)

---

## 🔍 Testar Antes do Deploy

### Desktop:
```bash
# Abra o arquivo index.html no navegador
file:///caminho-completo/index.html
```

### Mobile (Emulação Chrome):
1. F12 (abrir Developer Tools)
2. Clique em "Toggle device toolbar" (Ctrl+Shift+M)
3. Selecione diferentes dispositivos
4. Teste cliques, scroll, formulário

### Velocidade:
- Google PageSpeed: https://pagespeed.web.dev
- GTmetrix: https://gtmetrix.com

---

## 📱 Criar Atalho na Tela Inicial (PWA)

Adicione ao `<head>` do `index.html`:

```html
<meta name="theme-color" content="#d8a89e">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="apple-touch-icon" href="assets/images/logo-192.png">
<link rel="manifest" href="manifest.json">
```

Crie `manifest.json`:
```json
{
  "name": "Luniar Confeitaria",
  "short_name": "Luniar",
  "description": "Doces artesanais deliciosos",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#d8a89e",
  "orientation": "portrait-primary",
  "icons": [
    {
      "src": "assets/images/logo-192.png",
      "sizes": "192x192",
      "type": "image/png"
    }
  ]
}
```

---

## 🎯 Próximos Passos Após Deploy

1. **Divulgue nas redes sociais**
   - Instagram
   - WhatsApp Business
   - Facebook

2. **Monitore o site**
   - Google Analytics (acompanhe visitantes)
   - Console de Busca (SEO)

3. **Coletor de feedback**
   - Convide clientes a visitar
   - Peça feedback sobre UX

4. **Otimizações futuras**
   - Sistema de agendamento
   - Carrinho de compras
   - Blog com receitas

---

## 🆘 Troubleshooting

### Site não carrega:
- ✓ Verifique se todos os arquivos foram enviados
- ✓ Verifique a URL aplicadaorrectly
- ✓ Limpe cache do navegador (Ctrl+Shift+Delete)

### Links WhatsApp não funcionam:
- ✓ Verifique o número com código do país
- ✓ Teste o link em outro dispositivo
- ✓ Certifique-se de ter WhatsApp instalado

### Imagens não aparecem:
- ✓ Verifique os caminhos das imagens
- ✓ Use caminhos relativos: `assets/images/arquivo.jpg`
- ✓ Nomes sem espaços ou caracteres especiais

### Formulário não envia:
- ✓ Verifique se tem WhatsApp instalado/ativo
- ✓ Teste com número de teste primeiro
- ✓ Verifique no console (F12) por erros

---

## 📚 Manutenção Regular

- [ ] Atualizar cardápio mensalmente
- [ ] Adicionar fotos novas na galeria
- [ ] Responder emails de contato
- [ ] Acompanhar analytics
- [ ] Atualizar horários sazonais
- [ ] Revisar links e funcionalidades

---

## 💰 Custo Aproximado (Anual)

| Opção | Custo | Vantagens |
|-------|-------|-----------|
| GitHub Pages | **R$ 0** | Grátis, controle total |
| Netlify | **R$ 0** | Grátis, build otimizado |
| Vercel | **R$ 0** | Grátis, performance rápida |
| Hostinger | ~**R$ 60** | Domínio .com.br |
| Locaweb | ~**R$ 120** | Suporte em português |

---

**Recomendação:** 
👉 Comece com **GitHub Pages** (grátis, confiável)
👉 Depois compre um **domínio** (.com.br) se necessário
👉 Total: R$ 30-60/ano

---

🎉 **Parabéns! Seu site está pronto para o mundo!**

Qualquer dúvida: consulte a documentação do provedor ou entre em contato com suporte.
