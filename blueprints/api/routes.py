from flask import Blueprint, jsonify, render_template, url_for
from blueprints.photo.models import Photo

api_bp = Blueprint(
    'api',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@api_bp.route('/')
def apis():
    photos = Photo.query.all()
    photos_list = [
        {
            'id': photo.id,
            'file_name': photo.filename,
            'description': photo.description,
            'created_at': photo.created_at,
            'name': photo.name,
            'url': url_for('static', filename=f'/assets/photos/2025/12 Dec/{photo.filename}'),
        }
        for photo in photos
    ]

    return jsonify(photos_list)



