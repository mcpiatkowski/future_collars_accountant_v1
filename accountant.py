#  ACCOUNTANT

#  import sys


def buy(identification, price, amount):
    repeat = False
    #  sprawdzamy czy dodawany produkt znajduje się już w magazynie
    for i in warehouse:
        if i[0] == command[1]:
            repeat = True
            break
    # jeśli tak to dodajemy wskazaną ilość, jeśli nie dodajemy nowy produkt do magazynu
    if repeat:
        i[1] += command[3]
    else:
        warehouse.append([identification, amount])
    return price*amount


#  def sell(identification, price, amount):

balance = 0
warehouse = []
command = []

#  command = [str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]

while command != 'stop':
    command.append(input("Jaką czynność chcesz wykonać? "))
    if command[0] == 'stop':
        break
    if command[0] == 'saldo':
        command.append(int(input("Jaka kwota? ")))
        command.append(str(input("Komentarz: ")))
        balance += int(command[1])
    if command[0] == 'zakup':
        command.append(input("Jaki towar? "))
        command.append(int(input("Jaka cena? ")))
        command.append(int(input("Jaka ilość? ")))
        balance -= buy(command[1], command[2], command[3])
    command = []
    print("Balance: {}$".format(balance))
    print("Cały magazyn: ", warehouse)

#  Komendy z klawiatury
