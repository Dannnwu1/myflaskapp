from flask import Blueprint, render_template, request, flash, redirect, url_for
from blueprints.blog.models import User,db

user_bp = Blueprint(
    'user',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@user_bp.route('/')
def users():
    users = User.query.all()
    print(users)
    return render_template('users.html', users=users)
