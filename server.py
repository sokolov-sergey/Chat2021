import socket
import proto

'''
CT21 protocol
$XXXXX - request cmd
$$XXXX -  response

$CONNECT - connect request
$$CONNECT_OK - connection is established
$$CONNECT_REJ - Connection rejected

$REG_NIK:NICKNAME

$SEND_MSG:USER:message_body
'''


def tryNewUserConnect(userConnect: socket, timeout=2):
    userConnect.settimeout(timeout)
    incomeMsg = userConnect.recv(1024)
    msg = incomeMsg.decode('utf-8')

    if(msg == proto.connect()):
        userConnect.send(bytes(proto.connectionResult(True), 'utf-8'))
        return True
    else:
        userConnect.send(bytes(proto.connectionResult(False), 'utf-8'))
        return False


def acceptClient(clientsList: list, timeout=2):
    try:
        # wait for client timeout seconds
        SrvSoket.settimeout(timeout)
        conn, remoteAddr = SrvSoket.accept()

        # check connection by protocol
        userConnResult = tryNewUserConnect(conn)
        if(userConnResult == False):
            print("Hacker attack detected")

        # our client has come, let's welcom him
        conn.send(bytes('Dear somebody, you are at my ct2021 server!!!', 'utf-8'))

        # save new client connection to list
        clientsList.append((conn, remoteAddr))
        return conn
    except socket.timeout:
        # just exit from proc if no new connection was accepted
        pass


########################################################################
###################### Main server program starts below ################
########################################################################
Addr, Port = "192.168.1.100", 12345
SrvSoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientsList = []

print("listening for ", Addr, Port)
SrvSoket.bind((Addr, Port))
SrvSoket.listen(30)

# main loop
while True:
    try:

        acceptClient(ClientsList, .2)

        for (conn, addr) in ClientsList:
            conn.settimeout(.2)
            data = conn.recv(1024)

            if not data:
                print("user sent empty message, exit")
                exit("empty!!!")

            print("user said: " + data.decode('utf-8'))

        if len(ClientsList) > 0:
            toSend = input("let's say to user: ")
            for (conn, addr) in ClientsList:
                conn.send(bytes(toSend, 'utf-8'))

    except socket.timeout:
        pass
