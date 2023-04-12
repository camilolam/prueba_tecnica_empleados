# Se van a hacer dos posibles bases de datos, sqlite y mysql
import pymysql
import mysql


if __name__=='__main__':
    db1=mysql.mysqlDb()
    datos=db1.query_select_all("SELECT * FROM empleados")
    print(datos)
