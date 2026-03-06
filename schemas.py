from typing import List, Optional
from pydantic import BaseModel

class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str 

    class Config:
        from_attributes = True

class PerfilCreate(BaseModel):
    idade: int
    endereco: str

#Estudante
class Estudante(BaseModel):
    id: int
    nome: str
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True 

class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: PerfilCreate

#Professor
class ProfessorBase(BaseModel):
    nome: str
    disciplina: str

class ProfessorCreate(ProfessorBase):
    pass

class Professor(ProfessorBase):
    id: int

    class Config:
        from_attributes = True

#Matricula
class MatriculaBase(BaseModel):
    estudante_id: int
    professor_id: int

class MatriculaCreate(MatriculaBase):
    pass

class Matricula(MatriculaBase):
    id: int

    class Config:
       from_attributes = True

