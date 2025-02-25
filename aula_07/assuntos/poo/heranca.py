# Pessoa, Professor, Aluno

#Criando a Superclass Pessoa
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def exibir_dados(self):
        return(f"Nome: {self.nome} | Idade: {self.idade} | CPF: {self.cpf}") 
    
#Criando a Subclass Aluno
class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf) # Herda atributos da classe Pessoa.
        self.matricula = matricula
        self.notas = [] # Lista para armazenar notas do aluno.
    
    def adicionar_notas(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def exibir_dados(self):
        return f'''{super().exibir_dados()} | Matricula: {self.matricula}'''

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, salario, disciplina):
        super().__init__(nome, idade, cpf)
        self.salario = salario
        self.disciplina = disciplina

    def exibir_dados(self):
        return f"{super().exibir_dados()} | Salario: R${self.salario} | Disciplina: {self.disciplina}"
#Criando um Aluno
aluno1 = Aluno("Marcos", 27, "167.540.217.56", "2025525")

#Criando um Professor
professor1 = Professor("Carlos", 58, "12356789", "Filosofia", 5000)

#Exibindo as informações
print(aluno1.exibir_dados())
print(professor1.exibir_dados())