# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


def get_corsi() -> list[Corso] | None:
    """
    Funzione che legge tutti i corsi nel database
    :return: una lista con tutti i corsi presenti
    """

    cnx = DBConnect.get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM corso")
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

def get_iscritti_corso(codins) -> list[Studente] | None:
    cnx = DBConnect.get_connection()
    result = []
    query = """SELECT studente.* 
                        FROM iscrizione, studente 
                        WHERE iscrizione.matricola=studente.matricola 
                        AND iscrizione.codins = %s"""
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (codins,))
        for row in cursor:
            result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None


def get_corsi_studente(matricola) -> list[Corso]:
    """
               Funzione che data una matricola ricerca nel database i corsi frequentati
               :param matricola: la matricola dello studente da ricercare
               :return: una lista di corsi
               """
    cnx = DBConnect.get_connection()
    result = []
    query = """ SELECT c.* 
       FROM iscrizione, corso c
       WHERE iscrizione.codins=c.codins AND iscrizione.matricola = %s
       """
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (matricola,))
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return result