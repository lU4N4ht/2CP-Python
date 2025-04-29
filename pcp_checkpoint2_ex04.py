nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite o valor desejado do empréstimo: "))
parcelas = int(input("Digite o número de parcelas (de 3 a 24): "))


def verificar_aprovacao(idade, renda, emprestimo, parcelas):
    if idade <= 17:
        print("Idade deve ser maior que 18 anos.")
        return False
    if emprestimo > renda * 15:
        print("Valor solicitado é maior que 15x a renda mensal.")
        return False
    if parcelas < 3 or parcelas > 24:
        print("Número de parcelas deve estar entre 3 e 24.")
        return False
    
    valor_parcela_sem_juros = emprestimo / parcelas
    if valor_parcela_sem_juros < 100 or valor_parcela_sem_juros > 2000:
        print("Empréstimo negado: Valor da parcela deve estar entre R$100 e R$2000.")
        return False
    return True


def calcular_juros(parcelas):
    if parcelas <= 6:
        juros_mensal = 0.05
        print("Taxa de juros: 5% ao mês")
    elif parcelas <= 12:
        juros_mensal = 0.08
        print("Taxa de juros: 8% ao mês")
    else:
        juros_mensal = 0.10
        print("Taxa de juros: 10% ao mês")
    return juros_mensal


def calcular_valores(emprestimo, parcelas, juros_mensal):
    total_juros = emprestimo * juros_mensal * parcelas
    total_com_juros = emprestimo + total_juros
    valor_parcela = total_com_juros / parcelas
    print(f"Total com juros: R${total_com_juros:.2f}")
    print(f"Valor de cada parcela ({parcelas}x): R${valor_parcela:.2f}")
    return total_com_juros, valor_parcela, total_juros



if verificar_aprovacao(idade, renda, emprestimo, parcelas):
    juros_mensal = calcular_juros(parcelas)
    total_com_juros, valor_parcela, total_juros = calcular_valores(emprestimo, parcelas, juros_mensal)
    print(f"Empréstimo aprovado para {nome}!")
    print(f"Valor total com juros: R${total_com_juros:.2f}")
    print(f"Valor de cada parcela ({parcelas}x): R${valor_parcela:.2f}")
    print(f"Total de juros pagos: R${total_juros:.2f}")
    
else:
    print("Empréstimo negado!")