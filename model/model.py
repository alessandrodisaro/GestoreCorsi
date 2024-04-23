from database.corso_dao import CorsoDao

class Model:
    # def __init__(self):
    #     pass

    def get_corsi_periodo(self,pd):
        return CorsoDao.get_corsi_periodo(pd)

    def get_numero_studenti_periodo(self,pd):


        #soluzione col join in sql
        return CorsoDao.get_numero_studenti_periodo(pd)
