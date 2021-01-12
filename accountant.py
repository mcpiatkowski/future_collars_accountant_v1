#  ACCOUNTANT

#  import sys
command = []
warehouse = {}
history = []
brake_while = ['stop', 'konto', 'magazyn', 'przegląd']
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
    return action


def command_check(values, cash):
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
    return True


while True:

    command = f_command(input())
    check = command_check(command, balance)
    if not check:
        break
    if command[0] in brake_while:
        break
    elif command[0] == 'saldo':
        balance += int(command[1])
    elif command[0] == 'zakup':
        balance -= trade(command[2], command[3])
    elif command[0] == 'sprzedaż':
        balance += trade(command[2], command[3])

    history += [command]

history += [command]
if command[0] == 'konto':
    print("Balance: ", balance)
elif command[0] == 'magazyn':
    for key, amount in warehouse.items():
        print(key, amount)
elif command[0] == 'przegląd':
    print("Historia:")
    for record in history:
        print(record)
elif check:
    for record in history:
        for i in record:
            print(i)
print("")
print("Balance: ", balance)
for key, amount in warehouse.items():
    print(key, amount)