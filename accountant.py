#  ACCOUNTANT

#  import sys
command = []
warehouse = {}
history = []
balance = 0


def trade(price, amount):
    if (command[1] in warehouse) and command[0] == 'zakup':
        warehouse[command[1]] += command[3]
    elif command[1] in warehouse and command[0] == 'sprzedaż':
        warehouse[command[1]] -= command[3]
    else:
        warehouse.update({command[1]: command[3]})
    return price*amount


def f_command(action):
    action = [action]
    if action[0] == 'zakup' or action[0] == 'sprzedaż':
        action.append(input())
        action.append(int(input()))
        action.append(int(input()))
    elif action[0] == 'saldo':
        action.append(int(input()))
        action.append(str(input()))
    else:
        action[0] = 'stop'
        print("STOP")
    return action


def check_values(values, cash):
    if values[0] == 'saldo' and cash < 0:
        cash -= int(values[1])
        print("Ujemne saldo! Maksymalnie do wypłaty: ", cash)
        return cash
    elif (values[0] == 'zakup' or values[0] == 'sprzedaż') and (values[2] < 0 or values[3] < 0):
        print("Błąd! Cena oraz ilość muszą być dodatnie!")
        return False
    else:
        return cash


while True:

    command = f_command(input())
    print("Aktualna komenda: ", command)

    if command[0] == 'stop':
        break
    elif command[0] == 'saldo':
        balance += int(command[1])
        balance = check_values(command, balance)
    elif command[0] == 'zakup':
        balance -= trade(command[2], command[3])
        print("Balance: ", balance)
        print("Magazyn: ", warehouse)
    elif command[0] == 'sprzedaż':
        balance += trade(command[2], command[3])
        print("Balance: ", balance)
        print("Magazyn: ", warehouse)

    history += [command]

print("Balance: ", balance)
for record in history:
    print("Historia: ", record)

