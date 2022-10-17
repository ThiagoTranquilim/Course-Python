print(dir(str))

nome = 'Thiago Tranquilim'
print(nome)

#quando acontece de nome[-1], ele percorrerá a string ao contrario
# : é uado para percorrer uma string apartir de um certo ponto
print(nome[0])
print(nome[6:])
print(nome[0:10])
print(nome[::-1])

frase = 'Python e uma linguagem'
print('Py' in frase)
print(frase.lower())
print(frase.upper())
print(frase.split())


a = '123'
b = 'Thiago'
a.__add__(b)
print(str.__add__(a, b))
