from cabeçalho import *
from time import sleep


def ArqExiste(nome):
    try:
        a = open ( nome, 'rt' )
        a.close ()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArq(nome):
    try:
        a = open ( nome, 'wt+' )
        a.close ()
    except:
        print ( '\033[31mHouve um erro ao criar o arquivo\033[30m' )
    else:
        print ( f'\033[32mArquivo {nome} criado com sucesso!\033[30m' )


def LerArq(nome):
    try:
        a = open ( nome, 'rt' )
    except:
        print ( '\033[31mErro ao ler o arquivo.\033[30m' )
    else:
        titulo ( 'PESSOAS CADASTRADAS' )
        print ( '{:<40}{}'.format ( 'NOME', ' IDADE' ) )
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')
        sleep ( 1 )
    finally:
        a.close ()


def cadastrar(arquivo,nome,idade):
    try:
        a = open ( arquivo, 'at' )
    except:
        print ( '\033[31mErro ao abrir o arquivo.\033[30m' )
    else:
        a.write ( f'{nome};{idade}\n' )
        print ( f'Novo registro de {nome} adicionado.' )
        a.close ()
