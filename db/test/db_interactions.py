from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


DB_HOST = "localhost"
DB_NAME = "main"
DB_USER = "postgres"
DB_PASSWORD = "changeme"
PORT = 5432

# Database connection
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Base for ORM models
Base = declarative_base()



# Define models


# Junction table for many-to-many relationship
user_cards = Table(
    "user_cards",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("card_id", Integer, ForeignKey("cards.card_id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    cards = relationship("Card", secondary=user_cards, backref="users")  # Many-to-many relationship

class Card(Base):
    __tablename__ = "cards"
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    card_name = Column(String, nullable=False)

# Create tables in the database
Base.metadata.create_all(engine)





# Create a session
session = SessionLocal()

# Insert users
user1 = User(username="vova")
user2 = User(username="oleg")

# Insert cards
card1 = Card(card_name="Card 1")
card2 = Card(card_name="Card 2")
card3 = Card(card_name="Card 3")

# Associate cards with users
user1.cards.append(card1)  # John has Card 1
user1.cards.append(card2)  # John has Card 2
user2.cards.append(card3)  # Jane has Card 3

# Add and commit to the database
session.add_all([user1, user2, card1, card2, card3])
session.commit()


# Query and pull cards for a single user
username = "vova"
user = session.query(User).filter(User.username == username).first()

if user:
    print(f"User: {user.username}")
    for card in user.cards:
        print(f"  Card ID: {card.card_id}, Card Name: {card.card_name}")
else:
    print(f"User '{username}' not found.")

# Close the session
session.close()
