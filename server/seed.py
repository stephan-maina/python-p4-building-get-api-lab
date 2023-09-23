from app import db
from models import Book, Team

# Create and add some initial data to the database
def seed_data():
    with db.app.app_context():
        db.create_all()

        # Add books (players)
        book1 = Book(title='Cristiano Ronaldo', author='Al Nassr')
        book2 = Book(title='Darwin Nunez', author='Liverpool FC')
        book3 = Book(title='Valverde', author='Real Madrid')

        db.session.add(book1)
        db.session.add(book2)
        db.session.add(book3)

        # Add teams
        team1 = Team(name='Al Nassr', player='Cristiano Ronaldo')
        team2 = Team(name='Liverpool FC', player='Darwin Nunez')
        team3 = Team(name='Real Madrid', player='Valverde')

        db.session.add(team1)
        db.session.add(team2)
        db.session.add(team3)

        db.session.commit()
