import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

# =========== Aula 13 - Ex1

# 1 - Criar uma tabela na base de dados:
#   Papel(id, codigo, descricao, tipo_id)
# 2 - Inserir dados para teste
# 3 - Criar classe de dominio para mapeamento da tabela
# 4 - Criar classe base para manipulação da base de dados
# 5 - Criar classe Dao que contenha os seguintes métodos:
#       * listar_todos,
#       * listar_ultimos_dez_cadastrados,
#       * filtrar_por_codigo,
#       * buscar_por_id

# ----- Definição do nome da classe do alchemy como 'Base'
Base = declarative_base()


class Papel(Base):
    # ----- Definição do nome da tabela a qual esta classe representa
    __tablename__ = 'Papel'

# ----- Mapeamento de todas as colunas da tebela
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(length=100))
    tipo_id = db.Column(db.Integer)
    descricao = db.Column(db.String(length=200))

    def __str__(self):
        return f'"id":{self.id}, "codigo":"{self.codigo}", "tipo_id":{self.tipo_id}, "descricao":"{self.descricao}"'


# ===== Criação da engine e Sessao para conexao e consultas na base de dados
# ----- Criação da engine informando o conector, usuario, senha, url e a database
class Dao:
    engine = db.create_engine(
        'mysql+mysqlconnector://topskills05:Andrei2019@mysql.topskills.study/topskills05')
    Session = db.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()

# ----- Listando todos os dados da tabela
    def listar(self):
        papeis = self.session.query(Papel).all()

        print(f'\n{30*"="} Todas as linhas {30*"="}')
        for p in papeis:
            print(f'\t{p}')

# ----- Filtrando por codigo
    def filtrar_por_codigo(self, codigo):
        papel = self.session.query(Papel).filter_by(
            codigo=f'{codigo}').first()

        print(f'\n{30*"="} Linhas conforme codigo{30*"="}')
        print(f'\t{papel}')
# ----- Buscando o dado pelo id

    def buscar_por_id(self, id):
        papel_id = self.session.query(Papel).filter_by(id=f'{id}').first()

        print(f'\n{30*"="} Linha conforme Id{30*"="}')
        print(f'\t{papel_id}')
# ----- Listando os ultimos dez da tabela

    def listar_os_ultimos_dez(self):
        ultimos = self.session.query(Papel).order_by(
            Papel.id.desc()).limit(10).all()

        for p in ultimos:
            print(f'\t{p}')


# ----- Instanciando o objeto da Classe Dao
start = Dao()


start.listar_os_ultimos_dez()
