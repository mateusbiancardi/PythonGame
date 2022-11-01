# PythonGame

Primeiro de tudo, é necessário que esteja instalado o Git no computador de vocês.

Depois da instalação, abram o VSCode, cliquem em File e seleciona Open Folder, e selecionem uma pasta vazia. Depois, cliquem em Terminal e cliquem em New Terminal. Esse link explica os principais comandos para utilizar o Git. Mas a princípio, digitem a seguinte sequência:

https://blog.geekhunter.com.br/comandos-git-mais-utilizados/

### Comandos iniciais (talvez o terminal indique alguns comandos para configuração inicial, só fazer o que está pedindo):
- git init                                                                                             //esse comando inicializa o git na pasta
- git clone https://github.com/mateusbiancardi/PythonGame                                              //clona o repositório
- git remote add upstream https://github.com/mateusbiancardi/PythonGame.git                            //nao lembro exatamente oq faz mas executa aí e confia


### Comandos que todos irão utilizar:
- git pull                                                            //baixa automaticamente as atualizações feitas na branch principal pelos outros usuários (executar                                                                         toda vez que for programar)
- git add .                                                           //adiciona todos os arquivos que você alterou
- git commit -m "mensagem explicando a mudança no código"             
- git push                                                            //envia os arquivos para o github