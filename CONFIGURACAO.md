<!-- 
    ARQUIVO DE CONFIGURAÇÃO RÁPIDA
    Altere os valores abaixo para personalizar seu site
    Este arquivo serve como referência rápida de todas as alterações necessárias
-->

<!-- =====================================================
    1. DADOS DE CONTATO
    ===================================================== -->

Número do WhatsApp (formato internacional):
ANTES: 5511999999999
DEPOIS: 55 + DDD + NÚMERO (ex: 5511987654321)
Local: js/script.js (linhas 25, 42, 107, 156) e index.html (linha 368)


<!-- =====================================================
    2. REDES SOCIAIS
    ===================================================== -->

Instagram:
ANTES: https://instagram.com/luniar_confeitaria
DEPOIS: https://instagram.com/seu_perfil
Local: index.html (linha 389)


<!-- =====================================================
    3. LOCALIZAÇÃO E HORÁRIO
    ===================================================== -->

Localização:
ANTES: São Paulo - SP
DEPOIS: Sua Cidade - Estado
Local: index.html (linhas 385-387)

Horário:
ANTES: Seg-Sex: 10h às 19h | Sáb: 10h às 18h | Dom: Fechado
DEPOIS: Seus horários
Local: index.html (linhas 398-400)


<!-- =====================================================
    4. ADICIONANDO IMAGENS REAIS
    ===================================================== -->

Passo 1: Coloque suas imagens na pasta: assets/images/

Passo 2: Altere no HTML (exemplo):

ANTES:
<div class="produto-imagem">
    <i class="fas fa-cake-candles"></i>
</div>

DEPOIS:
<div class="produto-imagem">
    <img src="assets/images/bolo-chocolate.jpg" alt="Bolo de Chocolate Belga">
</div>


<!-- =====================================================
    5. EDITANDO O CARDÁPIO
    ===================================================== -->

Estrutura de um produto:

<div class="card-produto" data-categoria="bolos">
    <div class="produto-imagem">
        <i class="fas fa-cake-candles"></i>  <!-- Substitua por <img> se tiver foto -->
    </div>
    <h3>Nome do Produto</h3>               <!-- EDITE: Nome -->
    <p>Descrição breve</p>                <!-- EDITE: Descrição -->
    <div class="preco">Preço</div>        <!-- EDITE: Preço -->
    <button class="btn btn-outline">Orçamento</button>
</div>

Categorias disponíveis (data-categoria):
- bolos
- cupcakes
- doces-finos
- sobremesas

Ícones Font Awesome para cada categoria:
- Bolos: <i class="fas fa-cake-candles"></i>
- Cupcakes: <i class="fas fa-muffin"></i>
- Doces: <i class="fas fa-candy"></i>
- Sobremesas: <i class="fas fa-ice-cream"></i>


<!-- =====================================================
    6. CORES DO SITE (Se quiser alterar)
    ===================================================== -->

Abra: css/style.css (linhas 1-10)

Cores atuais:
--primary: #f4d4e6 (Rosa Claro)
--secondary: #ffeef8 (Rosa Muito Claro)
--accent: #d8a89e (Bege/Mauve)
--gold: #d4af6a (Dourado)
--dark: #2d2d2d (Cinza Escuro)

Exemplo de alteração:
:root {
    --primary: #e6b8d7;    /* Novo rosa */
    --secondary: #f5e6f0;
    --accent: #c097a0;
    /* ... resto das cores ... */
}


<!-- =====================================================
    7. TEXTOS PRINCIPAIS
    ===================================================== -->

Frase de Destaque (Hero):
ANTES: "Transformando momentos em doces memórias"
DEPOIS: Sua frase
Local: index.html (linha 65)

Botão Principal:
ANTES: "Faça seu pedido"
DEPOIS: Seu texto
Local: index.html (linha 66)

Título Sobre Nós:
ANTES: "Uma História de Amor e Sabor"
DEPOIS: Seu título
Local: index.html (linha 76)

Descrição Sobre Nós:
ANTES: Parágrafos atuais
DEPOIS: Sua história
Local: index.html (linhas 77-78)


<!-- =====================================================
    8. FUENTES CUSTOMIZADAS (Opcional)
    ===================================================== -->

Fonte Principal (Títulos): Playfair Display
Fonte Secundária (Texto): Montserrat

Para usar outras fontes (Google Fonts):
1. Acesse: https://fonts.google.com
2. Selecione a fonte desejada
3. Copie o link fornecido
4. Substitua na linha 7 do index.html
5. Altere o font-family em css/style.css


<!-- =====================================================
    9. CHECKLIST FINAL
    ===================================================== -->

✓ Números do WhatsApp atualizados
✓ Links Instagram corretos
✓ Localização e horário definidos
✓ Fotos adicionadas (pasta assets/images/)
✓ Cardápio personalizado
✓ Preços atualizados
✓ Textos da história atualizados
✓ Site testado em desktop
✓ Site testado em mobile
✓ Link publicado aos clientes


<!-- =====================================================
    10. LINKS ÚTEIS
    ===================================================== -->

Font Awesome (Ícones): https://fontawesome.com/icons
Google Fonts: https://fonts.google.com
Cores Pastel: https://coolors.co
Validator HTML: https://validator.w3.org


💡 DICA: Use Ctrl+F para encontrar rapidamente valores para alterar!

-->
