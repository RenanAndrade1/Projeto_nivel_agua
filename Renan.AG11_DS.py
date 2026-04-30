from colorama import Fore, Style

mensagens_reservatorio = ["Muito baixo", "Baixo", "Médio", "Alto", "Muito alto"]

def cores(i):
    if i == 0:
        return Fore.RED
    elif i == 1:
        return Fore.YELLOW
    elif i == 2:
        return Fore.GREEN
    elif i == 3:
        return Fore.CYAN
    elif i == 4:
        return Fore.BLUE

for i in range(len(mensagens_reservatorio)):
    cor = cores(i)
    print(cor + mensagens_reservatorio[i])

print(Style.RESET_ALL)