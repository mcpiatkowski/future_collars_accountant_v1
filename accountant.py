#  ACCOUNTANT

import sys

command = []
warehouse = {}
history = []
balance = 0
print_history = ['saldo', 'zakup', 'sprzedaż']
argv_break = ['przegląd', 'saldo', 'zakup', 'sprzedaż', 'konto', 'magazyn']
allow = 0

def trade(price, amount):
    if (command[1] in warehouse) and command[0] == 'zakup':
        warehouse[command[1]] += command[3]
    elif command[1] in warehouse and command[0] == 'sprzedaż':
        warehouse[command[1]] -= command[3]
    else:
        warehouse.update({command[1]: command[3]})
    return price*amount


def product_check():
    for item in command[1:]:
        try:
            print('{}: {}'.format(item, warehouse[item]))
        except KeyError:
            print('{}: 0'.format(item))


def summary():
    for index in range(int(command[1]), int(command[2])+1):
        for action in history[index]:
            print(action)


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
    if len(sys.argv) == 1:
        return command
    if sys.argv[1] == 'magazyn':
        command.append(str(sys.argv[1]))
        for item in range(2, len(sys.argv)):
            command.append(str(sys.argv[item]))
        return command
    if sys.argv[1] == 'przegląd':
            command.append(str(sys.argv[1]))
            command.append(int(sys.argv[2]))
            command.append(int(sys.argv[3]))
    if sys.argv[1] == 'saldo':
        command.append(str(sys.argv[1]))
        command.append(int(sys.argv[2]))
        command.append(str(sys.argv[3]))
        if balance + command[1] < 0:
            return print("Błąd! Brak środków.")
    elif sys.argv[1] == 'zakup' or sys.argv[1] == 'sprzedaż':
        command.append(str(sys.argv[1]))
        command.append(str(sys.argv[2]))
        command.append(int(sys.argv[3]))
        command.append(int(sys.argv[4]))
        if command[2] < 0 or command[3] < 0:
            return print("Błąd! Ilość musi być dodatnia.")
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'konto':
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


def argv_error():
    if sys.argv[1] == 'przegląd' and len(sys.argv) < 4:
        print("Błąd! Za mało argumentów.")
        return False
    if sys.argv[1] == 'saldo' and len(sys.argv) < 4:
        print("Błąd! Za mało argumentów.")
        return False
    elif (sys.argv[1] == 'zakup' or sys.argv[1] == 'sprzedaż') and len(sys.argv) < 5:
        print("Błąd! Za mało argumentów.")
        return False
    elif sys.argv[1] not in argv_break:
        print("Błąd! Za mało argumentów.")
        return False
    return True


while True:
    command = grab_command(input())
    check = error(command, balance, warehouse)
    history += [command]
    if not check:
        break
    if command[0] == 'stop':
        argv_check = argv_error()
        if argv_check == False:
            break
        command = grab_argv()
        if len(sys.argv) == 1:
            allow = 1
            break
        if command[0] in print_history:
            allow =1
    if command[0] == 'saldo':
        balance += int(command[1])
    if command[0] == 'zakup':
        balance -= trade(command[2], command[3])
    if command[0] == 'sprzedaż':
        balance += trade(command[2], command[3])
    if command[0] == 'konto':
        print("Balance: ", balance)
    if command[0] == 'magazyn':
        product_check()
    if command[0] == 'przegląd':
        summary()
    if history[-1] == ['stop']:
        stop = history.pop(-1)
        history += [command]
        history.append(stop)
        break

if allow == 1:
    for index in history:
        for action in index:
            print(action)