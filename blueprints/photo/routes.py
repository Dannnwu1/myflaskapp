from flask import Blueprint, jsonify
from blueprints.photo.models import Photo

photo_bp = Blueprint(
    'photo',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@photo_bp.route('/')
def photos():
    photos = Photo.query.all()
    photos_list = [
        {
            'id': photo.id,
            'file_name': photo.filename,
            'description': photo.description,
            'created_at': photo.created_at,
            'name': photo.name,
        }
        for photo in photos
    ]

    return jsonify(photos_list)
