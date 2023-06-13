from flask import render_template, request, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from userlogin import UserLogin
from flask_login import login_user, logout_user

from main import app, db
from forms import *
from models import *
from admin.admin import auth_bp


@app.route('/registr', methods=['GET', 'POST'])  # РЕГИСТРАЦИЯ <<<<<<<<<<<<<<<<<<<<<<<<<<
def registr():
   reg = RegistrateForm()
   if reg.validate_on_submit() and request.method == 'POST':
      checkemail = User.query.filter_by(email=reg.email.data).first()
      if checkemail in None and reg.password.data == reg.passconf.data:
         user = User(name=reg.name.data, surname=reg.surname.data, email=reg.email.data, password=reg.password.data)
         try:
            db.session.add(user)
            db.session.commit()
            flash('Your registration get successful')
         except:
            db.session.rollback()
            flash('Error of enters')
            return         
         return render_template('login.html', title='Login page')
      return render_template('registr.html', title='Register', error='error')
   return render_template('registr.html', title='Register')


@app.route('/login', methods=['GET', 'POST'])  # LOGIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def login():
   login = LoginForm()
   if login.validate_on_submit() and request.method == 'POST':
      user =  get_user(login.email.data)  
      if user and check_password_hash(login.password.data, user.password): # Проверяем существ такой email и верный ли пароль в БД
         login_user(user)  # сюда надо передать всю информацию по user из БД для авторизации 
         next = request.args.get('next')
         return redirect(next)
      else:
         flash('Login or password is not correct')
   else:
      flash('Please fill login and password fields')
   return render_template('login.html', title='Login')

@app.route('/', methods=['GET', 'POST']) # HOME PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def shop():
   search = SearchForm()
   if search.word.data is not None:
      result = Item.query.filter_by(title=search.word.data).all()
      if not result:
         return render_template('shop.html', content='no match')      
      products = Item.query.order(Item.id.desc())
   return render_template('shop.html', title='Product list')

@app.route('/<int:id>')
def detail(id):
   detailitem = Item.query.filter_by(id).first()
   popular = Item.query.order_by(Item.createdate).limit(5)
   return render_template('detail.html', title='Detail', detail=detailitem, popular=popular)

@app.route('/contact', methods=['GET', 'POST'])
def contacts():
   conform = ContactForm()
   if request.method == 'POST' and conform.validate_on_submit():
      contact = Contact(name=conform.name.data, email=conform.email.data, subject=conform.subject.data, message=conform.subject.data)
      try:
         db.session.add(contact)
         db.session.commit()
         flash('Mail successfully sent')
      except:
         db.sesssion.rollback()
         flash('Send error')
      return redirect(url_for('shop'))
   return render_template('contact.html', title='Contact')

@app.route('/favorites')
def favorites(user_id):
   favorite = Favorite.query.filter_by(user_id).all()
   return render_template('favorites.html', title='Favorites', favorite=favorite)