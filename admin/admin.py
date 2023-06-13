from flask import Blueprint, render_template


auth_bp = Blueprint(
   'auth_bp', __name__,
   template_folder = 'templates',
   static_folder = 'static'
)


@auth_bp.route('/')
def adminpanel():
   return render_template('panel.html', title='Admin Panel')