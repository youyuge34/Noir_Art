
import os
from flask import render_template, Blueprint, request, current_app, abort, make_response
from flask_login import login_required, current_user
from noirart.extensions import db
from noirart.models import Photo
from noirart.utils import rename_image, resize_image, redirect_back

from noirart.decorators import permission_required

# create main page blueprint
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('main/index.html')


@main_bp.route('/explore')
def explore():
    return render_template('main/explore.html')


@main_bp.route('/upload', methods=['GET', 'POST'])
@login_required
@permission_required('UPLOAD')
def upload():
    if request.method == 'POST' and 'file' in request.files:
        f = request.files.get('file')  # 返回FileStorage对象
        filename = rename_image(f.filename)
        f.save(os.path.join(current_app.config['NOIR_UPLOAD_PATH'], filename))
        filename_s = resize_image(f, filename, current_app.config['NOIR_PHOTO_SIZE']['small'])
        filename_m = resize_image(f, filename, current_app.config['NOIR_PHOTO_SIZE']['medium'])
        photo = Photo(
            filename=filename,
            filename_s=filename_s,
            filename_m=filename_m,
            author=current_user._get_current_object()
        )
        db.session.add(photo)
        db.session.commit()
    return render_template('main/upload.html')


@main_bp.route('/change-theme/<theme_name>')
def change_theme(theme_name):
    if theme_name not in current_app.config['NOIR_THEMES'].keys():
        abort(404)

    response = make_response(redirect_back())
    response.set_cookie('theme', theme_name, max_age=30 * 24 * 60 * 60)
    return response

