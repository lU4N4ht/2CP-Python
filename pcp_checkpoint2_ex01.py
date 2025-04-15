## Entrada:
# Código do estado de origem da carga (número inteiro de 1 a 5)
# Peso da carga em toneladas 
# Código da carga (inteiro entre 10 e 40)
# 
## Saída esperada:
# Peso da carga do caminhão em quilos
# Preço da carga do caminhão
# Valor do imposto com base no preço da carga e do estado de origem
# Valor total (carga + impostos)
# #


estado_origem = int(input("Informe o código do estado de origem da carga [1 a 5]: "))

if estado_origem not in [1, 2, 3, 4, 5]:
    print("O código de estado de origem de carga deve ser entre 1 e 5.")
else:
    peso_tonelada = float(input("Informe o peso da carga em toneladas: "))

    codigo_carga = int(input("Informe o código da carga [10 a 40]: "))

    if codigo_carga < 10 or codigo_carga > 40:
            print("O código da carga deve ser entre 10 e 40.")

    else:
         peso_quilo = peso_tonelada * 1000

         if(codigo_carga > 9 and codigo_carga < 21):
              preco_quilo = peso_quilo * 100.0

         elif(codigo_carga > 20 and codigo_carga < 31):
                    preco_quilo = peso_quilo * 250.0
         else:
                 preco_quilo = peso_quilo * 340.0
        
         if(estado_origem == 1):
             imposto = 0.35

         elif(estado_origem == 2):
               imposto = 0.25

         elif(estado_origem == 3):
                imposto = 0.15

         elif(estado_origem == 4):
                imposto = 0.05
         else:
               imposto = 0
        
         valor_total = (preco_quilo * imposto) + preco_quilo

         print(f"Peso da carga em quilos: {peso_quilo}.")
         print(f"Preço da carga: {preco_quilo}.")
         print(f"Valor do imposto: {imposto}.")
         print(f"Valor total transportado: {valor_total}.")
         
