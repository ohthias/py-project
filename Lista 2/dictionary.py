aluno = {
    "nome": "Lucas",
    "matricula": 123456,
    "curso": "Engenharia de Software",
    "notas" : [8.5, 9.0, 7.5]
}

print("Nome do aluno:", aluno["nome"], "Matrícula:", aluno["matricula"])
media = sum(aluno["notas"])/len(aluno["notas"])

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

print("Média:", media)