import classes.mysql as mysql
import logging
import datetime

logging.basicConfig(level=logging.DEBUG)
# DEBUG =10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50


class report:
    db = mysql.mysqlDb()

    def all_people_in(self):
        try:
            people_id = self.db.query_select_all(
                'SELECT distinct id_person FROM registers WHERE company_in = True')
            logging.debug('PERSONAS DENTRO DE LA COMPANIA')
            if len(people_id) <= 0 or people_id == None:
                logging.debug('No hay personas, dentro de la compañía')
            else:
                logging.debug(
                    'hay {} persona(s) dentro de la Compañía'.format(len(people_id)))
                logging.debug(people_id)
                people = []
                for id in people_id:
                    logging.debug(id[0])
                    people.append(self.db.getPerson(id[0]))
                logging.debug(people)

        except Exception as ex:
            logging.error(
                'problemas al consultar el número de personas en la compañía')
            logging.error(ex)

    def report_time_worked_by_employ(self):
        try:
            id_employs_registers = self.db.get_register_by_employs_distinct()
            logging.debug(id_employs_registers)
            # today_ = date
            today = datetime.datetime.now().date()

            for id in id_employs_registers:
                registers = self.db.getPerson_registers(id[0])
                logging.debug('hay {} registro con el id {}'.format(
                    len(registers), id[0]))
                total = 0
                for reg in registers:
                    if reg[1] == today:
                        logging.debug(reg)
                        total += int(reg[5])

                self.db.register_report_time_worked(
                    today, id[0], reg[7], total)

        except Exception as ex:
            logging.error(
                'No se ha podido generar el reporte de las horas trabajadas')
            logging.error(ex)
