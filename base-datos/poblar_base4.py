import json
import os
from datetime import datetime
from configuracion import Session
from crear_base_entidades import RecursoAcademico, Profesor

def poblar_recursos():
    session = Session()
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'datos_universidad', 'datos', 'recursos_academicos.json')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    for item in datos:
        partes_nombre = item['profesor'].split(' ', 1)
        if len(partes_nombre) == 2:
            nombres = partes_nombre[0]
            apellidos = partes_nombre[1]
        else:
            nombres = item['profesor']
            apellidos = ''

        profesor = session.query(Profesor).filter_by(nombres=nombres, apellidos=apellidos).first()
        
        if profesor:
            fecha_pub = datetime.strptime(item['fecha_publicacion'], '%Y-%m-%d').date()
            recurso = RecursoAcademico(
                titulo=item['titulo'],
                fecha_publicacion=fecha_pub,
                tipo=item['tipo'],
                url=item['url'],
                profesor=profesor
            )
            session.add(recurso)
        else:
            print(f"Advertencia: Profesor '{item['profesor']}' no encontrado para el recurso '{item['titulo']}'")
    
    session.commit()
    print("Recursos académicos insertados exitosamente.")

if __name__ == '__main__':
    poblar_recursos()
