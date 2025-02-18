#Agora, a nossa pizzaria está cobrando uma `taxa fixa de R$5 por entrega`, 
#além de `R$1 por km até 5km,` e `R$2 por km até 10km`. Mais ainda `não entregamos com a distância superior a 10km`.

#Pegando como base essas possibilidades, faça um programa que responda as seguintes perguntas:

#- Quanto Joana irá pagar de frete, sendo que mora a 8km da pizzaria.
#- Quanto Guilherme irá pagar de frete, sendo que mora a 3km da pizzaria.
#- Quanto Rafael irá pagar de frete, sendo que mora a 11km da pizzaria.


distancia = float(input("Informe em KM a distância da sua casa: "))
taxa_fixa = 5
valor_frete = 0

if(distancia <= 5):
    valor_frete = (distancia*1)+taxa_fixa
    print(f"O valor da entrega é de {valor_frete} reais.")
elif(distancia <= 10):
    valor_frete = (distancia*2)+taxa_fixa
    print(f"O valor da entrega é de {valor_frete} reais.")
else:
    print("Não atendenmos a sua localidade")


#RESULTADO

TAXA = 5

distancia = int(input("Informe em KM a distância da sua casa: "))
valor_menor_5 = 1
valor_menor_10 = 2

if distancia <= 5:
    frete = TAXA + (distancia * valor_menor_5)
    print(f"O valor do frete é de R${frete}")
elif distancia <= 10:
    frete = TAXA + (distancia * valor_menor_10)
    print(f"O valor do frete é de R${frete}")
else:
    print("Infelizmente não entregamos nessa distância.")
