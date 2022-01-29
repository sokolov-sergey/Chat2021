'''
ch21 Server 
'''
from os import error
import socket
import sys
import modules.proto as proto


def tryNewUserConnect(userConnect: socket, timeout=2):
    try:
        userConnect.settimeout(timeout)
        incomeMsg = userConnect.recv(1024)
        msg = incomeMsg.decode('utf-8')

        # get command list from recieved message
        cmd = proto.splitCommands(msg)
        
        if(proto.connect() in cmd):
            # it's ok, there's connection command. Send response and remove conn command
            userConnect.send(bytes(proto.connectionResult(True), 'utf-8'))
            cmd.remove(proto.connect())

            # return the rest of commands
            return cmd
        else:
            userConnect.send(bytes(proto.connectionResult(False), 'utf-8'))
            return False
    except:
        print("Unable to accept a new user")
        return False


UserId = 1


def acceptClient(serverSocket: socket,clientsList: list, timeout=2):
    try:
        # wait for client timeout seconds
        serverSocket.settimeout(timeout)
        conn, remoteAddr = serverSocket.accept()

        # check connection by protocol
        userConnResult = tryNewUserConnect(conn)
        if(userConnResult == False):
            print("Hacker attack detected")
            conn.close()
            return

        # extract $REG command and user name
        userName = ""
        for x in userConnResult:
            if proto.REG in x:
                userName = x.split(":")[1]

        # user name was not received exit
        if not userName:
            print("Anonim is prohibited")
            conn.close()
            return

        # our client has come, let's welcom him
        conn.send(bytes('Dear '+userName+', you are at my ct2021 server!!!', 'utf-8'))

        # save new client connection to list        
        newUser = (conn, remoteAddr, userName)
        clientsList.append(newUser)
        return newUser
    except socket.timeout:
        # just exit from proc if no new connection was accepted
        pass


def sendBroadcastMessage(fromClient, msg, clientList:list):
    print("BCM Proc")
    for client in clientList:
        try:
            (conn, addr, clientName) = client
            if clientName == fromClient:
                continue
            print("BCM: ", msg)
            conn.send(msg)
        except:
            removeClient(client, clientList)


def removeClient(client, clientList: list):
    if client in clientList:
        (conn, a, name) = client
        conn.close()
        clientList.remove(client)
        print("Client ", name, "was removed from the server")


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
        user = acceptClient(SrvSoket,ClientsList, .2)
        if user:
            UserId = len(ClientsList)+1
            print("a new user connected ", user[2])

        # receive clients messages
        for client in ClientsList:
            try:
                # variable client is a tuple and contains 3 values inside itself
                (conn, addr, clientName) = client

                if conn.fileno() < 0:
                    # a case when a client may send empty
                    print("user sent empty message, remove him from our list")
                    removeClient(client, ClientsList)
                    continue

                try:
                    # receive from a message client and send to all the clients
                    conn.settimeout(.3)
                    clientMsg = conn.recv(1024)
                    
                    if not clientMsg:
                        continue

                    sendBroadcastMessage(fromClient=clientName, msg=clientMsg,clientList=ClientsList)
                except socket.timeout:
                    print(".", end="")
                    continue

                print()
                print(clientName, " said:", clientMsg.decode('utf-8'))
            except ConnectionResetError as ex:
                # client lost connection
                print("Connection with", clientName, "was lost.", ex.strerror)
                removeClient(client, ClientsList)
            except error as err:
                # otheк error occured while procession client
                print('Client will be deleted from server because some error has occured...', err)
                removeClient(client, ClientsList)

        # send message to all clients
        if len(ClientsList) > 0 and ServerInput:
            toSend = input("let's say to users: ")
            for (conn, addr, clientName) in ClientsList:
                conn.send(bytes(toSend, 'utf-8'))

    except socket.timeout:
        pass
