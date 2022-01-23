s = "$werwer$gfdhgdfhdf:qweqwe:qqqq;$dfgdfgdfg$"
l = list(s.split("$"))
l = [x for x in l if "" != x]
res = map(lambda x: "$"+x, l)
print(list(res))


# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))
