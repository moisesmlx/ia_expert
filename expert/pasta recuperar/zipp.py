import zipfile
from tkinter import messagebox

def zipp(name,file):
    try:
        with zipfile.ZipFile(f'minhas_cifras/{name}.zip', 'a', zipfile.ZIP_DEFLATED) as myzip:
            myzip.write(file)
            myzip.close()
    except Exception as erro:
        messagebox.showerror(message=f'Ouve um error cheque as informações\n{erro}')



