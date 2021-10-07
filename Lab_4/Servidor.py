#Mauricio Caneo Catalan
#Universidad Finis Terrae
#Asignatura: Seguridad Informatica
#Profesor: Manuel Alba
#Laboratorio Evaluado N°4

#El servidor es Mauricio.
import socket
import random 

sv_socket = socket.socket()
sv_socket.bind(('localhost',8000))
sv_socket.listen()

while True:
    #Se establece la conexion.
    conexion, direccion = sv_socket.accept()
    print("Conectado con el cliente", direccion)

    #Recibimos el numero P del cliente.
    MensajeR = conexion.recv(1024).decode()
    #Guardamos el numero recibido en la variable P.
    P = int(MensajeR)
    print("P = ",P)
    #Recibimos el numero K del cliente.
    MensajeK = conexion.recv(1024).decode() 
    #Guardamos el numero recibido en la variable K.
    K = int(MensajeK)
    print("K = ",K)
    #Genera un numero random menor a P.
    a = random.randint(1, P-1)
    #Generamos la llave para Mauricio.
    A = ((pow(K, a)) % P) 
    #Envio A.
    print("A = ", A)
    num_A = str(A)
    conexion.send(num_A.encode())
    #Recibo B desde del cliente.
    B = conexion.recv(1024).decode()
    #Calculo clave secreta.
    Ka = ((pow(int(B), a)) % P)
    print("CLave Secreta de Mauricio  = ",Ka)

    print("Desconectado el cliente", direccion)
    #Cerramos conexion.
    conexion.close()

    