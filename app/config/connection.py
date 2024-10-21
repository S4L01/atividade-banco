from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session

@contextmanager
def get_db():
    db = Session()#criar uma sessao para acoes no banco de dados
    try:
        yield db#caso a sessao realize todas as tarefas, salva operaçao
        db.commit()
    except Exception as erro:
        db.rollback() # desfaz todas alteracoes em caso de erro em alguma operacao
        raise erro #lança uma exccao
    finally:
        db.close()# fecha sessao com o banco de dados        
