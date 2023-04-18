import classes.mysql as mysql  # own document
import classes.person as person
import sqlite3  # database on files
import logging  # logs making
import time
import datetime


class income_control:
    employs = []
    guests = []
    suppliers = []
    people = 0
    db = mysql.mysqlDb()

    def __init__(self):
        self.types = self.db.query_select_all("SELECT * FROM person_type ")
        # logging.debug(self.types[0])
        registros = self.db.query_select_all('select * from people_list')
        for p in registros:
            per = person.person(p[0], p[1], p[2], p[3], p[4])
            if p[3] == 1:
                self.employs.append(per)
            elif p[3] == 2:
                self.guests.append(per)
            elif p[3] == 3:
                self.suppliers.append(per)

    def all_people_in(self):
        people_in = self.db.query_select_all('SELECT * FROM people_list')
        logging.debug(people_in)
        if people_in == None:
            return 0
        else:
            return len(people_in)

    def entrance(self, id_person):
        time_ = datetime.datetime.now().time()
        date = datetime.datetime.now().date()
        self.db.query_insert('INSERT INTO registers (date,id_person,entrance) values("{}",{},"{}")'.format(
            date, id_person, time_))
        logging.debug('Se ha registrado correctamente el ingreso')

    def departure(self, id_person):
        time_ = datetime.datetime.now().time()
        registers = self.db.query_select_all(
            'SELECT * FROM registers WHERE id_person={}'.format(id_person))

        if registers == None:
            logging.debug('No hay registros con el id {}'.format(id_person))
        elif len(registers) == 1:
            logging.debug('hay 1 solo registro con el id {}'.format(id_person))
            self.db.query_insert(
                'UPDATE registers SET departure="{}" WHERE id_person={}'.format(time_, id_person))
            # me permite conocer las hora trabajadar por el trabajador que estoy buscando.
            time_worked = self.db.query_select_one(
                'SELECT TIMESTAMPDIFF(HOUR, entrance, departure) as horas FROM registers WHERE id_register={}'.format(registers[0][0]))
            logging.debug('tiempo trabajado: {}'.format(time_worked[0]))
            self.db.query_insert('UPDATE registers SET time_worked="{}" WHERE id_register = {}'.format(
                time_worked[0], registers[0][0]))
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
                            'UPDATE registers SET time_worked="1" WHERE id_register = {}'.format(registers[i][0]))
                    else:
                        logging.debug(
                            'tiempo trabajado: 1'.format(time_worked[0]))
                        self.db.query_insert('UPDATE registers SET time_worked="{}" WHERE id_register = {}'.format(
                            time_worked[0], registers[i][0]))
                    logging.debug('id_registro: {}'.format(registers[i][0]))
                    break
                i += 1
        logging.debug('Se ha registrado correctamente la salida')
