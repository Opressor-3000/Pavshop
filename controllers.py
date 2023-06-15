from flask import render_template, request, redirect, flash, url_for, g
from werkzeug.security import generate_password_hash, check_password_hash
from userlogin import UserLogin
from flask_login import login_user, logout_user, login_required, login_manager, current_user

from main import app, db
from forms import *
from models import *
# from admin.admin import auth_bp


@login_manager.user_loader
def load_user(id):
   return User.query.get(int(id))



@app.route('/reg', methods=['GET', 'POST'])  # РЕГИСТРАЦИЯ <<<<<<<<<<<<<<<<<<<<<<<<<<
def registr():
   # if current_user.is_authenticated():
   #    user_id = current_user.get_id()
   #    favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   # else:
   favorite = ''
   categorylist = Category.query.all()
   search = SearchForm()
   # if search is not None:
   #    result = Item.query.filter_by(title=search.word.data).all()
   #    if not result:
   #       return render_template('shop.html', content='no match', search=search)    
   reg = RegistrateForm()
   if reg.validate_on_submit():
      checkemail = User.query.filter_by(email=reg.email.data).first()
      if checkemail is None:
         hash = generate_password_hash(reg.password.data)
         user = User(reg.name.data, reg.surname.data, reg.email.data, hash)
         try:
            user.save()
            flash('Your registration get successful')
            return redirect(url_for('login'))
         except:
            db.session.rollback()
            flash('Error of enters')       
   return render_template('register.html', title='Register', search=search, reg=reg, favr=favorite, catlist=categorylist)


@app.route('/login', methods=['GET', 'POST'])  # LOGIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def login():
   # if current_user.is_authenticated():
   #    user_id = current_user.get_id()
   #    favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   # else:
   favorite = ''
   search = SearchForm()
   categorylist = Category.query.all()
   # if search:
   #    result = Item.query.filter_by(title=search.word.data).all()
   #    if not result:
   #       return render_template('shop.html', content='no match', search=search)    
   login = LoginForm()
   if login.validate_on_submit():
      user =  User.query.filter_by(email=login.email.data).first()
      if user and check_password_hash(user.password, login.password.data): # Проверяем существ такой email и верный ли пароль в БД
         login_user(user)  # сюда надо передать всю информацию по user из БД для авторизации 
         next = request.args.get('next') # дописать функцию которая возвращает на исходную страницу
         return redirect(next)
      else:
         flash('Login or password is not correct')
   else:
      flash('Please fill login and password fields')
   return render_template('login.html', title='Login',  login=login, favr=favorite, catlist=categorylist, search=search)

@app.route('/loguot', methods=['GET', 'POST'])
@login_required
def logout():
   logout_user()
   return redirect(url_for('shop'))


@app.route('/', methods=['GET', 'POST']) # HOME PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def shop():
   # if current_user.is_authenticated():
   #    user_id = current_user.get_id()
   #    favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   # else:
   favorite = ''
   categorylist = Category.query.all()
   search = SearchForm()
   if search:
      result = Item.query.filter_by(title=search.word.data).all()
      if result:
         return render_template('shop.html', content='no match', search=search, favr=favorite, catlist=categorylist, products=result)
   products = Item.query.order(Item.id.desc())
   return render_template('shop.html', title='Product list', products=products, search=search, favr=favorite, catlist=categorylist)
#  item.query.ofset().limit()


@app.route('/<int:id>')
def detail(id):
   # if current_user.is_authenticated():
   #    user_id = current_user.get_id()
   #    favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   # else:
   favorite = ''
   categorylist = Category.query.all()
   search = SearchForm()
   if search:
      result = Item.query.filter_by(title=search.word.data).all()
      if result:
         return render_template('shop.html', content='no match', search=search, favr=favorite, catlist=categorylist, products=result)   
   detailitem = Item.query.filter_by(id).first()
   popular = Item.query.order_by(Item.createdate).limit(5)
   return render_template('detail.html', title='Detail', detail=detailitem, popular=popular, search=search, favr=favorite, catlist=categorylist)


@app.route('/contact', methods=['GET', 'POST'])
@login_required
def contacts():
   # if current_user.is_authenticated():
   #    user_id = current_user.get_id()
   #    favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   # else:
   favorite = ''
   categorylist = Category.query.all()
   search = SearchForm()
   if search:
      result = Item.query.filter_by(title=search.word.data).all()
      if result:
         return render_template('shop.html', content='no match', search=search, favr=favorite, catlist=categorylist, products=result) 
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
   if search:
      result = Item.query.filter_by(title=search.word.data).all()
      if result:
         return render_template('shop.html', content='no match', search=search, favr=favorite, catlist=categorylist, products=result) 
   return render_template('favorites.html', title='Favorites', search=search, favr=favorite, catlist=categorylist, favorite=favorites)

@login_manager.unauthorized_handler
def unauthorized():
   return redirect(url_for('login'))


@app.errorhandler(404)
def pnf(error):
   if current_user.is_authenticated():
      user_id = current_user.get_id()
      favorite = Favorite.query.filter_by(user=user_id).count() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   item.query(user_id=id).count()
   categorylist = Category.query.all()
   search = SearchForm()
   if search:
      result = Item.query.filter_by(title=search.word.data).all()
   return render_template('page404.html', title='PageNotFound', search=search, favorite=favorite, catlist=categorylist),404

