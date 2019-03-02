from flask import render_template, Blueprint, jsonify, current_app
from flask_login import current_user

from noirart.notifications import push_follow_notification, push_collect_notification
from noirart.models import User, Notification, Photo

ajax_bp = Blueprint('ajax', __name__)


@ajax_bp.route('/profile/<int:user_id>')
def get_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('main/profile_popup.html', user=user)


@ajax_bp.route('/notifications-count')
def notifications_count():
    if not current_user.is_authenticated:
        return jsonify(message='Login required.'), 403

    count = Notification.query.with_parent(current_user).filter_by(is_read=False).count()
    return jsonify(count=count)


@ajax_bp.route('/<int:photo_id>/followers-count')
def collectors_count(photo_id):
    photo = Photo.query.get_or_404(photo_id)
    count = len(photo.collectors)
    return jsonify(count=count)


@ajax_bp.route('/collect/<int:photo_id>', methods=['POST'])
def collect(photo_id):
    current_app.logger.debug('ajax.py:collect()--->')
    if not current_user.is_authenticated:
        return jsonify(message='Login required.'), 403
    # if not current_user.confirmed:
    #     return jsonify(message='Confirm account required.'), 400
    if not current_user.can('COLLECT'):
        return jsonify(message='No permission.'), 403

    photo = Photo.query.get_or_404(photo_id)
    if current_user.is_collecting(photo):
        return jsonify(message='Already collected.'), 400

    current_user.collect(photo)
    if current_user != photo.author and photo.author.receive_collect_notification:
        push_collect_notification(collector=current_user, photo_id=photo_id, receiver=photo.author)
    return jsonify(message='Photo collected.')


@ajax_bp.route('/uncollect/<int:photo_id>', methods=['POST'])
def uncollect(photo_id):
    current_app.logger.debug('ajax.py uncollect()')
    if not current_user.is_authenticated:
        return jsonify(message='Login required.'), 403

    photo = Photo.query.get_or_404(photo_id)
    if not current_user.is_collecting(photo):
        return jsonify(message='Not collect yet.'), 400

    current_user.uncollect(photo)
    return jsonify(message='Collect canceled.')
