# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Digite a distância da viagem em Km: "))

# Verifique a distância e calcule o preço da passagem
if distancia <= 200:
    preco_passagem = distancia * 0.50
else:
    preco_passagem = distancia * 0.45

# Exiba o preço da passagem
print(f"O preço da passagem é R$ {preco_passagem:.2f}")


