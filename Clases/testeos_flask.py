from flask import *
from cliente import Cliente

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'Bienvenido %s' % name

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/esto',methods = ['POST', 'GET'])
def esto():
   if request.method == 'POST':
      user = request.form['nm']
      usera = request.form['nm2']
      c = Cliente()
      c.dni ='NULL'
      c.nombre = user
      c.nombre  = usera
      c.Dar_de_Alta_Cliente()
      return redirect(url_for('success',name = user,surname = usera,dni = 'NULL'))
   else:
      user = request.args.get('nm')
      usera = request.args.get('nm2')
      return redirect(url_for('success',name = user,surname = usera,dni = 'NULL'))



if __name__ == '__main__':
   app.run(debug = True)