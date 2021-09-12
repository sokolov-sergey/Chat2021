l = [1,2,3,4,"2352354", None]

def add(list:list):
    print('len before: ',len(list))
    list.append(object())
    print('len after append: ',len(list))
    



add(l)

print('len at the end: ',len(l))
