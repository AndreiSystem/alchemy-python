import sys
sys.path.append(
    'C:/Users/900213/Desktop/alchemy-python/estrutura/')

from model.papel import Papel
from model.tipo_papel import TipoPapel
from dao.tipo_dao import TipoPapelDao
from dao.papel_dao import PapelDao


# === instanciando objeto da classe PapelDao
dao = PapelDao()

# === instanciando objeto da classe TipoPapelDao
dao_tipo = TipoPapelDao()

# === instanciando objeto da classe Papel
papel = Papel()
tipo_papel = TipoPapel()

# tipo_papel.nome = 'Opa'
# tipo_papel.descricao = 'Oi'
# tipo_papel.id = 6

# dao_tipo.delete(6)


