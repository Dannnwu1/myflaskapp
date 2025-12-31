# app.py
from flask import Flask, render_template
from flask_cors import CORS
import config
from blueprints.api.routes import api_bp
from blueprints.photo.models import db, import_csv_with_pandas
from blueprints.views.routes import views_bp
from blueprints.photo.routes import photo_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config.Config)

    # Register blueprints

    app.register_blueprint(views_bp, url_prefix='/')
    app.register_blueprint(photo_bp, url_prefix='/photo')
    app.register_blueprint(api_bp, url_prefix='/api')
    db.init_app(app)

    # with app.app_context():
    #     import_csv_with_pandas()
    #     print("table created")

    # Root route
    @app.route('/')
    def index():
        return render_template('index.html')

    return app


app = create_app()

if __name__ == '__main__':
    # app = create_app()
    app.run(debug=False)
