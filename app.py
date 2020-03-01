from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import config
import os


app = Flask('__name__')
app.config.from_object(config) # recordar colocar config antes de db.
db = SQLAlchemy(app)



@app.route('/', methods=['GET'])
def home():
    from models import Usuarios
    users = Usuarios.query.all()
    return 'hola claudio'
    


# en este condicional damos inicio a la aplicacion
if __name__ == '__main__':
    app.run(debug=True)