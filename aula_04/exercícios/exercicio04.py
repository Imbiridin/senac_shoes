#4. **Controle de Estoque**
#`Crie` um `dicionário com os estoques` de cada sabor. `Decremente` o estoque conforme os pedidos feitos e exiba uma `mensagem se o estoque acabar.`

estoque = {
    "calabresa": 10,
    "mussarela": 8,
    "portuguesa": 10
}

pedido = ["mussarela", "calabresa", "calabresa"]


for sabor in pedido:
    estoque[sabor] = estoque[sabor] -1

print(estoque)
