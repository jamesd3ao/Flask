from flask import Flask 

app = Flask(__name__)#Nuevo objeto de flask.

@app.route('/')#wrap o decorador (rutas autorizadas).
def index(): #Función que retonar un string.
	return 'Hola mundo'

app.run()#Se encarga de ejecutar el servidor de python.