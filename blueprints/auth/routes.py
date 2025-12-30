# blueprints/auth/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import LoginForm, RegisterForm

# Create blueprint
auth_bp = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/auth'
)

# Routes
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successful!', 'success')
        return redirect(url_for('blog.index'))
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Registration successful!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth_bp.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))