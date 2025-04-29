nome = input("Nome do funcionário: ")

print("Cargo: 1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário")

cargo = int(input("Digite o número do cargo: "))
salario_base = float(input("Salário base: R$ "))
horas_extras = int(input("Total de horas extras trabalhadas: "))
faltas = int(input("Total de faltas no mês: "))
recebeu_bonus = input("Recebeu bônus por desempenho? (s/n): ").lower()

valor_hora_extra = 0.015 * salario_base * horas_extras
desconto_faltas = 0.02 * salario_base * faltas

if recebeu_bonus == 's':
    if cargo == 1:
        bonus = 1000
    elif cargo == 2:
        bonus = 500
    elif cargo == 3:
        bonus = 300
    elif cargo == 4:
        bonus = 100
    else:
        bonus = 0
else:
    bonus = 0

salario_bruto = salario_base
total_acrescimos = valor_hora_extra + bonus
total_descontos = desconto_faltas
salario_final = salario_bruto + total_acrescimos - total_descontos

print("\n--- RESUMO SALARIAL ---")
print(f"Nome: {nome}")
print(f"Salário base: R$ {salario_base:.2f}")
print(f"Total de horas extras: R$ {valor_hora_extra:.2f}")
print(f"Bônus: R$ {bonus:.2f}")
print(f"Descontos por faltas: R$ {desconto_faltas:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")