"""
Script para rodar a aplicação Flask
Executar: python run.py
"""

import os
from app import create_app, db

# Cria a aplicação
app = create_app(os.environ.get('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Contexto para flask shell"""
    return {'db': db}

if __name__ == '__main__':
    # Development
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
