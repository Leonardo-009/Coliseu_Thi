from sqlmodel import SQLModel, Session, create_engine
from models.models import School, StudentGroup, InviteKey, User
from pydantic.functional_validators import field_validator
#from pydantic import BaseSettings, BaseModel, Optional
#from pydantic import BaseModel, Optional
from pydantic_settings import BaseSettings



#altera o nome futuramente
database_file = "appT2.db"
database_connection_string = f"sqlite:///{database_file}"

connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def conn():
        # Cria o banco de dados .db e as tabelas
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session

