# AULA 01

## Nomeclatura
- Um arquivo .py em python, chamamos de mmódulo.
- Uma pasta dentro do workspace, chamamos de diretório.

1. Cases
``snake_case`` -> Tudo minúsculo, palavras separads por underline.
``cammelCase``  -> Primeira letra da primeira palavra em minúsculo, e toda próxima palavra a primeira letra em maiúsculo.


## Observações
1. Python é uma linguagem fracamente tipada.


# Aula 02

1. Para informar qantas cas decimais você quer após a vírgula, utilizamos o comando ":.2f".

2. Ao dividrmos dois números inteiros, caso seja necessário, ocorre uma conversão implicita [casting].


# Aula 03

1. Em Python, no momento que vamos realizar alguma operaçõa, existe uma precedência.
 Primeiramente, realizamos a * e a /.
 Depois, a + e a -.
Podemos utilizar os () para quebrar ou organizar uma operação.

2. Em Python, toda vez que utilizamos o método `input()`, a entrada automaticamente será do tipo `string`.

3. Para converter uma string para `int` ou `float`, podemos utilizar os métodos `int()` ou `float()`.


# Aula 05
## ESTRUTURAS DE REPETIÇÃO
1. for
=> Voê irá utilizar quando de antemão se sabe a quantidade de vezes a repetição irá acontecer. Normalmente é utilizado ara `iterar` sobre elementos de uma sequência.
1.1 - range() =>  Gera uma sequência de números. (inclusivo, exclusivo).

2. while
=> Será utilizado quando você não sabe ao certo quantas vezes a repetição irá acontecer. Será executado enquanto a condição for verdadeira.

## Atalhos no VScode
``CTRL + B`` => Oculta ou exibe o explorador.
``CTRL + ;`` => Comenta ou descomenta um código.
``CTRL + C`` => Copiar.
``CTRL + V`` => Colar.
``CTRL + Z`` => Desfazer a última alteração.
``SHIFT + ALT + SETA (↑ ou ↓)`` => Duplica a linha.
``CTRL + "`` => Oculta ou exibe o terminal.
``CTRL + D`` => Seleciona a próxima ocorrência.
``ALT + Z`` => Realiza uma quebra e linha.

## Atalhos do Windows
`windows + ç` => Exibe ícones e emotions.

# Relembrando Variavéis 
nome="Marcos Imbiriba"
idade=26
altura=1.75

print("O nome do usuário é:",nome,"e a idade do usuário é", idade)
print(f"O nome do usuário é: {nome}e a idade do usuário é {idade}")
