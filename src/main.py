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
    company = income_control.income_control()
    logging.info(company.all_people_in())

    # company.entrance(3)
    # time.sleep(1000)
    company.departure(3)
    # logging.debug(datetime.datetime.now().time())
    # logging.debug(datetime.datetime.now().date())

    # company.db.query_insert('INSERT INTO registers (date,id_person,entrance) values(CURRENT_DATE(),1, CURRENT_TIME() - "00:05:00")')
    # datos=company.db.query_select_all("SELECT * FROM people_list")
    # logging.info(datos)
