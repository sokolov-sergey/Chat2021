from os import error
import time
import socket
import proto

# объявление переменных
addrServer = '192.168.1.100' # '46.188.6.194'
portServer =  12345

# функция подключения. принимает параметры для подключения
def connect(addr, port, nickname):
    print('Connecting to ' +addr, port)
    srv = socket.socket()
    srv.connect((addr, port))

    # вызываем из модуля протокола proto.connect(), чтобы отправить на сервер 
    # запрос на подключение 
    rq = proto.connect()+proto.regUser(nickname)
    srv.send(bytes(rq,'utf-8'))  
    resp = srv.recv(1024)
    respMsg = resp.decode('utf-8')
    print("Server said: ",respMsg)
    if not resp or respMsg == proto.connectionResult(False):
        print('Connection error')
        return False

    return srv

def sendToServer(msg:str, server:socket):
    server.send(bytes(msg,'utf-8'))

 
nickname = input("What is your nickname? ")
server = connect(addrServer, portServer, nickname)

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

