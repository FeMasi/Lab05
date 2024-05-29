# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import DBConnect
from model.studente import Studente
from model.corso import Corso


def get_matricola(matricola) -> Studente | None:

    cnx = DBConnect.get_connection()
    query = """SELECT * FROM studente WHERE matricola=%s"""

    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (matricola,))
        row = cursor.fetchone()
        if row is not None:
            result = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
        else:
            result = None
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

