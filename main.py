from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'AAA267y~AC3NzaC1lZDI1NTE5AAAAIDvivHAMjgkRGFSeU/KuvuUPEeMRDijpWMoYVqCOhF3I'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:v01234567@localhost:3356/project'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False


db =SQLAlchemy(app)

login_manager = LoginManager(app)

from controllers import *

# app.register_blueprint(auth_bp, url_prefix='/admin')

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)



