'''
Considerando la siguiente función python:

def my_func(r, n):
for i in xrange(n): r = hashlib.sha1(r[:9]).hexdigest()
return r

calcular el valor de:
my_func("0123456789012345678901234567890123456789", 9999999999999999)

Algunos ejemplos concretos de la función:
my_func("0123456789012345678901234567890123456789", 0) = 0123456789012345678901234567890123456789
my_func("0123456789012345678901234567890123456789", 1) = 9a7149a5a7786bb368e06d08c5d77774eb43a49e
my_func("0123456789012345678901234567890123456789", 2) = 747c9a467f90021e5d213e2f6d27ccf82e25d0c9
my_func("9a7149a5a7786bb368e06d08c5d77774eb43a49e", 1) = 747c9a467f90021e5d213e2f6d27ccf82e25d0c9
my_func("0123456789012345678901234567890123456789", 2017) = ec6f690bfd70d46bb0e29237e796e2c34d8e7ad3

'''

import hashlib


def my_func(r, n):
    lista_hash = []
    conj = set()

    global listado
    # caso trivial
    if n == 0:
        return r

    for i in range(n):
        r = hashlib.sha1(r[:9].encode('utf8')).hexdigest()
        if r not in conj:  # pertenencia en conjuntos es mucho mas veloz
            lista_hash.append(r)
            conj.add(r)

        else:
            break

    indice = lista_hash.index(r)
    if n < len(lista_hash):
        return lista_hash[n]
    else:
        lista_repetidos = lista_hash[indice:]
        direccion = (n - indice - 1) % len(lista_repetidos)  # posible bug

        listado = lista_hash  # for debug

        return lista_repetidos[direccion]
