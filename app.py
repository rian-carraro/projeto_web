from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/bootstrap')
def ver_algo():
    return render_template('bootstrap.html')

@app.route('/sobre/fatec')
def sobre_fatec():
    return '''
<h1>Pagina da Fatec</h1>
<p>Desenvolvida na <b>Fatec</b></p>
'''

@app.route('/cor/<cor1>')
def exibe_cor(cor1):
    return f'<h1 style="color:{cor1}">A cor escolhida foi: {cor1}</h1>'


@app.route('/cor/<cor1>/<cor2>')
def exibe_cor2(cor1,cor2):
    return f'<h1 style="color:{cor1}">A cor 1 foi: {cor1} e <b style="color:{cor2}">{cor2}</b></h1> '

@app.route('/codigos/<int:ano_nascimento>')
def exibe_codigos(ano_nascimento):
    
    dados = {
        'nome': "rian",
        'ano_nascimento': ano_nascimento,
        'idade': (2026 - ano_nascimento),
        'texto' : "Vamos escrever um texto bem longo para que o truncante funcione!",
        'ativo' : 'erro',
        'pessoas': ['João', 'Maria', 'José']
    }
    return render_template('codigos.html', **dados)

if __name__ == '__main__':
    app.run(debug=True)