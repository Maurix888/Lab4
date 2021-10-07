#Mauricio Caneo Catalan
#Universidad Finis Terrae
#Asignatura: Seguridad Informatica
#Profesor: Manuel Alba
#Laboratorio Evaluado N°4

#El cliente es Jonathan.
import socket
import random 
import sys

cl_socket = socket.socket()
cl_socket.connect(('localhost',8000))

while True:
    #Escribimos el mensaje al servidor.
    mensaje = input("Escribe un numero primo : ")
    K = input("Escribe un numero menor al anterior : ")
    #Guardamos K y P.
    P = int(mensaje)
    print("P = ",P)
    Num_K = int(K)
    print("K = ",K)
    #Genera un numero random menor a P.
    b = random.randint(1, P-1)
    #Generamos la llave para Jonathan.
    B = ((pow(int(K), b)) % P)
    print("B = ",B)
    #Enviamos mensaje que seria P.
    cl_socket.send(mensaje.encode())
    #Enviamos mensaje que seria K.
    cl_socket.send(K.encode())
    #Recibo A.
    A = cl_socket.recv(1024).decode()
    #Calculo clave secreta
    Kb = ((pow(int(A), b)) % P)
    print("CLave Secreta de Jonathan  = ",Kb)
    #Envio B desde el cliente.
    num_B = str(B)
    cl_socket.send(num_B.encode())

    #Cerramos el socket del cliente.
    print("Cerrando Socket...")
    cl_socket.close()
    sys.exit()
