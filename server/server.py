import socket
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
addr, port = "192.168.1.100", 12345

srvSoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("listening for ", addr, port)
srvSoket.bind((addr, port))
srvSoket.listen(1)
conn, remoteAddr = srvSoket.accept()
conn.send(bytes('Dear somebody, you are at my ct2021 server!!!','utf-8'))

while True:
    try:
        conn.settimeout(.2)
        data = conn.recv(1024)

        if not data:
            print("user sent empty message, exit")
            exit("empty!!!")        

        print("user said: " + data.decode('utf-8'))
        
        toSend = input("let's say to user: ")
        conn.send(bytes(toSend,'utf-8'))
    except socket.timeout:
        pass
