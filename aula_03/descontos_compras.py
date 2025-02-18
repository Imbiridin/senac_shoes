#A conta da Mariana, cliente da pizzaria Sabores, `ficou no valor de R$ 120` e ela quer saber se tem direito a desconto.
#Tendo como base o valor do pedido, `escreva um programa que verifique se ela tem direito ao desconto.`

#Use:
#10% para pedidos acima de R$ 50.`
#20% para pedidos acima de R$ 100.`

desconto_50 = 10
desconto_100 = 20
pedido_cliente = int(input("Digite o valor do pedido: "))

if pedido_cliente >= 100:
    desconto = (desconto_100 / 100) * pedido_cliente
    print (f"O desconto do pedido é de {desconto}.")
elif pedido_cliente >= 50:
    desconto = pedido_cliente * (desconto_50/100)
    print (f"O desconto do pedido é de {desconto}.")
else:
    print("Não tem desconto para esse valor.")

