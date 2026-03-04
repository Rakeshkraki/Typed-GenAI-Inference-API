from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config import settings

#🔌 The connection factory to my database.
engine = create_engine(settings.database_url)

# A session is:
# 🧠 A conversation with the database
# Tracks objects
# Manages transactions
# Sends queries
# Commits changes
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


# SQLAlchemy:
# Gets connection from engine
# Starts a transaction
# Tracks objects you add
# On commit() → sends SQL
# On close() → returns connection to pool