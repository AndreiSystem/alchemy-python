import sqlalchemy as db


class BaseDao:
    def __init__(self, table):
        conector = 'mysql+mysqlconnector'
        user = 'topskills05'
        passwd = 'Andrei2019'
        hostname = 'mysql.topskills.study'
        port = 3306
        database = 'topskills05'
        engine = db.create_engine(
            f'{conector}://{user}:{passwd}@{hostname}:{port}/{database}')
        Session = db.orm.sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()
        self.table = table

    def list_all(self):
        return self.session.query(self.table).all()

    def get_by_id(self, id):
        return self.session.query(self.table).filter_by(id=id).first()

    def top(self, limit):
        return self.session.query(self.table).limit(limit).all()

    def last_items_list(self, limit):
        return self.session.query(self.table).order_by(self.table.id.desc()).limit(limit).all()

    def list_asc_cod(self):
        return self.session.query(self.table).order_by(self.table.codigo.asc()).all()

    def insert(self, object):
        self.session.add(object)
        self.session.commit()

    def delete(self, id):
        obj = self.get_by_id(id)
        self.session.delete(obj)
        self.session.commit()

