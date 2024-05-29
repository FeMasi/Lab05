import database.corso_DAO
from database import corso_DAO
from database import studente_DAO
class Model:
    def __init__(self):
        pass

    def get_corsi(self):
        return corso_DAO.get_corsi()

    def get_iscritti(self, codins):
        return corso_DAO.get_iscritti_corso(codins)

    def get_studente(self, matricola):
        return studente_DAO.get_matricola(matricola)

    def get_corsi_studente(self, matricola):
        return corso_DAO.get_corsi_studente(matricola)