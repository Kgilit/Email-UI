from app import app, db, User
from werkzeug.security import generate_password_hash

# Create a new user
email = 'testuser@example.com'
password = 'testpassword'
hashed_password = generate_password_hash(password)

# Add the user to the database
with app.app_context():
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

print("User added to database!")
