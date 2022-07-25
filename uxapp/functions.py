from functools import wraps
from flask_login import current_user
from flask import request, redirect, flash, url_for


#================================
# Admin Access Required Function
#================================
EXEMPT_METHODS = set(['OPTIONS'])
def admin_role_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_user.role != 1:
            flash('Access Denied, Admins only can view this page!', 'alert-danger')
            return redirect(url_for('main.dashboard'))
        return func(*args, **kwargs)
    return decorated_view

################################
# Role Required Function 
################################

def required_roles(*roles):
   def wrapper(f):
      @wraps(f)
      def wrapped(*args, **kwargs):
         check_roles = any(item in get_current_user_role() for item in roles)
         if not check_roles:
            flash('Access Denied: Sorry, you don\'t have access to view this page','alert-danger')
            return redirect(url_for('main.dashboard'))
         return f(*args, **kwargs)
      return wrapped
   return wrapper

def get_current_user_role():
   return current_user.access_list.split(",")

