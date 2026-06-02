from configuracion import Session
from crear_base_entidades import RecursoAcademico
from sqlalchemy import and_

def consulta():
    session = Session()
    recursos = session.query(RecursoAcademico).filter(and_(RecursoAcademico.tipo == 'Guia', RecursoAcademico.fecha_publicacion > '2024-05-01')).all()
    print("--- Guías publicadas después del 2024-05-01 ---")
    for r in recursos:
        print(f"{r.titulo} - {r.fecha_publicacion}")

if __name__ == '__main__':
    consulta()
