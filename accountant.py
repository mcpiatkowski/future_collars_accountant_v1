#  ACCOUNTANT

import sys


def trade(price, amount):
    if (command[1] in warehouse) and command[0] == 'zakup':
        warehouse[command[1]] += command[3]
    elif command[1] in warehouse and command[0] == 'sprzedaż':
        warehouse[command[1]] -= command[3]
    else:
        warehouse.update({command[1]: command[3]})
    return price*amount


def grab_command(action):
    action = [action]
    if action[0] == 'zakup' or action[0] == 'sprzedaż':
        action.append(input())
        action.append(int(input()))
        action.append(int(input()))
    elif action[0] == 'saldo':
        action.append(int(input()))
        action.append(str(input()))
    return action

def grab_argv():
    command = []
    if len(sys.argv) == 4:
        command.append(str(sys.argv[1]))
        command.append(int(sys.argv[2]))
        command.append(str(sys.argv[3]))
        if command[0] not in allow:
            return print("Błąd! Nieznana komenda.")
        if balance + command[1] < 0:
            return print("Błąd! Brak środków.")
    elif len(sys.argv) == 5:
        command.append(str(sys.argv[1]))
        command.append(str(sys.argv[2]))
        command.append(int(sys.argv[3]))
        command.append(int(sys.argv[4]))
        if command[0] not in allow:
            return print("Błąd! Nieznana komenda.")
        if command[2] < 0 or command[3] < 0:
            return print("Błąd! Ilość musi być dodatnia.")
    else:
        command.append(str(sys.argv[1]))
    return command


def error(values, cash, stock):
    for i in values:
        if values[0] == 'saldo' and cash + values[1] < 0:
            print("Błąd! Ujemne saldo!")
            return False
        if values[0] != 'saldo' and type(i) == int and i < 0:
            print("Błąd! Ujemne wartości!")
            return False
    if values[0] == 'zakup' and cash - values[2]*values[3] < 0:
        print("Błąd! Nie masz wystarczającej ilości środków")
        return False
    if values[0] == 'sprzedaż' and values[3] > stock[values[1]]:
        print("Błąd! Brak wystarczającej ilości sztuk na magazynie.")
        return False
    return True


command = []
warehouse = {}
history = []
brake_while = ['stop', 'konto', 'magazyn', 'przegląd']
allow = ['konto', 'magazyn', 'przegląd', 'saldo', 'zakup', 'sprzedaż']
balance = 0


while True:

    command = grab_command(input())
    check = error(command, balance, warehouse)
    history += command
    if not check:
        break
    if command[0] in brake_while:
        command = grab_argv()
    if command[0] == 'saldo':
        balance += int(command[1])
    if command[0] == 'zakup':
        balance -= trade(command[2], command[3])
    if command[0] == 'sprzedaż':
        balance += trade(command[2], command[3])
    if command[0] == 'konto':
        print("Balance: ", balance)
    if history[-1] == 'stop':
        stop = history.pop(-1)
        history += command
        history.append(stop)
        break

for record in history:
        print(record)

print("Balance: ", balance)
#elif command[0] == 'magazyn':
#    for item, amount in warehouse.items():
#        print(item, amount)
#elif command[0] == 'przegląd':
#    print("Historia:")
#    for record in history:
#        print(record)
#elif check:
#    for record in history:
#        for i in record:
#            print(i)
