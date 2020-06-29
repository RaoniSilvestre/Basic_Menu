from arquivo import *
from ex113 import *
from listagem import lista

arq = 'dados.txt'
if ArqExiste(arq):
    print('\033[32mArquivo encontrado com sucesso!\033[30m')
else:
    print('\033[31mArquivo não encontrado.\033[30m')
    CriarArq(arq)
while True:
    titulo( 'MENU PRINCIPAL' )
    lista('Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do sistema')
    lin()
    op = LeiaInt()
    if op == 1:
        sleep(1.5)
        LerArq(arq)
        print('')
    elif op == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq,nome,idade)
        sleep(1.5)
    elif op == 3:
        titulo('Obrigado por usar meu programa.')
        sleep(1.5)
        break
