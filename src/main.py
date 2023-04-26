# Se van a hacer dos posibles bases de datos, sqlite y mysql
import classes.income_control as income_control
import logging  # logs making
import classes.reports as reports
import datetime
import time

# DEBUG =10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    try:
        company = income_control.income_control()
        report = reports.report()
        # data = report.report_time_worked_by_employ()
        # logging.info(data)

        data = report.report_time_worked_by_area()
       # logging.info(data)
        # report.all_people_in()
        # logging.info(company.all_people_in())
        # company.add_employs('jorge montoya', '133636343563', 2)
        # company.add_guest('Victor Escobar', '46623737')
        # company.add_supplier('Laura Rodriguez', '6784575654')

        # company.edit_supplier('Laura Rodriguez', '1234567890', 6)
        # # company.delete_person(5)
        # company.entrance(1)
        # company.entrance(3)
        # # # company.entrance(6)
        # # # company.entrance(4)
        # time.sleep(1)
        # company.departure(1)
        # company.departure(3)
        # time.sleep(1)
        # time = report.report_time_worked_by_employ()
        # logging.info(time)

        # company.leave_early(3, 1)

        # data = company.get_registers('registers')
        # # data1 = company.get_registers('guests')
        # # data2 = company.get_registers('employs')
        # # data3 = company.get_registers('suppliers')

        # date = datetime.datetime.now().date()
        # info = company.get_registers_by_date(date)

        # logging.debug(len(info))
        # logging.debug(data)
        # logging.debug(len(data1))
        # logging.debug(len(data2))
        # logging.debug(len(data3))

    except Exception as ex:
        logging.error('Error en el funcionamiento de la app')
        logging.error(ex)
