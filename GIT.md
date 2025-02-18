# PASSO A PASSO PARA A UTILIZAÇÃO BÁSICA DO GIT/GITHUB

1. Ir no github e criar o repositório do projeto;
2. Abrir o diretório do projeo no VScode.
3. Abrir a tela do terminal do VScode (CTRL + J)
4. git init -> Cria o repositório local do projeto na pasta aonde ele está armazenado.
5. Informar as credenciais do git, isso é realizado uma única vez no computador.
-   git config --global user.name "Seu Nome"
-   git config --global user.email "seu_email@example.com"
6. git status -> verifica quais pastas/arquivos foram enviadas para o repositório local.
7. git add . -> Inclui tods os arquivos/pastas no repósitório local.
8. git branch -M main -> Altera o nome da branch atual para main.
9. git commit -m "A informação fica aqui" -> Realiza um novo commit no repositório local.
10. git remote add origin endereço_do_caminho_do_repositorio_remoto -> Comando para realizar a sincronização do repositório local com o remoto.
11. git push -u origin main -> Envia o repositório local para o remoto.
