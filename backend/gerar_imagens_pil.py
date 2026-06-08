#!/usr/bin/env python3
"""
Script para gerar imagens realistas de produtos da Luniar Confeitaria
Usa PIL/Pillow para criar imagens profissionais de cada produto
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import math
import random

# Diretório de saída
IMAGES_DIR = Path(__file__).parent.parent / 'assets' / 'images'
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# Produtos com cores dominantes e descrições
PRODUTOS = [
    {
        'nome': 'brownie',
        'titulo': 'Brownie',
        'cores': [(101, 47, 13), (139, 69, 19), (160, 82, 45), (179, 99, 53)],
        'descricao': 'Brownie Delicioso\ne Cremoso',
        'detalhes': 'Chocolate Premium'
    },
    {
        'nome': 'torta_cookie_ninho_nutela',
        'titulo': 'Torta Cookie de Ninho com Nutela',
        'cores': [(101, 47, 13), (139, 69, 19), (200, 120, 60), (220, 140, 80)],
        'descricao': 'Torta Cookie\nNinho & Nutela',
        'detalhes': 'Cobertura Irresistível'
    },
    {
        'nome': 'torta_cookie',
        'titulo': 'Torta Cookie',
        'cores': [(160, 82, 45), (200, 120, 60), (220, 140, 80), (240, 160, 100)],
        'descricao': 'Torta Cookie\nCrocante e Doce',
        'detalhes': 'Chocolate Suíço'
    },
    {
        'nome': 'torta_cookie_brigadeiro',
        'titulo': 'Torta Cookie de Brigadeiro',
        'cores': [(80, 20, 20), (120, 30, 30), (150, 40, 40), (180, 60, 60)],
        'descricao': 'Torta Brigadeiro\nGourmet',
        'detalhes': 'Cremosa e Fina'
    },
    {
        'nome': 'torta_cookie_doce_leite',
        'titulo': 'Torta Cookie de Doce de Leite',
        'cores': [(200, 140, 70), (220, 160, 90), (240, 180, 110), (250, 200, 130)],
        'descricao': 'Torta Doce de Leite\nTradição Brasileira',
        'detalhes': 'Caramelo Puro'
    },
    {
        'nome': 'palha_italiana',
        'titulo': 'Palha Italiana',
        'cores': [(255, 215, 0), (255, 200, 0), (255, 190, 0), (220, 160, 0)],
        'descricao': 'Palha Italiana\nCrocante',
        'detalhes': 'Açúcar Caramelizado'
    },
    {
        'nome': 'sanduiche_natural',
        'titulo': 'Sanduíche Natural',
        'cores': [(210, 180, 140), (220, 190, 150), (200, 170, 130), (180, 150, 110)],
        'descricao': 'Sanduíche Natural\nFresco e Saudável',
        'detalhes': 'Ingredientes Selecionados'
    },
]

def criar_fundo_gradiente(img, cor1, cor2):
    """Cria um fundo com gradiente entre duas cores"""
    pixels = img.load()
    width, height = img.size
    
    for y in range(height):
        r = int(cor1[0] + (cor2[0] - cor1[0]) * y / height)
        g = int(cor1[1] + (cor2[1] - cor1[1]) * y / height)
        b = int(cor1[2] + (cor2[2] - cor1[2]) * y / height)
        
        for x in range(width):
            pixels[x, y] = (r, g, b)

def desenhar_produto(nome_arquivo, titulo, cores, descricao, detalhes):
    """Cria uma imagem profissional de um produto"""
    try:
        print(f"🎨 Criando imagem: {titulo}...")
        
        # Criar imagem base
        width, height = 1200, 800
        img = Image.new('RGB', (width, height), color=cores[0])
        
        # Adicionar gradiente de fundo
        criar_fundo_gradiente(img, cores[0], cores[1])
        
        # Desenhar
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Adicionar formas decorativas (círculos com efeito de produto)
        # Círculo principal do produto
        cx, cy = width // 2, height // 2
        raio = 220
        
        # Sombra do produto
        sombra_cores = [
            (cores[2][0], cores[2][1], cores[2][2], 60),
            (cores[3][0], cores[3][1], cores[3][2], 30),
        ]
        
        for i, cor_sombra in enumerate(sombra_cores):
            r = raio + i * 20
            draw.ellipse(
                [cx - r, cy - r, cx + r, cy + r],
                fill=cor_sombra,
                outline=None
            )
        
        # Círculo principal (produto)
        draw.ellipse(
            [cx - raio, cy - raio + 50, cx + raio, cy + raio + 50],
            fill=cores[2],
            outline=(255, 255, 255, 80),
            width=3
        )
        
        # Highlight (brilho)
        highlight_x = cx - raio // 3
        highlight_y = cy - raio // 3 + 50
        draw.ellipse(
            [highlight_x - 60, highlight_y - 60, highlight_x + 60, highlight_y + 60],
            fill=(255, 255, 255, 40)
        )
        
        # Textos
        try:
            # Tentar usar fontes maiores
            fonte_titulo = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 64)
            fonte_detalhes = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 28)
            fonte_pequena = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 24)
        except:
            # Fallback para fonte padrão
            fonte_titulo = ImageFont.load_default()
            fonte_detalhes = ImageFont.load_default()
            fonte_pequena = ImageFont.load_default()
        
        # Sombra de texto
        sombra_offset = 2
        cor_texto = (255, 255, 255)
        cor_sombra_texto = (0, 0, 0, 100)
        
        # Descrição do produto (topo)
        y_desc = 100
        lines = descricao.split('\n')
        for line in lines:
            # Sombra
            draw.text(
                (width // 2 + sombra_offset, y_desc + sombra_offset),
                line,
                fill=cor_sombra_texto,
                font=fonte_titulo,
                anchor="mm"
            )
            # Texto
            draw.text(
                (width // 2, y_desc),
                line,
                fill=cor_texto,
                font=fonte_titulo,
                anchor="mm"
            )
            y_desc += 70
        
        # Detalhes (abaixo do círculo)
        y_detalhe = cy + raio + 100
        # Sombra
        draw.text(
            (width // 2 + sombra_offset, y_detalhe + sombra_offset),
            detalhes,
            fill=cor_sombra_texto,
            font=fonte_detalhes,
            anchor="mm"
        )
        # Texto
        draw.text(
            (width // 2, y_detalhe),
            detalhes,
            fill=cor_texto,
            font=fonte_detalhes,
            anchor="mm"
        )
        
        # Adicionar marca d'água Luniar
        try:
            fonte_marca = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 16)
        except:
            fonte_marca = ImageFont.load_default()
        
        draw.text(
            (width - 150, height - 40),
            "🎂 Luniar Confeitaria",
            fill=(255, 255, 255, 150),
            font=fonte_marca,
            anchor="mm"
        )
        
        # Salvar imagem
        caminho = IMAGES_DIR / f"{nome_arquivo}.png"
        img.save(caminho, 'PNG', quality=95)
        print(f"✅ Imagem criada: {nome_arquivo}.png")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar imagem: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 70)
    print("🎂 Gerador de Imagens - Luniar Confeitaria")
    print("=" * 70)
    print(f"📁 Salvando imagens em: {IMAGES_DIR}\n")
    print("Criando imagens profissionais dos produtos...\n")
    
    sucesso = 0
    falhas = 0
    
    for i, produto in enumerate(PRODUTOS, 1):
        print(f"[{i}/{len(PRODUTOS)}] {produto['titulo']}")
        
        if desenhar_produto(
            produto['nome'],
            produto['titulo'],
            produto['cores'],
            produto['descricao'],
            produto['detalhes']
        ):
            sucesso += 1
        else:
            falhas += 1
        print()
    
    # Resumo
    print("=" * 70)
    print(f"✅ Imagens criadas com sucesso: {sucesso}/{len(PRODUTOS)}")
    if falhas > 0:
        print(f"❌ Falhas: {falhas}/{len(PRODUTOS)}")
    print("=" * 70)
    
    if sucesso == len(PRODUTOS):
        print("\n🎉 Todas as imagens foram criadas com sucesso!")
    
    # Listar arquivos
    print("\n📋 Arquivos criados:")
    for arquivo in sorted(IMAGES_DIR.glob("*.png")):
        tamanho_kb = arquivo.stat().st_size / 1024
        print(f"   ✓ {arquivo.name} ({tamanho_kb:.1f} KB)")

if __name__ == '__main__':
    main()
