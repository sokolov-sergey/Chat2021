from asciimatics.screen import ManagedScreen
import asciimatics.event as events
import time
import threading

_output = []
_screenLock = threading.Lock()

def chPrint(msg):
    msgCnt = len(_output)
    msg = time.strftime("%X |") + msg
    _output.insert(0, msg)
    if(msgCnt > 5):
        _output.pop()


def sendMsg(msg: str):
    pass

def printMessages(_output, screen:ManagedScreen):
    while True:
        if(len(_output) > 0):
            fullOut = ""
            for outMsg in _output:
                fullOut = fullOut + outMsg+'\n'
         
        time.sleep(.5)
                


def chekInput(currIn: str, char: str):
    if(len(currIn) < 80):
        currIn = currIn + char

    return currIn



def start():
    with ManagedScreen() as screen:
        currIn = ""
        lastMsg = ""
        msgThread = threading.Thread(target=printMessages, args=(_output, screen))
        msgThread.start()

        while True:
            keyEv = screen.get_event()
            if keyEv and isinstance(keyEv, events.KeyboardEvent):
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

            # printMessages(_output, screen)
            # if(len(_output) > 0):
            #     fullOut = ""
            #     for outMsg in _output:
            #         fullOut = fullOut + outMsg+'\n'
            
            screen._print_at(_output, 0, 3,80)            
            screen.refresh()
            
            time.sleep(0.03)


if __name__ == "__main__":
    start()
