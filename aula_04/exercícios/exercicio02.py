#2. **Verificação de Ingredientes**
#Dado dois conjuntos de ingredientes, `exiba os ingredientes comuns entre eles` e os `que estão disponíveis apenas em um conjunto.`

ingredientes = {"mussarela", "oregáno", "tomate", "calabresa"}

pizza_calabresa = ("tomate", "calabresa", "cebola")
comuns = ingredientes.intersection(pizza_calabresa)
unicos = ingredientes.symmetric_difference(pizza_calabresa)

print("Os ingredientes comuns são:", comuns)
print("Os ingredientes unicos são:", unicos)

