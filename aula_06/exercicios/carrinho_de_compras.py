'''
Crie um programa que permita adicionar produtos a um carrinho de compras. O programa deve continuar pedindo produtos até que o usuário digite "finalizar".
No final, exiba todos os produtos comprados.

- O usuário digita o nome do produto e ele é adicionado a uma lista.
- Se o usuário digitar "finalizar", o programa encerra e mostra os produtos comprados.
'''

produtos = ["azeitona", "sardinha", "macarrão", "molho de tomate", "creme de leite"]
print(produtos)
pedido = []
item = ""

while item != "finalizar":
    item = input("\n Digite o nome do produto para adicionar ou 'finalizar' para encerrar: ")
    if item in produtos:
        pedido.append(item)
        print(f"\n Produto adicionado.\n {item}\n Adicionar mais um produto ?: ") 
    elif item.lower() == "finalizar":
        print(f"\n Pedido encerrado! \n - {pedido}")
    else:
        print("\n Não temos esse produto!")
        break

    

