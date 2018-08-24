from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
"""
@app.route('/')
def pagina_principal():
    return 'Bienvenido a GetarCine'

if __name__ == '__main__':
    app.run(debug = True)
"""

@app.route('/')
def params():
    #parametro = request.args.get('parametro1','no existe el parametro')
    hola = "Hola Mundo"
    return render_template("index.html", var = hola)
    #return 'el parametro es: {}'.format(parametro)

if __name__ == '__main__':
    app.run(debug = True)

