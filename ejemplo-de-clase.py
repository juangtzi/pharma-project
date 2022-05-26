import pymysql
import os
#import sys

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='toor',
            db='pedidos'
        )
        self.cursor = self.connection.cursor()
        print("Conexión establecida exitosamente!")

    def select_user(self, id):
        sql = 'SELECT id_clientes, apellido, nombres FROM clientes WHERE id_clientes = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone() #Si queremos obtener un solo registro utilizamos fetchone

            print("Id: ", user[0])
            print("Apellido: ", user[1])
            print("Nombres: ", user[2])
        except Exception as e:
            raise

    def select_all_users(self):
        sql = 'SELECT id_clientes, apellido, nombres FROM clientes'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall() #Si queremos obtener mas de un registro utilizamos fetchall

            for user in users:
                print("Id: ", user[0])
                print("Username: ", user[1])
                print("Nombre:", user[2])
                print("______\n")

        except Exception as e:
            raise

     #Cuando realizamos alguna modificación a nuestra tabla, para insertar, actualizar o eliminar un registro
     #Lo que debemos hacer es que el cambio persista de forma permanente con commit
    def update_user(self, id, username):
        sql = "UPDATE clientes SET apellido='{}' WHERE id_clientes = {}".format(username, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        
        except Exception as e:
            raise

    def insert(self):
        surname = input("Inglese un apellido: \n")
        name = input("Inglese un nombre: \n")
        adrress = input("Inglese una dirección: \n")
        mail = input("Inglese un email: \n")
        
        sql = "INSERT INTO clientes(apellido, nombres, dirección, mail) values('{}', '{}', '{}', '{}')".format(surname,name,adrress,mail)
        self.cursor.execute(sql)
        self.connection.commit()
        print("Ingresado correctamente \n")
        os.system('pause')

    
    #Finalizar la conexion
    def close(self):
        self.connection.close()

# if __name__ == '__main__':

#     database = DataBase()



    # database.insert()
    # database.select_user(1)
    # database.select_all_users()

    # database.close()

    #database.update_user(1, 'Gutierrez')



