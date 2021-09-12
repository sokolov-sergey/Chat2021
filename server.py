import socket
import sys
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


UserId = 1


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
        userName = "userId: "+str(UserId)
        newUser = (conn, remoteAddr, userName)
        clientsList.append(newUser)
        return newUser
    except socket.timeout:
        # just exit from proc if no new connection was accepted
        pass


########################################################################
###################### Main server program starts below ################
########################################################################

Addr, Port = "192.168.1.100", 12345
SrvSoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientsList = []

# server can/cannot use input to send broadcast msg
ServerInput = False

if len(sys.argv) > 1:
    ServerInput = sys.argv[1].upper() == "I"


print("listening for ", Addr, Port)
SrvSoket.bind((Addr, Port))
SrvSoket.listen(30)

# main loop
while True:
    try:
        # check for new connection
        user = acceptClient(ClientsList, .2)
        if user:
            UserId = len(ClientsList)+1
            print("a new user connected ", user[2])

        # receive clients messages
        for client in ClientsList:
            try:
                (conn, addr, clientName) = client
                conn.settimeout(.1)
                data = conn.recv(1024)

                if not data or conn.fileno() < 0:                    
                    print("user sent empty message, remove him from our list")
                    ClientsList.remove(client)
                    continue

                print()
                print(clientName, " said:", data.decode('utf-8'))
            except socket.timeout:
                print(".", end="", flush=True)
                pass

        # send message to all clients
        if len(ClientsList) > 0 and ServerInput:
            toSend = input("let's say to users: ")
            for (conn, addr, clientName) in ClientsList:
                conn.send(bytes(toSend, 'utf-8'))

    except socket.timeout:
        pass
