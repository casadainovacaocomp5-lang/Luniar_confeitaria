"""
Script para gerenciar o banco de dados

Uso:
    python manage.py init-db          # Inicializar banco
    python manage.py create-admin     # Criar admin
    python manage.py reset-db         # Resetar banco (CUIDADO!)
"""

import os
import sys
from app import create_app, db

app = create_app()

def init_db():
    """Cria as tabelas no banco"""
    with app.app_context():
        db.create_all()
        print('✅ Banco de dados inicializado com sucesso!')

def reset_db():
    """Reseta o banco de dados (remove tudo)"""
    response = input('⚠️  Isso vai deletar TUDO! Tem certeza? (sim/nao): ')
    if response.lower() == 'sim':
        with app.app_context():
            db.drop_all()
            db.create_all()
            print('✅ Banco resetado!')
    else:
        print('❌ Cancelado')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python manage.py [init-db|reset-db|create-admin]')
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'init-db':
        init_db()
    elif command == 'reset-db':
        reset_db()
    else:
        print(f'Comando desconhecido: {command}')
