from app import app, db
from app.models.user import User  # Adjust this import if your User model is elsewhere

with app.app_context():

    admin = User.query.filter_by(email="admin@airport.com").first()

    if admin:
        print("Admin already exists.")
    else:
        admin = User(
            fullname="System Administrator",
            email="faanprotocol@gmail.com",
            role="admin"
        )

        admin.set_password("admin123")

        db.session.add(admin)
        db.session.commit()

        print("Admin created successfully!")