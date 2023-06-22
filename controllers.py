from flask import render_template, request, redirect, flash, url_for, g
from werkzeug.security import generate_password_hash, check_password_hash
from userlogin import UserLogin
from flask_login import login_user, logout_user, login_required, login_manager, current_user
from sqlalchemy import func

from main import app, db
from forms import *
from models import *



@login_manager.user_loader
def load_user(id):
   return User.query.get(id)


@app.route('/reg', methods=['GET', 'POST'])  # РЕГИСТРАЦИЯ <<<<<<<<<<<<<<<<<<<<<<<<<<
def registr():
   reg = RegistrateForm()
   if current_user.is_authenticated:
       return redirect(url_for('shop'))
   categorylist = Category.query.all()
   favorite = ''
   search = SearchForm()  
   if request.method == "POST":
      if reg.validate_on_submit():
         checkemail = User.query.filter_by(email=reg.e_mail.data).first()
         if checkemail is None:
            hash = generate_password_hash(reg.password.data)
            user = User(reg.name.data, reg.surname.data, reg.e_mail.data, hash)
            try:
               user.save()
               flash('Your registration get successful')
               return redirect(url_for('login'))
            except:
               db.session.rollback()
               flash('Error of enters')
         else:
            return render_template('register.html', title='email error', search=search, reg=reg, catlist=categorylist, favr=favorite)
            # flash('this email is already registered')
   return render_template('register.html', title='Register', search=search, reg=reg, catlist=categorylist, favr=favorite)


@app.route('/login', methods=['GET', 'POST'])  # LOGIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def login():
   if current_user.is_authenticated:
      user_id = current_user.get_id()
      favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   else:
      favorite = ''
   login = LoginForm()
   search = SearchForm()
   categorylist = Category.query.all()
   if login.validate_on_submit():
      user =  User.query.filter_by(email=login.email.data).first()
      if user and check_password_hash(user.password, login.password.data): # Проверяем существ такой email и верный ли пароль в БД
         login_user(user)  # сюда надо передать всю информацию по user из БД для авторизации 
         return redirect(url_for('shop'))
      else:
         flash('Login or password is not correct')
   else:
      flash('Please fill login and password fields')
   return render_template('login.html', title='Login',  login=login, favr=favorite, catlist=categorylist, search=search)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
   logout_user()
   return redirect(url_for('shop'))


@app.route('/', methods=['GET', 'POST']) # HOME PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def shop():
   print(request.method)
   search = SearchForm()
   print(search.word.data)
   if current_user.is_authenticated:
      user_id = current_user.get_id()
      favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   else:
      favorite = ''
   categorylist = Category.query.all()
   products = Item.query.all()
   return render_template('shop.html', title='Product list', products=products, search=search, favr=favorite, catlist=categorylist)
#  item.query.ofset().limit()


@app.route('/<int:id>')
def detail(id):
   detailitem = Item.query.filter_by(id=id).first()
   categorylist = Category.query.all()
   search = SearchForm()
   reform = ReviewForm()
   images = Image.query.filter_by(item_id=id).all()
   revcount = Review.query.filter_by(item_id=id).count()
   review = Review.query.filter_by(item_id=id).all()
   popular = Item.query.order_by(Item.createdate).limit(5)
   if current_user.is_authenticated:
      user_id = current_user.get_id()
      favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   else:
      favorite = ''
   return render_template('detail.html', title='Detail', detail=detailitem, username='name', reform=reform, revcount=revcount, images=images, popular=popular, search=search, favr=favorite, catlist=categorylist, review=review)


@app.route('/contact', methods=['GET', 'POST'])
@login_required
def contacts():
   if current_user.is_authenticated():
      user_id = current_user.get_id()
      favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   else: 
      return redirect(url_for('login'))
   categorylist = Category.query.all()
   search = SearchForm()
   conform = ContactForm()
   if conform.validate_on_submit():
      contact = Contact(conform.name.data, conform.email.data, conform.subject.data, conform.subject.data)
      try:
         contact.save()
         flash('Send successful')
      except:
         db.sesssion.rollback()
         flash('Send error')
      return redirect(url_for('shop'))
   return render_template('contact.html', title='Contact', search=search, conform=conform, favr=favorite, catlist=categorylist)


@app.route('/favorites')
@login_required
def favorites():
   if current_user.is_authenticated():
      user_id = current_user.get_id()
      favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
      favorites = Favorite.query.filter_by(user=user_id).all()
   else:
      favorite = ''
   categorylist = Category.query.all()
   search = SearchForm()
   return render_template('favorites.html', title='Favorites', search=search, favr=favorite, catlist=categorylist, favorite=favorites)

@login_manager.unauthorized_handler
def unauthorized():
   return redirect(url_for('login'))


@app.errorhandler(404)
def pnf(error):
   favorite = ''
   if current_user.is_authenticated:
      user_id = current_user.get_id()
      favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   categorylist = Category.query.all()
   search = SearchForm()
   return render_template('page404.html', title='PageNotFound', search=search, favorite=favorite, catlist=categorylist),404


@app.route('/adm', methods=['GET', 'POST'])
def admin():
   if current_user:
      user_id = current_user.get_id()
      favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   categorylist = Category.query.all()
   search = SearchForm()
   itemform = ItemForm()
   return render_template('adddate.html', title='Contact', search=search, favr=favorite, catlist=categorylist, itemform=itemform)

@app.route('/<int:categoryid>')
def filter(categoryid):
   products = Item.query.filter_by(category_id=categoryid).all()
   categorylist = Category.query.all()
   search = SearchForm()
   if current_user:
      user_id = current_user.get_id()
      favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   return render_template('shop.html', title='Product list', products=products, search=search, favr=favorite, catlist=categorylist)

@app.route('/', methods=['GET', 'POST'])
def search():
   args = request.args
   if args.get('Search'):
      products=Item.query.filter(Item.name.contains(args.get('Search'))).all()
   else :
      products = Item.query.all()