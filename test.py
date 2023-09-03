def retorna_tupla(*args, **kwargs):
    return args, kwargs


valor = retorna_tupla(1, 2, 3, asdf='caio')

print(valor)


lista = [1, 2, 3, 4]

lista_com_dobro = [x * 2 for x in lista if x % 2 == 0]

teste_lamdba = lambda x: x * 2

print(teste_lamdba(2))

print(lista_com_dobro)

print(tuple(map(lambda x: x * 2, lista)))