#  ACCOUNTANT

#  import sys


def trade(identification, price, amount):
    repeat = False
    #  sprawdzamy czy dodawany produkt znajduje się już w magazynie
    for i in warehouse:
        if i[0] == command[1]:
            repeat = True
            break
    # jeśli tak to dodajemy wskazaną ilość, jeśli nie dodajemy nowy produkt do magazynu
    if repeat and command[0] == 'zakup':
        i[1] += command[3]
    elif repeat and command[0] == 'sprzedaż':
        i[1] -= command[3]
    else:
        warehouse.append([identification, amount])
    return price*amount


command = []
brake_while = ['stop', 'konto', 'magazyn', 'przegląd']
warehouse = []
history = []
balance = 0

#  command = [str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]

#  Pierwsza, modyfikująca część programu

while command != 'stop':

    command.append(input())
    print("Komenda: ", command)

    if command[0] in brake_while:
        break
    if command[0] == 'saldo':
        command.append(int(input()))
        command.append(str(input()))
        balance += int(command[1])
        print(command[1:])
        print("Stan konta wynosi {}$.".format(balance))
        if balance <0:
            balance -= int(command[1])
            print("Błąd! Ujemne saldo! Maksymalnie do wypłaty: ", balance)
    elif command[0] == 'zakup' or command[0] == 'sprzedaż':
        command.append(input())
        command.append(int(input()))
        command.append(int(input()))
        if command[2] < 0 or command[3] < 0:
            print("Wartość musi być większa bądź równa zero!")
            continue
        if command[0] == 'zakup':
            balance -= trade(command[1], command[2], command[3])
        else:
            balance += trade(command[1], command[2], command[3])
        print(command[1:])
        print("Stan konta wynosi {}$.".format(balance))
    else:
        print("Błąd! Nieznana komenda! Podsumowanie:")
        break

    history += [command]
    command = []


if command[0] == 'konto':
    print("Stan konta wynosi {}$.".format(balance))
if command[0] == 'magazyn':
    print("Cały magazyn: ", warehouse)
if command[0] == 'przegląd':
    print("Historia zleceń: ")
    for i in history:
        print(i)

print("Stan konta wynosi: {}$.".format(balance))
print("Cały magazyn: ", warehouse)
print("Historia zleceń: ")
for i in history:
    print(i)