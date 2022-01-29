from os import error

import time

import socket


# convert str  utf-8 to bytes

def _strToByte(val: str) -> bytes:

    return bytes(val, 'utf-8')


# send msg through the socket
def send(sok: socket.socket, msg: str) -> bool:
    sent = sok.send(_strToByte(msg))
    return sent > 0

# receive a message from Sok and return as a string
def recv(sok: socket.socket) -> str:
    resp = sok.recv(1024)
    return resp.decode('utf-8')