from dao.base_dao import BaseDao
from model.tipo_papel import TipoPapel

class TipoPapelDao(BaseDao):
    def __init__(self):
        self.model = TipoPapel
        super().__init__(self.model)

    def list_asc_name(self):
        return self.session.query(self.model).order_by(self.model.nome.asc()).all()

    def filter_name(self, nome):
        return self.session.query(self.model).filter_by(nome=nome).all()

     #---- apenas metodo especifico para Papel
    def get_by_cod(self, cod):
        return self.session.query(self.model).filter(self.model.codigo.contains(cod))
    
    #---- update
    def update(self, object:TipoPapel):
        old_obj:TipoPapel = self.get_by_id(object.id)

        old_obj.nome = object.nome
        old_obj.descricao = object.descricao
        self.session.commit()