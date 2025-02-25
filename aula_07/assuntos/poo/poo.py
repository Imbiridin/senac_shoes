# aluno -> nome, idade, endereço, cpf
class Aluno: # utilizamos o padrão PascalCase para Classes.
     
    def __init__(self, nome, idade, endereco, cpf):
        self.nome = nome 
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.matriculado = True # default, toda cópia da classe Aluno vai ter essa característica.
    
    #Método que altera o status da matricula do aluno
    def situacao(self):
         if self.matriculado == True:
             self.matriculado = False
         elif self.matriculado == False:
             self.matriculado == True
    
    #Método que exibe as informações do aluno
    def exibir_info(self):
        print(f"""
            DADOS DO ESTUDANTE
         👨‍🎓 O nome do(a) aluno(a) é {self.nome}
            A idade do(a) aluno(a) é {self.idade}
            O endereço do(a) aluno(a) é {self.endereco}
            O cpf do(a) aluno(a) é {self.cpf}
        """)
     
    
# Criando cópias da classe Aluno(instanciação)
a1 = Aluno("Marcos", 27, "Rua 0", "854.674.215-37")
a2 = Aluno("Patricia", 32, "Rua 84", "254.931.785-79")

a1.exibir_info()