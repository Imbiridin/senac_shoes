"""
Os conjuntos não são ordenados, são muáveis, Heterogêneos ou Homogêneos
e não permitem elementos duplicados.

"""

# Declaração dos conjuntos
ingredientes = {"mussarela", "calabresa", "tomate", "azeitona", "tomate"}
print("🧀 Ingredientes básicos:", ingredientes)

# Operações com os conjuntos
# Adicionar itens:
ingredientes.add("oregáno")
print("🧀 Ingredientes atuaçizados: ", ingredientes)

# Remover itens:
ingredientes.remove("tomate")
print("🧀 Ingredientes após a remoção:", ingredientes)

# União de conjuntos:
adicionais = {"bacon", "palmito"}
todos_ingredientes = ingredientes.union(adicionais)
print("🍅 Todos os ingredientes:", todos_ingredientes)

# Interseção de conjuntos: Aparece em ambos os conjuntos
pizza_vegana = {"tomate", "azeitona", "rúcula"}
comuns = ingredientes.intersection(pizza_vegana)
print("🥦 Ingredientes comuns:", comuns)
