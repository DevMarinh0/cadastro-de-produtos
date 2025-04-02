#!/usr/bin/env python
import os
import sys

def main():
    """Ponto de entrada principal do Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar Django. "
            "Tem certeza de que ele está instalado e acessível no seu ambiente?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
