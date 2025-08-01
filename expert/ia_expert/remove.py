import os
import shutil

def remover_arquivos_da_pasta(pasta, decode):
    """
    Remove todos os arquivos de uma pasta especificada.

    Args:
        pasta (str): O caminho da pasta.
    """
   
    try:
        for filename in os.listdir(pasta):
            filepath = os.path.join(pasta, f'{decode}{filename}')
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)  # Remove diretórios recursivamente
            except Exception as e:
                print(f"Erro ao remover {filepath}: {e}")
    except FileNotFoundError:
        print(f"Pasta não encontrada: {pasta}")
    except OSError as e:
        print(f"Erro de sistema ao acessar a pasta: {e}")
