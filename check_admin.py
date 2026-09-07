from app import app
from app.models.user import User

with app.app_context():
    users = User.query.all()

    for user in users:
        print(
            user.id,
            user.fullname,
            user.email,
            user.role
        )