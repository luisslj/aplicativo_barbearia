import menu



escolha = 0
barbeiro = 0
cliente = 0

while True:
    menu.Clinte_Barbeiro()
    escolha = int(input('Digite uma opção: '))
    if escolha == 1: 
        menu.Menu_Cliente()
        escolha = int(input('Digite uma opção: '))
        print('----Menu de Servisos----')
        menu.Menu_Servisos()
        cliente = int(input('Digite uma opção: '))
        if cliente == 1:
            print('----Escolha do dia da semana----')
            menu.dias_semana()
            cliente = int(input('Digite uma opção: '))
            if cliente == 1:
                print('----Escolha o Horario----')
                menu.horario_Corte()
                print(f'Horario marcado:')
                break    
                  
    elif escolha == 2:
        menu.Menu_Barbeiro()
        escolha = int(input('Digite uma opção: '))
    elif escolha == 3:
        print('Sair do aplicativo')
        break     



