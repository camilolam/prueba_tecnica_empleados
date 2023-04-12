# clases para realizar al conexion con mysql

import pymysql
import sys

class mysqlDb: 
    host="www.db4free.net"
    user='prueba_tecnica'
    passwd='prueba1234.'
    db='ptecnica'

    def conn(self):
        try:
            data = pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db) #MySQLdb
            print('conexion correcta')
            return data
        except pymysql.Error as e:
            print('Error al conectar la base de datos')
            print(e)
            return -1
        
    def query_select_all(self,sql):
        db = self.conn()
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            datos = cursor.fetchall()
            return datos
        except:
            db.close()
            return -1
        
    def query_select_one(self,sql):
        db = self.conn()
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            datos = cursor.fetchone()
            return datos
        except:
            db.close()
            return -1
        
    def query_insert(self,sql):
        db = self.conn()
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
        except:
            print('error al insertar el registro')

    

if __name__=='__main__':
    db1=mysqlDb()
    datos=db1.query_select_all("SELECT * FROM empleados")
    print(datos)