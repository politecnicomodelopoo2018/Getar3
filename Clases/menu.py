from flask import Flask
from flask import render_template
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('menu.html')

@app.route('/pelis')
def peliculas():
   return render_template('pelis.html')

@app.route('/success/<name>')
def success(name):
    return render_template('pelis.html', nombre= name)


@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['nombre']
        return redirect('/success/' + usuario)
    else:
       return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)