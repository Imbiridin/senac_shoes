"""
Homogêneo -> Aceita apenas um único tipo de dado.
Heterogêneo -> Aceita dados de tipos diferentes.
A estruturas de dados são declaradas com snake_case;
"""

# Declaração Listas []
# Odenadas, mutáveis e hetergêneas

sabores = ["mussarela", "calabresa", "frango com catupiy", "portuguesa"]
dados_pizza = ["mussarela", 26.90, True]
#print("Sabores disponíveis: ", sabores)
#print("Informções da pizza", dados_pizza)


# Operações com Lista
# 1. append() -> Adiciona um novo valor  ao final da lista.
sabores.append("marguerita")
print("Sabores disponíveis: ", sabores)

# 2. remove() -> remove um elemento da lista.
sabores.remove("calabresa")
print("Sabores disponíveis: ", sabores)

# 3. Acessando os elementos.
pizzas = ["mussarela", "calabresa", "frango com catupiy", "portuguesa"]
print(pizzas[0])
print(pizzas[-1])
