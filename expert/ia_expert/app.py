
from flask import Flask, render_template, request
import os
from time import sleep
from tkinter import *
import Expert_em_Cifras
from pathlib import Path
os.system('del /s /q static\minhas_cifras')
app = Flask(__name__)
DIRETORIO = r"\output"
fpath = Path('mus.txt').absolute()

@app.route('/',  methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home_page():
    filename = ''
    confirme = ''


    def post_arquivo():
        arquivo = request.files.get("meuArquivo")
        nome_do_arquivo = arquivo.filename
        arquivo.save(os.path.join(DIRETORIO, nome_do_arquivo))


        post_arquivo()
    if request.method == 'POST':
        confirme = 'Sua cifra está pronta click aqui para baixar'
        req = request.form

        original = req['original']
        nova = req['new']
        nome = nova
        text_area = req['text_area']

        Expert_em_Cifras.translate(original, nova, nome, text_area)
        sleep(0.5)
        try:           
            filename = Expert_em_Cifras.t(nome, nova)                  
        except:
            filename = 'Cifra não encontrada'

    return render_template('index.html', filename = filename, conferir = confirme)


def name_cifra():
        with open('name.txt', 'r', encoding='utf-8') as cifra:
            cif = cifra.read()
        return cif

   
@app.route('/cifra', methods=['GET', 'POST'])
def archivo(): 
    return f'''
    <html>
<head>
	<title>Expert em cifras</title>
</head>

<body bgcolor="turquoise">
    <a name="arq" href="/index"><h3>Pagina inicial</h3></a><br>
    <Center>
        <img src="/static/logo.png"/>
        <h4>Troque de escala Musical a hora que quiser; <br>
        </h4>
        Sua cifra está pronta click em baixar e um arquivo .txt sera enviado para voçê <br>
        <br> 
		<a name="arq" href=static\minhas_cifras\{name_cifra()} download="Nova Cifra"><h3>Baixar</h3></a><br>
        <br>

    </Center>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

