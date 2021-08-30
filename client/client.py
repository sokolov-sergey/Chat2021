from os import error
import time
import socket

# объявление переменных
addrServer = '192.168.1.100' # '46.188.6.194'
portServer =  12345

# функция подключения. принимает параметры для подключения
def connect(addr, port):
    print('Connecting to ' +addr, port)
    srv = socket.socket()
    srv.connect((addr, port))
    srv.send(bytes('$CONNECT','utf-8'))
    resp = srv.recv(1024)

    if not resp or resp.decode('utf-8') == '$$CONNECT_REJ':
        print('Connection error')
        return False

    return srv

def sendToServer(msg:str, server:socket):
    server.send(bytes(msg,'utf-8'))

 
server = connect(addrServer, portServer)

if server == False:
    exit('Connection error')
else:
    print('Succesfully connected')

#Главный цикл
while True:
        msg = input('Enter your message here: ')
        if msg == 'exit':
            print('Quitting the chat...')
            break
        else:
            sendToServer(msg,server)

        try:
            server.settimeout(0.1)
            msgFromSrv = server.recv(1024)  
       
            print("msg size:",len(msgFromSrv))
            if not msgFromSrv:
                print("empty message from server has come")

            print('Server message ['+time.strftime("%H:%M:%S")+']: ',msgFromSrv.decode ('utf-8'))
        except socket.timeout as ex:
            pass

