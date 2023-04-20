import classes.mysql as mysql  # own document
import classes.person as person
import sqlite3  # database on files
import logging  # logs making
import datetime

# DEBUG =10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50


class income_control:
    people = 0
    db = mysql.mysqlDb()

    def __init__(self):
        types = self.db.query_select_all('SELECT * FROM person_type')
        logging.info('Tipos de persona')
        logging.info(types)

    def entrance(self, id_person):
        try:
            before_register = self.db.getPerson_registers(id_person)
            count = 0
            for register in before_register:
                if register[5] == 0:
                    count += 1

            if count == 0:
                time_ = datetime.datetime.now().time()
                date = datetime.datetime.now().date()
                persona = self.db.getPerson(id_person)
                id_area = persona[4]
                id_type = persona[3]
                self.db.add_register(date, id_person, time_, id_area, id_type)
                logging.debug('Se ha registrado correctamente el ingreso')

            else:
                logging.debug(
                    'No se puede ingresar nuevamente, tienes que registrar la salida')
        except Exception as ex:
            logging.error('problemas al registrar el ingreso')
            logging.error(ex)

    def departure(self, id_person):
        try:
            time_ = datetime.datetime.now().time()
            registers = self.db.getPerson_registers(id_person)
            if registers == None:
                logging.debug(
                    'No hay registros con el id {}'.format(id_person))

            elif len(registers) == 1:
                logging.debug(
                    'hay 1 solo registro con el id {}'.format(id_person))
                if registers[0][5] == 0:
                    self.db.register_departure(time_, registers[0][0])
                    time_worked = self.db.get_time_worked(registers[0][0])
                    logging.debug(
                        'tiempo trabajado: {}'.format(time_worked[0]))

                    if time_worked[0] <= 0:
                        self.db.register_time_worked(1, registers[0][0])
                    else:
                        self.db.register_time_worked(
                            time_worked[0], registers[0][0])

                    logging.debug('Se ha registrado correctamente la salida')
                else:
                    logging.debug('No hay salidas que registrar')

            else:
                logging.debug('{} registros con el id {}'.format(
                    len(registers), id_person))

                i = 0
                find = False
                while find == False and i < len(registers):
                    if registers[i][5] == 0:
                        self.db.register_departure(time_, registers[i][0])
                        find = True
                        time_worked = self.db.get_time_worked(registers[i][0])

                        if time_worked[0] <= 0:
                            self.db.register_time_worked(1, registers[i][0])

                        else:
                            self.db.register_time_worked(
                                time_worked[0], registers[i][0])

                        logging.debug(
                            'id_registro: {}, horas trabajadas: {}'.format(registers[i][0], time_worked[0]))
                        break

                    i += 1

                if i == (len(registers)):
                    logging.debug(
                        'No hay salidas para registrar con el id : {}'.format(id_person))
                else:
                    logging.debug(
                        'Se ha registrado correctamente la salida')

        except Exception as ex:
            logging.error('problemas al registrar la salida')
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

    def leave_early(self, id_person, excuse):
        time_ = datetime.datetime.now().time()
        try:
            logging.info('Nos fuimos temprano')
            registers = self.db.getPerson_registers(id_person)

            if registers == None:
                logging.debug(
                    'No hay registros con el id {}'.format(id_person))

            elif len(registers) == 1:
                if registers[0][5] == 0:
                    logging.debug(
                        'Hay 1 solo registro con el id {}'.format(id_person))
                    self.db.register_departure(time_, registers[0][0])

                    time_worked = self.db.get_time_worked(registers[0][0])
                    if time_worked[0] <= 0:
                        self.db.register_time_worked_early(
                            1, excuse, registers[0][0])

                    else:
                        self.db.register_time_worked_early(
                            time_worked[0], excuse, registers[0][0])

                    logging.debug(
                        'Se ha registrado correctamente la salida temprano')
                else:
                    logging.debug('No hay salidas que registrar')

            else:
                logging.debug('{} registros con el id {}'.format(
                    len(registers), id_person))

                i = 0
                find = False
                while find == False and i < len(registers):
                    if registers[i][5] == 0:
                        self.db.register_departure(time_, registers[0][0])
                        find = True
                        time_worked = self.db.get_time_worked(registers[0][0])

                        if time_worked[0] <= 0:
                            self.db.register_time_worked_early(
                                1, excuse, registers[i][0])

                        else:
                            self.db.register_time_worked_early(
                                time_worked[0], excuse, registers[i][0])

                        logging.debug(
                            'id_registro: {}'.format(registers[i][0]))
                        break
                    i += 1

                if i == (len(registers)):
                    logging.debug(
                        'No hay salidas para registrar con el id : {}'.format(id_person))

                else:
                    logging.debug(
                        'Se ha registrado correctamente la salida temprano')

        except Exception as ex:
            logging.error('problemas con la salida temprano')
            logging.error(ex)

    def get_registers_by_date(self, date):
        data = self.db.get_register_by_date(date)
        return data

    def get_registers(self, type):
        datetime.datetime
        info = {
            'registers': self.db.get_registers(),
            'employs': self.db.get_register_by_employs(),
            'guests': self.db.get_register_by_guests(),
            'suppliers': self.db.get_register_by_suppliers(),
        }
        # logging.debug(info[type])
        return info[type]
