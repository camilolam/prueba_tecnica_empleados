import classes.mysql as mysql
import logging

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
