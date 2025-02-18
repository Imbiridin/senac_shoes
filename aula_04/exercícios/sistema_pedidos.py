# Cardápio da pizzaria
cardapio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frabgo com catupiry": 29.90
}

# Pedido inicial do cliente
pedido = []
pedido.append("mussarela")
pedido.append("calabresa")

# Calcular o total do pedido do cliente
total = sum(cardapio[sabor] for sabor in pedido)

# Resumo do pedido
print(" Resumo do pedido")
for sabor in pedido: 
    print(f" 🍕 - {sabor}: R${cardapio[sabor]:.2f}")
print(f"Total: R${total:.2f}")