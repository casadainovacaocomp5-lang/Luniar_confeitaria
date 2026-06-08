#!/usr/bin/env python3
"""
Script para gerar imagens de produtos da Luniar Confeitaria
Usa Unsplash API - Serviço gratuito de fotos stock de alta qualidade
"""

import os
import requests
from pathlib import Path
import time

# Diretório de saída
IMAGES_DIR = Path(__file__).parent.parent / 'assets' / 'images'
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# Produtos com queries otimizadas para Unsplash
PRODUTOS = [
    {
        'nome': 'brownie',
        'titulo': 'Brownie',
        'query': 'chocolate brownie professional food photography'
    },
    {
        'nome': 'torta_cookie_ninho_nutela',
        'titulo': 'Torta Cookie de Ninho com Nutela',
        'query': 'chocolate cake with hazelnut spread professional food photography'
    },
    {
        'nome': 'torta_cookie',
        'titulo': 'Torta Cookie',
        'query': 'cookie cake chocolate chips professional food photography'
    },
    {
        'nome': 'torta_cookie_brigadeiro',
        'titulo': 'Torta Cookie de Brigadeiro',
        'query': 'chocolate cake with chocolate filling professional food photography'
    },
    {
        'nome': 'torta_cookie_doce_leite',
        'titulo': 'Torta Cookie de Doce de Leite',
        'query': 'caramel cake dulce de leche professional food photography'
    },
    {
        'nome': 'palha_italiana',
        'titulo': 'Palha Italiana',
        'query': 'crispy candy strands Brazilian sweet professional food photography'
    },
    {
        'nome': 'sanduiche_natural',
        'titulo': 'Sanduíche Natural',
        'query': 'healthy sandwich fresh vegetables professional food photography'
    },
]

def baixar_imagem_unsplash(nome_arquivo, query):
    """
    Baixa uma imagem do Unsplash usando a query
    Unsplash permite downloads sem autenticação
    """
    try:
        print(f"🎨 Baixando imagem para: {nome_arquivo}...")
        
        # URL da API Unsplash (free, sem API key necessária)
        # Usando source=unsplash para pegar fotos de alta qualidade
        url = f"https://source.unsplash.com/1200x800/?{query.replace(' ', '+')}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        
        if response.status_code == 200 and response.content:
            caminho = IMAGES_DIR / f"{nome_arquivo}.jpg"
            with open(caminho, 'wb') as f:
                f.write(response.content)
            print(f"✅ Imagem salva: {nome_arquivo}.jpg")
            return True
        else:
            print(f"⚠️  Erro ao baixar (Status: {response.status_code})")
            return False
            
    except requests.exceptions.Timeout:
        print(f"⏱️  Timeout na conexão")
        return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def criar_imagem_local(nome_arquivo):
    """
    Cria uma imagem placeholder usando Pillow como fallback
    """
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # Criar imagem colorida com texto
        img = Image.new('RGB', (1200, 800), color=(255, 200, 100))
        draw = ImageDraw.Draw(img)
        
        # Adicionar texto
        texto = f"Imagem do produto\n{nome_arquivo.replace('_', ' ').title()}"
        
        try:
            # Tentar usar fonte padrão
            draw.text((600, 400), texto, fill=(139, 69, 19), anchor="mm")
        except:
            # Fallback para fonte padrão do sistema
            pass
        
        caminho = IMAGES_DIR / f"{nome_arquivo}_placeholder.jpg"
        img.save(caminho)
        print(f"📋 Placeholder criado: {nome_arquivo}_placeholder.jpg")
        return True
        
    except ImportError:
        print("⚠️  Pillow não instalado para criar placeholders")
        return False
    except Exception as e:
        print(f"❌ Erro ao criar placeholder: {e}")
        return False

def main():
    """
    Função principal - baixa todas as imagens
    """
    print("=" * 70)
    print("🎂 Gerador de Imagens - Luniar Confeitaria")
    print("=" * 70)
    print(f"📁 Salvando imagens em: {IMAGES_DIR}\n")
    print("Fonte: Unsplash (fotos stock gratuitas de alta qualidade)\n")
    
    sucesso = 0
    falhas = 0
    
    for i, produto in enumerate(PRODUTOS, 1):
        print(f"[{i}/{len(PRODUTOS)}] {produto['titulo']}")
        
        if baixar_imagem_unsplash(produto['nome'], produto['query']):
            sucesso += 1
        else:
            print(f"    Tentando criar placeholder...")
            if criar_imagem_local(produto['nome']):
                sucesso += 1
            else:
                falhas += 1
        
        # Pequeno delay entre requisições para respeitar a API
        if i < len(PRODUTOS):
            time.sleep(1)
        print()
    
    # Resumo
    print("=" * 70)
    print(f"✅ Imagens obtidas com sucesso: {sucesso}/{len(PRODUTOS)}")
    if falhas > 0:
        print(f"❌ Falhas: {falhas}/{len(PRODUTOS)}")
    print("=" * 70)
    
    if sucesso == len(PRODUTOS):
        print("\n🎉 Todas as imagens foram obtidas com sucesso!")
        print("📍 As imagens estão prontas em: assets/images/")
    else:
        print(f"\n⚠️  Algumas imagens falharam. Verifique a conexão.")
    
    # Listar arquivos criados
    print("\n📋 Arquivos criados:")
    for arquivo in sorted(IMAGES_DIR.glob("*")):
        print(f"   - {arquivo.name}")

if __name__ == '__main__':
    main()
