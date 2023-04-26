# clases para realizar al conexion con mysql
import pymysql
import logging
import json

logging.basicConfig(level=logging.DEBUG)


class mysqlDb:
    host = "www.db4free.net"
    user = 'prueba_tecnica'
    passwd = 'prueba1234.'
    db = 'ptecnica'

    def conn(self):
        try:
            data = pymysql.connect(
                host=self.host, user=self.user, passwd=self.passwd, db=self.db)  # MySQLdb
            return data
        except pymysql.Error as e:
            logging.error('Error al conectar la base de datos')
            return -1

    def getPerson(self, id_person):
        sql = 'SELECT * FROM people_list WHERE id_person={}'.format(id_person)
        data = self.query_select_one(sql)
        return data

    def get_registers(self):
        sql = 'SELECT * FROM registers'
        data = self.query_select_all(sql)
        return data

    def getPerson_registers(self, id_person):
        sql = 'SELECT * FROM registers WHERE id_person={}'.format(id_person)
        data = self.query_select_all(sql)
        return data

    def get_register_by_date(self, date):
        sql = 'SELECT * FROM registers WHERE date="{}"'.format(date)
        data = self.query_select_all(sql)
        return data

    def get_register_by_employs(self):
        sql = 'SELECT * FROM registers WHERE id_type = 1'
        data = self.query_select_all(sql)
        return data

    def get_register_by_employs_distinct(self):
        sql = 'SELECT distinct id_person FROM registers WHERE id_type = 1'
        data = self.query_select_all(sql)
        return data

    def get_register_by_guests(self):
        sql = 'SELECT * FROM registers WHERE id_type = 2'
        data = self.query_select_all(sql)
        return data

    def get_register_by_suppliers(self):
        sql = 'SELECT * FROM registers WHERE id_type = 3'
        data = self.query_select_all(sql)
        return data

    def add_register(self, date, id_person, time_, id_area, id_type):
        sql = 'INSERT INTO registers (date,id_person,entrance,area,company_in,id_type) values("{}",{},"{}",{},True,{})'.format(
            date, id_person, time_, id_area, id_type)
        self.query_insert(sql)

    def register_departure(self, time_, id_register):
        sql = 'UPDATE registers SET departure="{}" WHERE id_register={}'.format(
            time_, id_register)
        self.query_insert(sql)

    def get_time_worked(self, id_register):
        sql = 'SELECT TIMESTAMPDIFF(HOUR, entrance, departure) as horas FROM registers WHERE id_register={}'.format(
            id_register)
        data = self.query_select_one(sql)
        return data

    def register_time_worked(self, time_worked, id_register):
        sql = 'UPDATE registers SET time_worked={},company_in=False WHERE id_register = {}'.format(
            time_worked, id_register)
        self.query_insert(sql)

    def register_time_worked_early(self, time_worked, excuse, id_register):
        sql = 'UPDATE registers SET time_worked="{}",company_in=False, early=True, excuse = {} WHERE id_register = {}'.format(
            time_worked, excuse, id_register)
        self.query_insert(sql)

    def register_report_time_worked(self, date, id_person, id_area, time_worked):
        sql = 'INSERT INTO report_time_worked (date,id_person,id_area,all_time_work) values("{}",{},"{}",{})'.format(
            date, id_person, id_area, time_worked)
        self.query_insert(sql)

    def get_employ_time(self):
        sql = 'SELECT * FROM report_time_worked '
        data = self.query_select_all(sql)
        return data

    # --------------

    def query_select_all(self, sql):
        db = self.conn()
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            datos = cursor.fetchall()
            return datos
        except:
            db.close()
            return -1

    def query_select_one(self, sql):
        db = self.conn()
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            datos = cursor.fetchone()
            return datos
        except:
            db.close()
            return -1

    def query_insert(self, sql):
        db = self.conn()
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
        except Exception as ex:
            logging.error(ex)
            logging.error('error al insertar el registro')


if __name__ == '__main__':
    db1 = mysqlDb()
    datos = db1.query_select_all("SELECT * FROM empleados")
    logging.info(datos)
