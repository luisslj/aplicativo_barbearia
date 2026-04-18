import calendar
from datetime import datetime
import menu

hora_formatada = datetime.now().strftime("%H:%M:%S")
print(hora_formatada)

horaday = datetime.now().strftime("%H:%M:%S")

print(horaday)



print(calendar.month(2026, 3))
  


escolha_barbeiro = 0
hora = [
    '8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00'
]

barbeiros = [{'barbeiro': "Betinho"},
             {'barbeiro': 'Jose Roberto'}
             ]

print(barbeiros[1]['barbeiro'])


def barbeiro():
    print(barbeiros)
    while True:
        escolha_barbeiro = int(input('Escolha o Barbeiro: '))
        if escolha_barbeiro == 1:
            print(barbeiros[0]['barbeiro'])
        elif escolha_barbeiro == 2:
            print(barbeiros[1]['barbeiro'])  
        elif escolha_barbeiro == 0:
            print('Fim de programa')
        break

def horario():
    while True:
        for i in enumerate(hora):
            print(i)
        horarios = int(input('Escolha um horario: '))
        print(hora[horarios])
        print(f'Horario marcado as {hora[horarios]} com o barbeiro')
        break

def app():
    barbeiro()
    horario()


app()


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

