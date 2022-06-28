from functools import reduce

lista = [1, 1.7, 2, 2.5, 3, 3.3]

usandofilter = list(filter(lambda x: type(x)==int, lista))

print(usandofilter)

usandomap = list(map(lambda x: x ** 2, usandofilter))

print(usandomap)

usandoreduce = reduce(lambda x, y: x + y, usandomap)

print(usandoreduce