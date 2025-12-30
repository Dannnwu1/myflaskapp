# blueprints/blog/routes.py
from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Post, db  # Example model

blog_bp = Blueprint(
    'blog',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Dummy data for example
posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is the first blog post.'},
    {'id': 2, 'title': 'Second Post', 'content': 'This is the second blog post.'}
]


@blog_bp.route('/')
def index():
    return render_template('blog/index.html', posts=posts)


@blog_bp.route('/post/<int:post_id>')
def show_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        flash('Post not found!', 'error')
        return redirect(url_for('blog.index'))
    return render_template('blog/post.html', post=post)


@blog_bp.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        new_post = {'id': len(posts) + 1, 'title': title, 'content': content}
        posts.append(new_post)
        flash('Post created successfully!', 'success')
        new_post = Post(id=len(posts) + 1, title=title, content=content, created_at=datetime.now())
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.index'))
    return render_template('blog/create.html')
