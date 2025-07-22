# Cadastro de um aluno
nome = input("Digite o Seu Nome: ")
print(f"Seja Bem Vindo {nome}")

nota1 = float(input("Digite a sua nota da sua Primeira prova parcelar: "))
nota2 = float(input("Digite a sua nota da sua Segunda prova parcelar: "))
nota3 = float(input("Digite a sua nota do Exame final: "))

total = (nota1 + nota2 + nota3) / 3

if total >= 10:
    print(f"Parabéns {nome}, você Aprovou! Média: {total:.1f}")
else:
    print(f"Que Triste {nome} você Reprovou. Média: {total:.1f}")

#Codigo desenvolvido por: Emanuel João
# Projeto: Cadastro de um aluno
# Este projeto visa aprimorar conhecimentos básicos sobre:
# entrada de dados, variáveis, conversão de tipos,
# operações aritméticas, estrutura condicional e saída formatada.
#22/07/2025
