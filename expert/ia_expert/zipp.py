import zipfile
import os


def zipp(name, decode=None):
    list_cifra = os.listdir('./cifras')
    try:
        for file in list_cifra:
            if str(decode in str(file)):
                with zipfile.ZipFile(f'ia_expert/Minhas_cifras/{name}.zip', 'a', zipfile.ZIP_DEFLATED) as myzip:
                    myzip.write(f'./cifras/{file}')
                    myzip.close()
                    
           
    except Exception as erro:
        print(erro)

if __name__ == '__main__':
    zipp('tom','')
