import cores
def LeiaInt():
    while True:
        try:
            inteiro = int ( input ( '\033[32mDigite uma opção: \033[30m' ) )
        except KeyboardInterrupt:
            cores.vermelho ( 'O usuário preferiu não informar valores.' )
        except ValueError:
            cores.vermelho ( 'ERRO! Digite uma opção válida.' )
        except Exception as erro:
            cores.vermelho(f'O erro encontrado foi {erro}, tente novamente.')
        else:
            if 1<= inteiro <=3:
                return inteiro
            else:
                print('\033[31mERRO! Digite uma opção válida.')


def LeiaFloat():
    while True:
        try:
            real = float(input('Digite um número real: '))
        except KeyboardInterrupt:
            cores.vermelho ( 'O usuário preferiu não informar valores.' )
        except ValueError:
            cores.vermelho ( 'ERRO! Digite um número real válido.' )
        else:
            return real

