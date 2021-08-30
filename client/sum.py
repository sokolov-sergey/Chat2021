# num = 10 то тебе нужно  посчитать сумму всех чисел от 1 до 10
# 1+2+3+4+5+6+7+8+9+1
list = ['aaaaa','22222','fdfd']
list.count()
for i in list:
    print(i)

i = list.count()-1

while (i >=0):
    print(list[i])
    i=i-1


num = int(input("give a num please"))
result = 0



# объявление цикла
for i in range(1, num+1):
    # Итерация - шаг цикла
    result = result+i
    print("Current value: ", result)

print("FOR result: ", result)

result = 0

while (num > 0):
    result = result + num
    num = num-1

print("WHILE result: ", result)
