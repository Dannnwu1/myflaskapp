# app.py
from flask import Flask, render_template
from blueprints.auth.routes import auth_bp
from blueprints.blog.routes import blog_bp
from blueprints.admin.routes import admin_bp
from blueprints.views.routes import views_bp
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    # Register blueprints
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    # app.register_blueprint(blog_bp, url_prefix='/admin')
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(views_bp, url_prefix='/views')

    # Root route
    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
