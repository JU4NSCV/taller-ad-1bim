from configuracion import Session
from crear_base_entidades import Profesor

def consulta():
    session = Session()
    profesores = session.query(Profesor).order_by(Profesor.apellidos).all()
    print("--- Profesores ordenados por apellidos ---")
    for p in profesores:
        print(f"{p.apellidos} {p.nombres} - {p.especialidad}")

if __name__ == '__main__':
    consulta()
