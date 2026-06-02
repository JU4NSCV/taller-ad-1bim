from configuracion import Session
from crear_base_entidades import RecursoAcademico
from sqlalchemy import or_

def consulta():
    session = Session()
    recursos = session.query(RecursoAcademico).filter(or_(RecursoAcademico.tipo == 'Libro', RecursoAcademico.tipo == 'Video')).all()
    print("--- Recursos que son Libro o Video ---")
    for r in recursos:
        print(f"{r.titulo} ({r.tipo})")

if __name__ == '__main__':
    consulta()
