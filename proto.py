'''
Mодуль функций протокола CH21

Комманды начинаются с $
Ответы команд начинаются с $$

Большими буквами - имя команды, например $REG:user_name или $$CONNECT:REJ
После двоеточия данные, которые нужно передать в команде $REG:user_name (например $REG:Levs16)
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

REG = "$REG"
def regUser(name: str):
    return REG+":"+name


def regUserResult(ok: bool):
    if(ok):
        return "$"+REG+":OK"
    else:
        return "$"+REG+":BUSY"

# -----------------------------------------
# special function to work with messages


def splitCommands(msg: str):
    # we check that there's at least one command $ and no response $$
    if (len(msg) == 0) or ("$" not in msg) or ("$$" in msg):
        return []

    # split the whole msg string on commands separated by $
    l = msg.split("$")

    for x in l:
        # and remove empty element
        if x == "":
            l.remove("")

    if len(l) == 0:
        return []

    return list(map(lambda x: "$"+x, l))

