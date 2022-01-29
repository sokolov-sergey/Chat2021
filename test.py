
# заголовок
def myFunc(var1:int)->str:
    # тело функции
    res = 'NOL'
    if var1 < 0:
        res = 'Menshe'
    elif var1>0 :
        res = 'Bolshe'
        
    # вщвращаемое значение или выход
    return res


v = 303030
otvet = myFunc(v)
print(otvet)

a = -234234
otvet = myFunc(a)
print(otvet)