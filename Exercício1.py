#Última Aula

# São 3 exercícios de revisão

# 1 – Crie um Algoritmo (Programa) que leia 7 números e retorne o seguinte:
# 	Soma total dos números
# 	Menor número
# 	Maior número ‘



numeros = [1,2,3,4,5,6,7]

def soma():
    soma = sum(numeros)
    print("A soma dos valores é: ",soma)
soma()

def menor_valor():
    menor_valor = min(numeros)
    print("O menor valor da lista é: ",menor_valor)
menor_valor()

def maior_valor():
    maior_valor = max(numeros)
    print("O maior valor da lista é: ",maior_valor)
maior_valor()



