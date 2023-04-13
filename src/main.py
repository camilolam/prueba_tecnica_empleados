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




if __name__=='__main__':
    db1=mysql.mysqlDb()
    datos=db1.query_select_all("SELECT * FROM empleados")
    logging.info(datos)