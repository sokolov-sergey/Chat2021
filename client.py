from os import error
import time
import socket
import modules.proto as proto
import modules.transfer as tsf



# объявление переменных
addrServer = '192.168.1.100' # '46.188.6.194'
portServer =  12345

# функция подключения. принимает параметры для подключения
def connect(addr, port, nickname):
    print('Connecting to ' +addr, port)
    srv = socket.socket()
    srv.connect((addr, int(port)))

    # вызываем из модуля протокола proto.connect(), чтобы отправить на сервер 
    # запрос на подключение 
    rq = proto.connect()+proto.regUser(nickname)
    tsf.send(srv, rq)

    respMsg =tsf.recv(srv)
    print("Server said: ",respMsg)
    if not respMsg or respMsg == proto.connectionResult(False):
        print('Connection error')
        return False

    return srv    

def sendToServer(server:socket, msg:str):
    tsf.send(server, msg)

if __name__ == "__main__":

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
                sendToServer(server,msg)

            try:
                server.settimeout(0.1)
                
                srvMsg=tsf.recv(server)
        
                print("msg size:",len(srvMsg))
                if not srvMsg:
                    print("empty message from server has come")

                print('Server message ['+time.strftime("%H:%M:%S")+']: ',srvMsg)
            except socket.timeout as ex:
                pass

