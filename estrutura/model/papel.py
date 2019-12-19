import sqlalchemy as db
from .base_model import BaseDao
from sqlalchemy.orm import relationship, Session

from model.tipo_papel import TipoPapel

class Papel(BaseDao):
    __tablename__  = 'Papel'    
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(length=100))
    
    tipo_id = db.Column(db.Integer,db.ForeignKey('Tipo_Papel.id') )

    tipo_papel = relationship(TipoPapel)

    descricao = db.Column(db.String(length=200))
        
    def __str__(self):
        return f'''
                    {{
                        "id" :"{self.id}", 
                        "codigo" :"{self.codigo}", 
                        "tipo_id" :{self.tipo_id}, 
                        "descricao" :"{self.descricao}", 
                        "tipo_papel" : 
                            {self.tipo_papel}
                    }}
                '''
