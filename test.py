def parseUserMessage(msg:str)->list:
    msgFromUser = msg
    split = msgFromUser.split(':')
    return split
    

print(parseUserMessage("$$MESSAGE:USER:HHMMSS:INCOMING"))



'''
print(parseUserMessage(""))
print(parseUserMessage("A:B:C"))

'''