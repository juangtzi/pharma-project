from calendar import c
import os, time
from sys import stdout
import platform
import socket
from colorama import Fore, init
init()

#Clase de otro archivo
import claseDb as c
class1 = c.DataBase()

#Los siguientes comandos imprimen el nombre del equipo
#print("Bienvenido " + socket.gethostname())
#print("Bienvenido " + platform.node())
#print("Bienvenido + os.environ['COMPUTERNAME']
#El siguiente comando imprime el nombre del usuario
print(Fore.GREEN + "Bienvenido, " + os.getlogin() + Fore.RESET)
banner = """
 
      ███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░░█████╗░██╗░█████╗░     
      ██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██║██╔══██╗      
      █████╗░░███████║██████╔╝██╔████╔██║███████║██║░░╚═╝██║███████║      
      ██╔══╝░░██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║██║░░██╗██║██╔══██║
      ██║░░░░░██║░░██║██║░░██║██║░╚═╝░██║██║░░██║╚█████╔╝██║██║░░██║
      ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝
        

A continuación, coloque un número (1-4) según la tarea que desea realizar.\n\n
        """

def menu():
    
    print(Fore.GREEN + banner)
    time.sleep(0.2)   
    print(Fore.YELLOW + "1 -> Agregar un paciente a la base de datos")
    time.sleep(0.2)
    print("\n2 -> Buscar paciente por numero de DNI")
    time.sleep(0.2)
    print("\n3 -> Mostrar una lista de todos los pacientes")
    time.sleep(0.2)
    print("\n4 -> Salir")
    time.sleep(0.2)
    
    option = input("\n-->> ")
    
    print(Fore.RESET)
    
    
    if option == "1":
        class1.insert()
        print("Datos ingresados correctamente\n")
        time.sleep(1)
        menu()
        
    if option == "2":
        class1.select_user()
        os.system('pause')
        menu()
        
    if option == "3":
        class1.select_all_users()
        os.system('pause')
        menu()
        
    
    if option == "4":
        class1.close()
        exit()



if __name__=='__main__':
    menu()
    
    
    