#3. **Atualizar Cardápio**
#`Crie` um `dicionário para o cardápio` e `adicione um novo sabor com preço`. `Atualize` o preço de um sabor existente e `remova` um sabor do cardápio.

cardapio = {
    "portuguesa": 29.90,
    "calabresa": 27.90,
    "rúcula com tomate seco": 32.90
}

cardapio["mussarela"] = 26.90
cardapio["rúcula com tomate seco"] = 30.90
del cardapio["portuguesa"]

print(cardapio)
