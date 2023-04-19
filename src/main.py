# Se van a hacer dos posibles bases de datos, sqlite y mysql
import classes.income_control as income_control
import logging  # logs making

# DEBUG =10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    try:
        company = income_control.income_control()
        # logging.info(company.all_people_in())
        # company.add_employs('jorge montoya', '133636343563', 2)
        # company.add_guest('Victor Escobar', '46623737')
        # company.add_supplier('Laura Rodriguez', '6784575654')

        # company.edit_supplier('Laura Rodriguez', '1234567890', 6)
        # company.delete_person(5)
        # company.entrance(6)
        #    time.sleep(1000)
        # company.departure(6)
        # company.all_people_in()
        # logging.debug(datetime.datetime.now().time())
        # logging.debug(datetime.datetime.now().date())
        company.leave_early(4, 2)
        # company.db.query_insert('INSERT INTO registers (date,id_person,entrance) values(CURRENT_DATE(),1, CURRENT_TIME() - "00:05:00")')
        # datos=company.db.query_select_all("SELECT * FROM people_list")
        # logging.info(datos)
    except Exception as ex:
        logging.error('Error en el funcionamiento de la app')
        logging.error(ex)
        logging.info('Revisa la conexión a internet')
