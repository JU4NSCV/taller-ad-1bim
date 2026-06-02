import json
import os
from configuracion import Session
from crear_base_entidades import Facultad

def poblar_facultades():
    session = Session()
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'datos_universidad', 'datos', 'facultades.json')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    for item in datos:
        facultad = Facultad(
            nombre_oficial=item['nombre'],
            ubicacion=item['ubicacion'],
            decano=item['decano']
        )
        session.add(facultad)
    
    session.commit()
    print("Facultades insertadas exitosamente.")

if __name__ == '__main__':
    poblar_facultades()
