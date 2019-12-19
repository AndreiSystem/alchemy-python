from dao.base_dao import BaseDao
from model.papel import Papel

class PapelDao(BaseDao):
    def __init__(self):
        self.model = Papel
        super().__init__(self.model)

    #---- apenas metodo especifico para Papel
    def get_by_cod(self, cod):
        return self.session.query(self.model).filter(self.model.codigo.contains(cod))
    
    #---- update
    def update(self, object:Papel):
        old_obj:Papel = self.get_by_id(object.id)

        old_obj.codigo = object.codigo
        old_obj.descricao = object.descricao
        old_obj.tipo_id = object.tipo_id
        self.session.commit()






    
           

    
