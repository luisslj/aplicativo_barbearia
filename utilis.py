import calendar
import datetime

agora = datetime.datetime.now()

ano = agora.year
mes = agora.month
dias = []
escolha1 = 0 #escolha do dia
escolha2 = 0 #escolha da hora
escolha3 = 0 #escolha do barbeiro

horas = [
    '8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00',
    '12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30',
    '17:00','17:30','18:00'
]

barbeiros = [ 'Betinho', 'Jose','Vinicios']


def calendario(dia): # Função para escolhar o dia do mês
    print(calendar.month(ano, mes))
    cal = calendar.monthcalendar(ano, mes)
    for semana in (cal):
        for dia in (semana):
            if dia != 0:
                dias.append(dia)
    escolha1 = int(input('Digite o dia: '))
    dia = dias[escolha1 -1]
    return dia

# Retorna um número de 0 (segunda-feira) até 6 (domingo)   #codigo para fazer validação de final de semana 
#dia = calendar.weekday(2026, 4, 18)
#print(dia)  # 5 → sábado

def horario(hora): #função para escolha das horas 
    cont = 0
    for i in (horas):
        cont += 1 
        print(f'{cont} -> {i}')
    escolha2 = int(input('Digite a hora desejada: '))
    hora = horas[escolha2 -1]
    return hora

def escolha_barbeiro(barbeiro):
    cont1 = 0
    for i in (barbeiros):
        cont1 += 1
        print(f'{cont1} -> {i}')
    escolha3 = int(input('escolha o barbeiro: '))
    barbeiro = barbeiros[escolha3 - 1]
    return barbeiro


#barbeiro1 = escolha_barbeiro(escolha3)
#dia_escohido = calendario(escolha1)
#hora_escolhida = horario(escolha2)
#print(f'Agendado para o dia {dia_escohido} as {hora_escolhida} com o barbeiro {barbeiro1}')