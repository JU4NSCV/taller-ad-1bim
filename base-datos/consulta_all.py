from configuracion import Session
from crear_base_entidades import Facultad

def consulta():
    session = Session()
    facultades = session.query(Facultad).all()
    print("--- Todas las Facultades ---")
    for f in facultades:
        print(f)

if __name__ == '__main__':
    consulta()
