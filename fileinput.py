def add_to_command(input_from_file, command):
    if input_from_file[0] == 'zakup' or input_from_file[0] == 'sprzedaz':
        command.append(input_from_file[0])
        command.append(input_from_file[1])
        command.append(int(input_from_file[2]))
        command.append(int(input_from_file[3]))    
    elif input_from_file[0] == 'saldo':
        command.append(input_from_file[0])
        command.append(int(input_from_file[1])) 
        command.append(input_from_file[2])
    elif input_from_file[0] == 'stop':
        command.append(input_from_file[0])


def delete_from_input(input_from_file):
    if input_from_file[0] == 'zakup' or input_from_file[0] == 'sprzedaz':
        for count in range(4):
            del input_from_file[0]
    elif input_from_file[0] == 'saldo':
        for count in range(3):
            del input_from_file[0]
    elif input_from_file[0] == 'stop':
        del input_from_file[0]


def grab_input(input_from_file):
    with open('in.txt') as input_txt:
        for line in input_txt:
            line = line.strip()
            input_from_file.append(line)


def grab_command(input_from_file, command):
    if input_from_file[0] == 'saldo':
        add_to_command(input_from_file, command)
        delete_from_input(input_from_file)
    elif input_from_file[0] == 'zakup' or input_from_file[0] == 'sprzedaz':
        add_to_command(input_from_file, command)
        delete_from_input(input_from_file)
    elif input_from_file[0] == 'stop':
        add_to_command(input_from_file, command)
        delete_from_input(input_from_file)