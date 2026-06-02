from configuracion import Session
from crear_base_entidades import Carrera

def consulta():
    session = Session()
    carreras = session.query(Carrera).filter(Carrera.facultad.has(nombre_oficial="Facultad de Ingeniería")).all()
    print("--- Carreras de la Facultad de Ingeniería ---")
    for c in carreras:
        print(c)

if __name__ == '__main__':
    consulta()
