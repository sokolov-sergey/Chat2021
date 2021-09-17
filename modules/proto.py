# модуль функций протокола CH21
'''
Комманды начинаются с $
Ответы команд начинаются с $$
Большими буквами - имя команды, например $REG:user_name или $$CONNECT:REJ

После двоеточия

данные, которые нужно передать в команде $REG:user_name (например $REG:Levs16)
результат выполнения команды $$CONNECT:REJ
$$ERROR:error_message - ошибка и ее описание

$CONNECT - команда для подсоединения к серверу
$$CONNECT:OK - удачно
$$CONNECT:REJ - ошибка, соединение не удалось

$DISCONNECT

$REG:user_name - регистрация на сервере 
$$REG:OK - ок 
$$REG:BUSY - занято имя
'''

'''
Комманда для подключения
'''


def connect():
    return "$CONNECT"


def connectionResult(ok: bool):
    if(ok == True):
        return '$$CONNECT:OK'
    else:
        return '$$CONNECT:REJ'


def disconnect():
    return '$DISCONNECT'


def regUser(nick: str):
    return "$REG:"+nick
