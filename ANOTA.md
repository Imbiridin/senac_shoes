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

# Aula 06
## COMANDOS DE DESVIO
1. continue -> significa continuar, basicamente se uma condição for favorável, ela será desconsiderada.

2. break -> Significa quebrar, quando utilizado irá finalizar o loop mais próximo.

## FUNÇÕES
=> É um bloco de código que é reutilizável. Serve para deixar o código organizado e eficiente. `Executam uma tarefa específica.`

# Aula 07
## PRINCÍPIOS DA PROGRAMAÇÃO ORIENTADA A OBJETOS (P.O.O.)
1. ENCAPSULAMENTO
2. HERANÇA -> É um conceito de P.O.O. que um classe herde atributos e métodos de outra, evitando a repetição de código.
3. POLIMORFISMO
4. ABSTRAÇÃO

## PALAVRAS RESERVADAS EM P.O.O.
1. `class` -> É uma palavra-chave em python onde você cria um `molde`. Toda classe pode ter atibutos e métodos, sendo que os atributos precisam estar dentro de um método chamado construtor (__init__).
2. `object` -> É um nome dado a cada `cópia` criada da classe. ambém conhecido como instância.
3. `__init__` -> É um inicializador(construtor) onde você informa que toda cópia precisa passar aqueles valores no momento da criação. É um método especial.
4. `self` -> Referencia o atributo atual da classe(valor).

## TERMOS UTILIZADOS EM P.O.O.
1. método -> É uma função que está dentro de uma classe. É uma ação.
2. atributo -> São as características de uma classe. 

## HERANÇA
Teremos 2 tipos de classes: 
- superclass -> É a classe pai, é a que oferece a herança.
- subclass -> É a classe filha, que herda a herança. 



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
