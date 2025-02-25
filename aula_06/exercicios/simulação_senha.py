'''
Crie um sistema que peça para o usuário digitar uma senha para acessar sua conta bancária. Ele tem **apenas 3 tentativas** para acertar a senha correta.
 Se ele errar as 3 vezes, o sistema bloqueia a conta.

- A senha correta é `"1234"`.
- O usuário tem **até 3 tentativas** para acertar.
- Se errar as 3 vezes, exiba "🚫 Conta bloqueada!".
'''

senha = 1234
erro = 3
tentativas = int(input("\nDigite a sua senha: "))

if tentativas == senha:
    print("Senha correta!")
else:
        
      while tentativas != senha:
        erro -= 1  
        if erro <= 0:          
            print("Conta bloqueada!")
            break
        elif tentativas == senha:
         print("Senha correta!")   
        else: 
            print(f"Senha incorreta!\n O numero de tentativas é de {erro}.")
        tentativas = int(input("Digite novamente: "))
print("Senha correta!")
