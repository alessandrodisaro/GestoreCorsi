import mysql.connector
from database.DB_connect import DBConnect
from model.corso import Corso

class CorsoDao:  # posso decidere di alsciare i metodi che vivono da soli fuori da corsoDAO
    #posso fare un metodo statico (eseguo questo metodo senza avere un istanza di corsoDAO
    @staticmethod
    def get_corsi_periodo(pd):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore di connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query="""SELECT * FROM corso 
                    WHERE pd=%s"""
            cursor.execute(query,(pd,))
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_numero_studenti_periodo(pd):
        cnx=DBConnect.get_connection()
        result=[]
        if cnx is None:
            print ("Errore di connessione")
            return result
        else:
            cursor = cnx.cursor()
            query="""SELECT COUNT(DISTINCT i.matricola)
                    FROM corso c, iscrizione i
                    WHERE c.codins=i.codins and c.pd=%s"""
            cursor.execute(query, (pd,))
            result = 0
            if cursor.with_rows:
                result =  cursor.fetchone()[0]
            cursor.close()
            cnx.close()
            return result
            
