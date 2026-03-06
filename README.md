# Projeto API Escola – FastAPI

API desenvolvida com **FastAPI**, **SQLAlchemy** e **PostgreSQL** para gerenciamento de estudantes, professores e matrículas.

## 🚀 Tecnologias utilizadas

* Python 3.12
* FastAPI
* SQLAlchemy
* PostgreSQL
* Uvicorn
* Pydantic

## 📁 Estrutura do projeto

```
projeto-db
│
├── main.py          # Arquivo principal da aplicação
├── models.py        # Modelos do banco de dados (SQLAlchemy)
├── schemas.py       # Schemas de validação (Pydantic)
├── database.py      # Configuração da conexão com o banco
├── requirements.txt # Dependências do projeto
└── .gitignore
```

## ⚙️ Instalação

Clone o repositório:

```
git clone https://github.com/Caio-vinicius-10/Projeto_DB.git
```

Entre na pasta do projeto:

```
cd Projeto_DB
```

Crie o ambiente virtual:

```
python -m venv venv
```

Ative o ambiente virtual:

Windows:

```
venv\Scripts\activate
```

Instale as dependências:

```
pip install -r requirements.txt
```

## 🗄️ Configuração do banco de dados

No arquivo **database.py** configure a conexão com o PostgreSQL:

```
DATABASE_URL = "postgresql+psycopg2://usuario:senha@localhost:5432/db_escola"
```

Crie o banco de dados no PostgreSQL antes de rodar o projeto.

## ▶️ Executar o projeto

Inicie o servidor com:

```
uvicorn main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

## 📚 Documentação automática

FastAPI gera documentação automática:

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Redoc:

```
http://127.0.0.1:8000/redoc
```

## 📌 Endpoints principais

### Estudantes

* Criar estudante
  `POST /estudantes`

* Listar estudantes
  `GET /estudantes`

### Professores
  
* Criar professor
  `POST /professores`

* Listar professores
  `GET /professores`

### Matrículas

* Criar matrícula
  `POST /matriculas`

* Listar matrículas
  `GET /matriculas`

## 🎓 Curso de referência

Este projeto foi desenvolvido como parte dos estudos no curso:

**Persistência de dados com arquivos, bancos de dados e APIs REST**

Instrutor: Rodrigo Oliveira Suigh
Plataforma: Alura

O projeto foi adaptado e expandido para fins de estudo e prática de desenvolvimento de APIs com FastAPI, SQLAlchemy e PostgreSQL.

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

* Modelagem de banco de dados
* Relacionamentos com SQLAlchemy
* Criação de APIs REST com FastAPI
* Validação de dados com Pydantic
* Integração com PostgreSQL
* Estruturação de projetos backend em Python


## 👨‍💻 Autor

Caio Vinicius

GitHub:
https://github.com/Caio-vinicius-10
