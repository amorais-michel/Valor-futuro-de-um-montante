print('Informe a taxa de juros mensal em formato decimal.\nSe a taxa for de 6% digite 0.06. Se for 1,49% digite 0.0149 \n\n')

montante = 1 #é conveniente usar o valor 1, para o laço while
n = 0

i = float(input("Taxa de juros:"))
print(f'Taxa de juros informada é de {100*i:.2f}% ao mes')

while montante <= 2:
    montante = montante + montante * i # recebe o valor do montante + montante e multiplica-o pelo valor da taxa de juros
    n = n + 1 # itera o numero de meses
    print(f'O montante é igual a {100 * montante:.2f}% após {n} meses')