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
    
@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)
    

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(32), nullable=False, unique=True)

    def __init__(self, category):
        self.category = category

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.category
    

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    oldprice = db.Column(db.Float, default=None)
    img = db.Column(db.String(255))
    quantity = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    description = db.Column(db.Text)
    createdate = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, price, oldprice, quantity, category_id, description):
        self.title = title
        self.price = price
        self.oldprice = oldprice
        self.quantity = quantity
        self.category_id = category_id
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.item
    

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
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    subject = db.Column(db.String(100), unique=True, nullable=False)
    message = db.Column(db.String(255), nullable=False, unique=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
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


# class admin(db.Model):
#     __teblename__ = 'admin'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __init__(self, user_id):
#         self.user_id = user_id
    
#     def __repr__(self):
#         return self.user_id

    




