'''TUPLAS'''
# Tuplas são utilizadas para armazenamento de dados assim como as listas com uma diferença as tuplas
# são objetos imutaveis que não mudam seus valores. EX

tupla = (1, 2, 3, 4, 'banana')
print(tupla)

# Sendo um valor imutavel não tem funções built-in para uso nas tuplas, mais uma tupla pode se tornar uma lista

lista = list(tupla)

print(lista)

# As tuplas aceitam fatiamentos,criação de lista dentro delas e outros mesmo sendo imutavel.

print(tupla[2])  # Seleção por indice
print(tupla[::-1])  # Fatiamento


'''DICIONARIOS'''
# Os dicionarios são utilizados para armazena dados imutaveis porem a diferença é que eles nao alocam objetos e sim valores e sua forma é baseada em keys no caso chave e valor. EX

dicionario = {'nome':'Wendell', 'sobrenome':'Barcelos', 'idade':30}


