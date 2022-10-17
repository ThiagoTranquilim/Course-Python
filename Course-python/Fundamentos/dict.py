from pickle import APPEND


pessoa = {'nome': 'Prof(a). Ana', 'idade': '38', 'cursos': ['Ingles', 'Portugues']}
print(type(pessoa))

print(pessoa.keys())
print(pessoa.values())

pessoa = {'nome': 'Prof Alberto', 'idade': '43', 'cursos': ['React', 'Python']}
pessoa['cursos'].append('Angular')
print(pessoa)
