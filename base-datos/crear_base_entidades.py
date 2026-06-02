from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from configuracion import engine

Base = declarative_base()

class Facultad(Base):
    __tablename__ = 'facultad'
    id = Column(Integer, primary_key=True)
    nombre_oficial = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)
    decano = Column(String, nullable=False)
    
    carreras = relationship("Carrera", back_populates="facultad")

    def __str__(self):
        return f"Facultad: {self.nombre_oficial} (Decano: {self.decano} | Ubicación: {self.ubicacion})"

class Carrera(Base):
    __tablename__ = 'carrera'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, unique=True, nullable=False)
    
    facultad_id = Column(Integer, ForeignKey('facultad.id'), nullable=False)
    
    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship("Profesor", back_populates="carrera")

    def __str__(self):
        return f"Carrera: {self.nombre} [{self.codigo}]"

class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, primary_key=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    especialidad = Column(String, nullable=False)
    
    carrera_id = Column(Integer, ForeignKey('carrera.id'), nullable=False)
    
    carrera = relationship("Carrera", back_populates="profesores")
    recursos = relationship("RecursoAcademico", back_populates="profesor")

    def __str__(self):
        return f"Profesor: {self.nombres} {self.apellidos} - {self.especialidad} ({self.correo})"

class RecursoAcademico(Base):
    __tablename__ = 'recurso_academico'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    fecha_publicacion = Column(String) 
    tipo = Column(String, nullable=False)
    url = Column(String)
    
    profesor_id = Column(Integer, ForeignKey('profesor.id'), nullable=False)
    
    profesor = relationship("Profesor", back_populates="recursos")

    def __str__(self):
        return f"{self.tipo}: {self.titulo} (Publicado: {self.fecha_publicacion}) - {self.url}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Tablas creadas exitosamente en la base de datos.")