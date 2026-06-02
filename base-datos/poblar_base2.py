import json
import os
from configuracion import Session
from crear_base_entidades import Carrera, Facultad

def poblar_carreras():
    session = Session()
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'datos_universidad', 'datos', 'carreras.json')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    for item in datos:
        facultad = session.query(Facultad).filter_by(nombre_oficial=item['facultad']).first()
        if facultad:
            carrera = Carrera(
                nombre=item['nombre'],
                codigo=item['codigo'],
                facultad=facultad
            )
            session.add(carrera)
        else:
            print(f"Advertencia: Facultad '{item['facultad']}' no encontrada para la carrera '{item['nombre']}'")
    
    session.commit()
    print("Carreras insertadas exitosamente.")

if __name__ == '__main__':
    poblar_carreras()
