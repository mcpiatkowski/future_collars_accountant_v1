#  ACCOUNTANT

import sys


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
command = [str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]

#  identification = str(sys.argv[2])
#  price = int(sys.argv[3])
#  amount = int(sys.argv[4])


while command != 'stop':

    if command[0] == 'zakup':
        balance -= buy(command[1], command[2], command[3])

    print("Balance: {}$".format(balance))
    print("Cały magazyn: ", warehouse)

#  Komendy z klawiatury
    command[0] = input("Jaką czynność chcesz wykonać? ")

    if command[0] == 'stop':
        break

    command[1] = input("Jaki towar? ")
    command[2] = int(input("Jaka cena? "))
    command[3] = int(input("Jaka ilość? "))
