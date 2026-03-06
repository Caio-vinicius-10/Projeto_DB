from fastapi import FastAPI, Depends, HTTPException
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# conexão com banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Estudante

@app.post("/estudantes/", response_model=schemas.Estudante)
def criar_estudante(
    estudante: schemas.EstudanteCreate,
    db: Session = Depends(get_db)
):

    db_estudante = models.Estudante(
        nome=estudante.nome,
        email=estudante.email,
        perfil=models.Perfil(**estudante.perfil.model_dump())
    )

    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)

    return db_estudante


@app.get("/estudantes/", response_model=List[schemas.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):

    estudantes = db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil)
    ).all()

    return estudantes



# Professor

@app.post("/professores/", response_model=schemas.Professor)
def criar_professor(
    professor: schemas.ProfessorCreate,
    db: Session = Depends(get_db)
):

    db_professor = models.Professor(
        nome=professor.nome,
        disciplina=professor.disciplina
    )

    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)

    return db_professor


@app.get("/professores/", response_model=List[schemas.Professor])
def listar_professores(db: Session = Depends(get_db)):

    professores = db.query(models.Professor).all()

    return professores

# Matriculas

@app.post("/matriculas/", response_model=schemas.Matricula)
def criar_matricula(
    matricula: schemas.MatriculaCreate,
    db: Session = Depends(get_db)
):

    db_matricula = models.Matricula(
        estudante_id=matricula.estudante_id,
        professor_id=matricula.professor_id
    )

    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)

    return db_matricula


@app.get("/matriculas/", response_model=List[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):

    matriculas = db.query(models.Matricula).all()

    return matriculas