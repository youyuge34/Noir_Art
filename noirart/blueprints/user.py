from flask import render_template, Blueprint, request, current_app

from noirart.models import User, Photo

user_bp = Blueprint('user', __name__)


@user_bp.route('/<username>')
def index(username):
    # 这就是之前给username做index的原因
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['NOIR_PHOTO_PER_PAGE']
    pagination = Photo.query.with_parent(user).order_by(Photo.timestamp.desc()).paginate(page, per_page)
    photos = pagination.items
    return render_template('user/index.html', user=user, pagination=pagination, photos=photos)
