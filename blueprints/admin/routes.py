# blueprints/admin/routes.py
from functools import wraps

from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Admin only decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/users')
@login_required
@admin_required
def manage_users():
    return "User management page"

@admin_bp.route('/settings')
@login_required
@admin_required
def settings():
    return "Admin settings"