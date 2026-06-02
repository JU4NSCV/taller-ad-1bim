import json
import os
from configuracion import Session
from crear_base_entidades import Profesor, Carrera

def poblar_profesores():
    session = Session()
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'datos_universidad', 'datos', 'profesores.json')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    for item in datos:
        carrera = session.query(Carrera).filter_by(nombre=item['carrera']).first()
        if carrera:
            profesor = Profesor(
                nombres=item['nombres'],
                apellidos=item['apellidos'],
                correo=item['correo'],
                especialidad=item['especialidad'],
                carrera=carrera
            )
            session.add(profesor)
        else:
            print(f"Advertencia: Carrera '{item['carrera']}' no encontrada para el profesor '{item['nombres']} {item['apellidos']}'")
    
    session.commit()
    print("Profesores insertados exitosamente.")

if __name__ == '__main__':
    poblar_profesores()
