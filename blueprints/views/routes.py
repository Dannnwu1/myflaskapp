# blueprints/blog/routes.py
from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for, session

views_bp = Blueprint(
    'views',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@views_bp.route('/projects')
def projects():
    return render_template('projects.html')


@views_bp.route('/resume')
def resume():
    return render_template('resume.html')


@views_bp.route('/contact')
def contact():
    return render_template('contact.html')


@views_bp.route("/privacy")
def privacy():
    context = {
        'site_name': 'Dan\'s App',
        'company_name': 'Dan one person limited company',
        'contact_email': 'privacy@yourapp.com',
        'company_address': '123 Tech Street, San Francisco, CA 94107',
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'current_year': datetime.now().year,
    }
    return render_template('privacy.html', **context)


@views_bp.route('/terms')
def terms():
    context = {
        'site_name': 'Dan\'s App',
        'company_name': 'Dan one person limited company',
        'contact_email': 'privacy@yourapp.com',
        'company_address': '123 Tech Street, San Francisco, CA 94107',
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'current_year': datetime.now().year,
    }
    return render_template('terms.html', **context)


@views_bp.route('/technical')
def technical():
    if 'password' in session:
        if session['password'] == '123456':
            return render_template('technical.html')
    return redirect(url_for('views.password'))


@views_bp.route('/password', methods=["POST", 'GET'])
def password():
    if request.method == "POST":
        password = request.form.get('password')
        print(password)
        session['password'] = password
        return redirect(url_for('views.technical'))
    return render_template('password.html')
