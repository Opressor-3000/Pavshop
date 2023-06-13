from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from alldata import categorydata, itemdata

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AAA267y~AC3NzaC1lZDI1NTE5AAAAIDvivHAMjgkRGFSeU/KuvuUPEeMRDijpWMoYVqCOhF3I'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:v01234567@localhost:3356/project'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False



db =SQLAlchemy(app)

login_manager = LoginManager(app)

from controllers import *

app.register_blueprint(auth_bp, url_prefix='/admin')

migrate = Migrate(app, db)
n = None
d = '''Volup erat ipsum diam elitr rebum et dolor. Est nonumy elitr erat
             diam stet sit clita ea. Sanc invidunt ipsum et, labore clita lorem
             magna lorem ut. Erat lorem duo dolor no sea nonumy. Accus labore
             stet, est lorem sit diam sea et justo, amet at lorem et eirmod ipsum
             diam et rebum kasd rebum.

            <p>
                Eos no lorem eirmod diam diam, eos elitr et gubergren diam sea.
                Consetetur vero aliquyam invidunt duo dolores et duo sit. Vero
                diam ea vero et dolore rebum, dolor rebum eirmod consetetur
                invidunt sed sed et, lorem duo et eos elitr, sadipscing kasd
                ipsum rebum diam. Dolore diam stet rebum sed tempor kasd eirmod.
                Takimata kasd ipsum accusam sadipscing, eos dolores sit no ut
                diam consetetur duo justo est, sit sanctus diam tempor aliquyam
                eirmod nonumy rebum dolor accusam, ipsum kasd eos consetetur at
                sit rebum, diam kasd invidunt tempor lorem, ipsum lorem elitr
                sanctus eirmod takimata dolor ea invidunt.
            </p>
            <p>
                Dolore magna est eirmod sanctus dolor, amet diam et eirmod et
                ipsum. Amet dolore tempor consetetur sed lorem dolor sit lorem
                tempor. Gubergren amet amet labore sadipscing clita clita diam
                clita. Sea amet et sed ipsum lorem elitr et, amet et labore
                voluptua sit rebum. Ea erat sed et diam takimata sed justo.
                Magna takimata justo et amet magna et.
            </p>'''
catdata = ['Shirts', 'Jeans', 'Swimwear', 'Sleepwear', 'Sportswear', 'Jumpsuits', 'Blazers', 'Jackets', 'Shoes']
itemdat = ['Colorful Stylish Shirt', '150.00', '200.00', f"../static/img/pr-' + {n} + '.webp", n, n, d]
categorydata(catdata)
itemdata(itemdat)

if __name__ == '__main__':
    app.run(debug=True)



