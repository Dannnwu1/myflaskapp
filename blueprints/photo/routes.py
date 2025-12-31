from flask import Blueprint, render_template

photo_bp = Blueprint(
    'photo',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@photo_bp.route('/gallery')
def gallery():
    return render_template('gallery.html')

