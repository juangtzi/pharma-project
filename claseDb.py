import pymysql
import os
from datetime import date, time, datetime
from colorama import Fore, init
init()

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='sql10.freesqldatabase.com',
            user='sql10484748',
            password='bEuFyDVExv',
            db='sql10484748'
        )
        self.cursor = self.connection.cursor()
        print("Conexión establecida\n")

    def insert(self):
        print(Fore.LIGHTYELLOW_EX)
        name = input("Ingrese el nombre: \n")
        print("\n")
        surname = input("Ingrese el apellido: \n")
        print("\n")
        date = input("Ingrese fecha de nacimiento (YYYY-mm-dd): \n")
        print("\n")
        dni = input("Ingrese número de DNI: \n")
        print("\n")
        sex = input("Ingrese el sexo (M/F): \n")
        print("\n")
        weight = input("Ingrese el peso (kg): \n")
        print("\n")
        height = input("Ingrese la altura (cm): \n")
        print("\n")
        diagnostic = input("Ingrese el diagnóstico: \n")
        print("\n")
        drug = input("Ingrese el fármaco: \n")
        print(Fore.RESET)
        
        
        sql = "INSERT INTO paciente(nombre, apellidos, fecha_nacimiento, dni, sexo, peso, altura, diagnostico, farmaco) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name, surname, date, dni, sex, weight, height, diagnostic, drug)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
            
        
        except Exception as e:
            raise

    
    def select_all_users(self):
        sql = 'SELECT id_paciente, nombre, apellidos, DATE_FORMAT(fecha_nacimiento, "%d/%m/%Y"), TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) ,dni, sexo, peso, altura, diagnostico, farmaco FROM paciente'
        
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall() #Si queremos obtener mas de un registro utilizamos fetchall
            print(Fore.CYAN)
            for user in users:
                print("Id:", user[0])
                print("Nombre:", user[1])
                print("Apellido:", user[2])
                print("Nacimiento:", user[3])
                print("Edad actual:", user[4])
                print("DNI:", user[5])
                print("Sexo:", user[6])
                print("Peso:", user[7],"kg")
                print("Altura:", user[8],"cm")
                print("Diagnóstico:", user[9])
                print("Farmaco:", user[10])
                print("___________________\n")
                print("___________________\n")
            print(Fore.RESET)
            
                

        except Exception as e:
            raise

    
    def select_user(self):
        print(Fore.LIGHTYELLOW_EX)
        dni1 = input("Ingrese numero de DNI: ")
        print(Fore.RESET)
        sql = 'SELECT id_paciente, nombre, apellidos, DATE_FORMAT(fecha_nacimiento, "%d/%m/%Y"), TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) ,dni, sexo, peso, altura, diagnostico, farmaco FROM paciente WHERE dni = {}'.format(dni1)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone() #Si queremos obtener un solo registro utilizamos fetchone
            print(Fore.CYAN)
            print("___________________\n")
            print("___________________\n")
            print("Id:", user[0])
            print("Nombre:", user[1])
            print("Apellido:", user[2])
            print("Nacimiento:", user[3])
            print("Edad actual:", user[4])
            print("DNI:", user[5])
            print("Sexo:", user[6])
            print("Peso:", user[7],"kg")
            print("Altura:", user[8],"cm")
            print("Diagnóstico:", user[9])
            print("Farmaco:", user[10])
            print("___________________\n")
            print("___________________\n")
            print(Fore.RESET)
        except Exception as e:
            raise  
    

        
    def close(self):
        self.connection.close()
    
    