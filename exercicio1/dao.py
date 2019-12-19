from exercicio1.ex1 import Papel


class Dao:
    engine = db.create_engine(
        'mysql+mysqlconnector://topskills05:Andrei2019@mysql.topskills.study/topskills05')
    Session = db.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    def listar(self):
        papeis = self.session.query(Papel).all()

        print(f'\n{30*"="} Todas as linhas {30*"="}')
        for p in papeis:
            print(f'\t{p}')

    def filtrar_por_codigo(self, codigo):
        papel = self.session.query(Papel).filter_by(
            codigo=f'{codigo}').first()

        print(f'\n{30*"="} Todas as linhas {30*"="}')
        print(f'\t{papel}')


start = Dao()


start.filtrar_por_codigo('LCDP')
