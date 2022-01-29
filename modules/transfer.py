from os import error
import time
import socket

# convert str  utf-8 to bytes
def _strToByte(val: str) -> bytes:
    return bytes(val, 'utf-8')

# send msg through the socket
def send(socket: socket.socket, msg: str) -> bool:
    sent = socket.send(_strToByte(msg))
    return sent > 0

