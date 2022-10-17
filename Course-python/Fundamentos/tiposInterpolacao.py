from string import Template
nome, idade = 'Ana', 30


#Formas do print funcinar
print('Nome: %s Idade: %d %r %r' % (nome, idade, True, False))
print('Nome: {0} Idade: {1}'.format(nome, idade))
print(f'Nome: {nome} Idade: {idade}')

s = Template('Nome : $nome Idade $idade')
print(s.substitute(nome = nome, idade = idade))
