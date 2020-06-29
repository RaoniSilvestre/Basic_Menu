def lista(*lst):
    cont = 1
    for item in lst:
        print(f'\033[33m{cont} - \033[34m{item}\033[30m')
        cont += 1