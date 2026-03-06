from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# ESTUDANTE
class Estudante(Base):
    __tablename__ = 'estudante'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)

    perfil = relationship(
        "Perfil",
        back_populates="estudante",
        uselist=False,
        cascade="all, delete-orphan"
    )

    matriculas = relationship("Matricula", back_populates="estudante")


# PERFIL
class Perfil(Base):
    __tablename__ = 'perfis'

    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)

    estudante_id = Column(
        Integer,
        ForeignKey("estudante.id"),
        unique=True
    )

    estudante = relationship(
        "Estudante",
        back_populates="perfil"
    )


# PROFESSOR
class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    disciplina = Column(String)

    matriculas = relationship("Matricula", back_populates="professor")


# MATRICULA
class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)

    estudante_id = Column(Integer, ForeignKey("estudante.id"))
    professor_id = Column(Integer, ForeignKey("professores.id"))

    estudante = relationship("Estudante", back_populates="matriculas")
    professor = relationship("Professor", back_populates="matriculas")