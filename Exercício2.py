## 2 – Cria um Algoritmo (Programa) que leia 3 notas de 4 alunos e retorne:
# 	Média dos alunos
# 	Quem passou
# 	Quem reprovou
# 	Quem ficou em Exame 



aluno1 = [7,6,8]
aluno2 = [6,6,6]
aluno3 = [5,5,5]
n = 3

def media_aluno():
    media_aluno1 = sum(aluno1)/ n
    media_aluno2 = sum(aluno2)/ n
    media_aluno3 = sum(aluno3)/ n
  

    if media_aluno1 >= 7:
        print("Aprovado, sua media foi de: ", media_aluno1)
    elif media_aluno1 >= 6 and media_aluno1 < 7:
        print("Exame, sua media foi de: ", media_aluno1)
    else:
        print("Reprovado, sua media foi de: ", media_aluno1)
    
    if media_aluno2 >= 7:
        print("Aprovado, sua media foi de: ", media_aluno2)
    elif media_aluno2 >= 6 and media_aluno2 < 7:
        print("Exame, sua media foi de: ", media_aluno2)
    else:
        print("Reprovado, sua media foi de: ", media_aluno2)
    
    if media_aluno3 >= 7:
        print("Aprovado")
    elif media_aluno3 >= 6 and media_aluno3 < 7:
        print("Exame, sua media foi de: ",media_aluno3)
    else:
        print("Reprovado, sua media foi de: ", media_aluno3)

media_aluno()





