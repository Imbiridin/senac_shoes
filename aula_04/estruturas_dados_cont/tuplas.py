"""
As tuplas são coleções ordenadas, porém são imutáveis.
Homogêneas e podem ser Heteroêneas

"""

# Declação da tuplas

tamanhos = ("pequena", "média", "grande")
print(f"""
    🤳 Tamanhos disponíveis: {tamanhos}
""")


# Operações com tuplas
#Acessar itens
print("🍕 Tamanho médio:", tamanhos[1])

# Verificar itens
print("✅  Existe tamanho grande?", "grande" in tamanhos)
