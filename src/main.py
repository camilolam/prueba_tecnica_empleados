# Se van a hacer dos posibles bases de datos, sqlite y mysql
import classes.mysql as mysql# own document
import classes.person as person
import sqlite3 # database on files 
import logging # logs making 

# DEBUG =10
# INFO = 20 
# WARNING = 30 
# ERROR = 40 
# CRITICAL = 50

logging.basicConfig(level=logging.DEBUG)

class income_control: 
    employs = []
    guests = []
    suppliers = []
    people = 0
    db = mysql.mysqlDb()
    
    def __init__(self):
        self.types = self.db.query_select_all("SELECT * FROM person_type ")
        #logging.debug(self.types[0])
        registros = self.db.query_select_all('select * from people_list')
        for p in registros: 
            per = person.person(p[0],p[1],p[2],p[3],p[4])
            if p[3]==1:
                self.employs.append(per)
            elif p[3] == 2:
                self.guests.append(per)
            elif p[3] == 3:
                self.suppliers.append(per)
        
        logging.debug(self.types)
        logging.debug(self.employs)
        logging.debug(self.guests)
        logging.debug(self.suppliers)
    
    def all_people(self):
        return (len(self.employs)+len(self.guests)+len(self.employs))
        

if __name__=='__main__':
    company = income_control()
    #datos=company.db.query_select_all("SELECT * FROM people_list")
    #logging.info(datos)