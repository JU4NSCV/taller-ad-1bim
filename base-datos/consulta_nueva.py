from configuracion import Session
from crear_base_entidades import RecursoAcademico, Profesor, Carrera

def consulta_recursos_salud():
    session = Session()
    
    recursos = session.query(RecursoAcademico).filter(
        RecursoAcademico.profesor.has(
            Profesor.carrera.has(
                Carrera.facultad.has(nombre_oficial="Facultad de Educación")
            )
        )
    ).all()
    
    print("--- Recursos de la Facultad de Educación ---")
    for r in recursos:
        print(r)

if __name__ == '__main__':
    consulta_recursos_salud()