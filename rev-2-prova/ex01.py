musculacao = {"Ana", "Bruno", "Carlos", "Daniela"}
funcional = {"Carlos", "Eduarda", "Fernanda", "Bruno"}
alunos = {}

alunos["ambas"] = musculacao & funcional
alunos["musculacao"] = musculacao - funcional
alunos["funcional"] = funcional - musculacao
alunos["unicos"] = musculacao | funcional

print(alunos["ambas"])
print(alunos["musculacao"])
print(alunos["funcional"])
print(alunos["unicos"])