from datetime import datetime

from main import db, login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255))
    createdate = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, surname, email, password, is_active=True, is_superuser=False):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_superuser = is_superuser

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
       return self.id
    
# @login_manager.user_loader
# def get_user(user_id):
#     return User.query.get(user_id)
    

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(32), nullable=False, unique=True)

    def __init__(self, category_name):
        self.category_name = category_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.category_name
    

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    oldprice = db.Column(db.Float, default=None)
    image = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    description = db.Column(db.Text)
    createdate = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, price, oldprice, image, quantity, category_id, description):
        self.title = title
        self.price = price
        self.oldprice = oldprice
        self.image = image
        self.quantity = quantity
        self.category_id = category_id
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.item
    

class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def __init__(self, item_id, url):
        self.item_id = item_id
        self.url = url

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.url
    

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

    def __init__(self, user, item):
        self.user = user
        self.item = item

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.id


class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(100), unique=True, nullable=False)
    message = db.Column(db.String(255), nullable=False, unique=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, subject, message):
        self.user_id = user_id
        self.subject = subject
        self.message = message

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.id


class Review(db.Model):
    __tablername__ = 'review'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    review = db.Column(db.String(255), nullable=False)
    published_at = db.Column(db.Boolean, default=True)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)



    def __init__(self, user_id, item_id, review):
        self.user_id = user_id
        self.item_id = item_id
        self.review = review

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.id


def categorydata(data):
    for c in data:
        cat = Category(c)
        cat.save()


def ncount(n, d):
    itemdat = ('Colorful Stylish Shirt', 150.00, 200.00, f"../static/img/pr-{n}.webp", n, n, d)
    return itemdat


def itemdata(discript):
   for i in range(1, 9):
        icoun = ncount(i, discript)
        print(icoun)
        itmd = Item(icoun)
        itmd.save()
        

d =  '''<p>
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


def datarecord():
    # item1 = Item('Colorful Stylish Shirt', )
    # categorydata(catdata)
    itemdata(d)

# datarecord()


   




