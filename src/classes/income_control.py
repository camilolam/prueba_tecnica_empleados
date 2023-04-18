import classes.mysql as mysql  # own document
import classes.person as person
import sqlite3  # database on files
import logging  # logs making
import datetime


class income_control:
    people = 0
    db = mysql.mysqlDb()

    def __init__(self):
        types = self.db.query_select_all('SELECT * FROM person_type')
        logging.info('Tipos de persona')
        logging.info(types)

    def entrance(self, id_person):
        try:
            time_ = datetime.datetime.now().time()
            date = datetime.datetime.now().date()
            persona = self.db.query_select_one(
                'SELECT * FROM people_list WHERE id_person={}'.format(id_person))
            id_area = persona[4]
            self.db.query_insert('INSERT INTO registers (date,id_person,entrance,area,company_in) values("{}",{},"{}",{},True)'.format(
                date, id_person, time_, id_area))
            logging.debug('Se ha registrado correctamente el ingreso')
        except Exception as ex:
            logging.error('problemas al registrar el ingreso')
            logging.error(ex)

    def departure(self, id_person):
        try:
            time_ = datetime.datetime.now().time()
            registers = self.db.query_select_all(
                'SELECT * FROM registers WHERE id_person={}'.format(id_person))

            if registers == None:
                logging.debug(
                    'No hay registros con el id {}'.format(id_person))

            elif len(registers) == 1:
                logging.debug(
                    'hay 1 solo registro con el id {}'.format(id_person))
                self.db.query_insert(
                    'UPDATE registers SET departure="{}" WHERE id_person={}'.format(time_, id_person))
                # me permite conocer las hora trabajadar por el trabajador que estoy buscando.
                time_worked = self.db.query_select_one(
                    'SELECT TIMESTAMPDIFF(HOUR, entrance, departure) as horas FROM registers WHERE id_register={}'.format(registers[0][0]))
                logging.debug('tiempo trabajado: {}'.format(time_worked[0]))
                self.db.query_insert('UPDATE registers SET time_worked="{}",company_in=False WHERE id_register = {}'.format(
                    time_worked[0], registers[0][0]))
                logging.debug('Se ha registrado correctamente la salida')

            else:
                logging.debug('{} registros con el id {}'.format(
                    len(registers), id_person))

                i = 0
                find = False
                while find == False and i < len(registers):
                    if registers[i][5] == 0:
                        self.db.query_insert('UPDATE registers SET departure="{}" WHERE id_register = {}'.format(
                            time_, registers[i][0]))
                        find = True
                        time_worked = self.db.query_select_one(
                            'SELECT TIMESTAMPDIFF(HOUR, entrance, departure) as horas FROM registers WHERE id_register={}'.format(registers[i][0]))  # me permite conocer las hora trabajadar por el trabajador que estoy buscando.

                        if time_worked[0] <= 0:
                            logging.debug(
                                'tiempo trabajado: 1')
                            self.db.query_insert(
                                'UPDATE registers SET time_worked="1",company_in=False WHERE id_register = {}'.format(registers[i][0]))

                        else:
                            logging.debug(
                                'tiempo trabajado: 1'.format(time_worked[0]))
                            self.db.query_insert('UPDATE registers SET time_worked="{}",company_in=False WHERE id_register = {}'.format(
                                time_worked[0], registers[i][0]))
                        logging.debug(
                            'id_registro: {}'.format(registers[i][0]))
                        break

                    i += 1
                # logging.debug('indice: {}'.format(i))
                # logging.debug('tamano - 1 : {}'.format((len(registers))))

                if i == (len(registers)):
                    logging.debug(
                        'No hay salidas para registrar con el id : {}'.format(id_person))
                else:
                    logging.debug(
                        'Se ha registrado correctamente la salida boom')
        except Exception as ex:
            logging.error('problemas al registrar la salida')
            logging.error(ex)

    def all_people_in(self):
        try:
            people = self.db.query_select_all(
                'SELECT distinct id_person FROM registers WHERE company_in = True')
            logging.debug('PERSONAS DENTRO DE LA COMPANIA')
            if len(people) <= 0 or people == None:
                logging.debug('No hay personas, dentro de la compañía')
            else:
                logging.debug(
                    'hay {} personas dentro de la Compañía'.format(len(people)))

        except Exception as ex:
            logging.error(
                'problemas al consultar el número de personas en la compañía')
            logging.error(ex)

    def add_employs(self, name, document, area):
        try:
            self.db.query_insert(
                'INSERT INTO people_list (name_person,document_person, id_type, id_area) values("{}","{}",1,"{}")'.format(name, document, area))
            logging.info('Se ha agregado un empleado nuevo')

        except Exception as ex:
            logging.error('problemas al agregar empleados')
            logging.error(ex)

    def add_guest(self, name, document):
        try:
            self.db.query_insert(
                'INSERT INTO people_list (name_person,document_person, id_type, id_area) values("{}","{}",2,4)'.format(name, document))
            logging.info('Se ha agregado un invitado nuevo')

        except Exception as ex:
            logging.error('problemas al agregar invitado')
            logging.error(ex)

    def add_supplier(self, name, document):
        try:
            self.db.query_insert(
                'INSERT INTO people_list (name_person, document_person, id_type, id_area) values("{}","{}",3,4)'.format(name, document))
            logging.info('Se ha agregado un proveedor nuevo')

        except Exception as ex:
            logging.error('problemas al agregar proveedor')
            logging.error(ex)

    def edit_employs(self, name, document, area, id_person):
        try:
            self.db.query_insert(
                'update people_list (name_person,document_person, id_type, id_area) values("{}","{}",1,"{}")'.format(name, document, area))
            logging.info('Se ha agregado un empleado nuevo')

        except Exception as ex:
            logging.error('problemas al agregar empleados')
            logging.error(ex)

    def edit_guest(self, name, document, id_person):
        try:
            self.db.query_insert(
                'update people_list (name_person,document_person, id_type, id_area) values("{}","{}",2,4)'.format(name, document))
            logging.info('Se ha agregado un invitado nuevo')

        except Exception as ex:
            logging.error('problemas al agregar invitado')
            logging.error(ex)

    def edit_supplier(self, name, document, id_person):
        try:
            self.db.query_insert(
                'update people_list set name_person = "{}", document_person = "{}" where id_person = {}'.format(name, document, id_person))
            logging.info('Se ha agregado un proveedor nuevo')

        except Exception as ex:
            logging.error('problemas al agregar proveedor')
            logging.error(ex)

    def delete_person(self, id_person):
        try:
            self.db.query_insert(
                'delete from people_list where id_person = {}'.format(id_person))
            logging.info('Se ha eliminado a la persona')

        except Exception as ex:
            logging.error('problemas al eliminar a la persona')
            logging.error(ex)
