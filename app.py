# app.py
from flask import Flask, render_template

from blueprints.user.routes import user_bp
from blueprints.blog.models import db, import_csv_with_pandas
from blueprints.views.routes import views_bp
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    # Register blueprints
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    # app.register_blueprint(blog_bp, url_prefix='/blog')
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(views_bp, url_prefix='/')
    app.register_blueprint(user_bp, url_prefix='/user')
    db.init_app(app)

    with app.app_context():
        import_csv_with_pandas()
        print("table created")

    # Root route
    @app.route('/')
    def index():
        return render_template('index.html')

    return app


app = create_app()

if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)
