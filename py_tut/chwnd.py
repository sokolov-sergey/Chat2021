from asciimatics.screen import ManagedScreen
import time
import threading

_output = []


def chPrint(msg):
    msgCnt = len(_output)
    msg = time.strftime("%X |") + msg
    _output.insert(0, msg)
    if(msgCnt > 5):
        _output.pop()


def sendMsg(msg: str):
    pass


def chekInput(currIn: str, char: str):
    if(len(currIn) < 80):
        currIn = currIn + char

    return currIn


def start():
    with ManagedScreen() as screen:
        currIn = ""
        lastMsg = ""

        while True:
            keyEv = screen.get_event()
            if keyEv:
                keyCode = keyEv.key_code

                if keyCode == 13:
                    sendMsg(currIn)
                    lastMsg = currIn
                    chPrint(lastMsg)
                    currIn = ""
                    screen.reset()

                if keyCode == screen.KEY_BACK:
                    currIn = currIn[0: -1]

                elif keyCode > 0 and keyCode != 13:
                    currIn = chekInput(currIn, chr(keyCode))

            screen.clear()
            screen.print_at('Chat2021', 0, 0)
            screen.print_at("Message: "+currIn, 0, 1)

            if(len(_output) > 0):
                fullOut = ""
                for outMsg in _output:
                    fullOut = fullOut + outMsg+'\n'

                screen._print_at(fullOut, 0, 3,80)

            screen.refresh()
            time.sleep(0.01)


if __name__ == "__main__":
    start()
