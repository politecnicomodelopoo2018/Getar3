from flask import Flask
from flask import render_template
from Clases.cliente import Cliente
app = Flask(__name__)

@app.route('/user/<name>')
def user(name = 'Eduardo'):
   c = Cliente()

   return render_template('user.html', nombre = name, client = c)

if __name__ == '__main__':
   app.run(debug = True)