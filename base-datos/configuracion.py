from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuramos la conexión a SQLite
# Si deseas usar PostgreSQL vía Docker, puedes usar: 'postgresql://user:password@localhost:5434/postgres'
engine = create_engine('sqlite:///universidad.db')

Session = sessionmaker(bind=engine)
