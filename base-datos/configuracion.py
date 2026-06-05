from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://user:password@localhost:5434/universidad_db') # Cadena de postgres
#engine = create_engine('mysql+pymysql://root:rootpassword@localhost:3308/universidad_db') #Cadena de mariadb
#engine = create_engine('sqlite:///universidad.db')  #Cadena de sqlite

Session = sessionmaker(bind=engine)