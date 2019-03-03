from faker import Faker
from sqlalchemy.exc import IntegrityError

from noirart.extensions import db
from noirart.models import User

fake = Faker()


def fake_admin():
    admin = User(name='YouSheng',
                 username='yoyo',
                 email='1197993367@qq.com',
                 bio=fake.sentence(),
                 website='https://www.github.com/youyuge34',
                 confirmed=True)
    admin.set_password('123456')
    db.session.add(admin)
    admin = User(name='tony',
                 username='tony',
                 email='tony@qq.com',
                 bio=fake.sentence(),
                 website='https://www.github.com/youyuge34',
                 confirmed=True)
    admin.set_password('123456')
    db.session.add(admin)
    db.session.commit()


def fake_user(count=10):
    for i in range(count):
        user = User(name=fake.name(),
                    confirmed=True,
                    username=fake.user_name(),
                    bio=fake.sentence(),
                    location=fake.city(),
                    website=fake.url(),
                    member_since=fake.date_this_decade(),
                    email=fake.email())
        user.set_password('123456')
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
