AREA = 3


def create_display():
    display = []
    for _ in range(AREA):
        row = []
        for i in range(AREA):
            row.append('-')
        display.append(row)
    return display

def print_display(display):
    for row in display:
        for i,x in enumerate(row):
            if i < 2:
                print(x, end=' | ')
            else: 
                print(x)


def player1(display, cache):
    while True:
        player1_move = int(input("Jugador 1, te toca jugar: "))-1
        if player1_move in cache:
            print("Ya tienes colocada una ficha ahí!")
        else:
            cache.append(player1_move)
            break
    if player1_move < 3:
        display[0][player1_move] = 'O'
    if player1_move >= 3 and player1_move < 6:
        display[1][(player1_move)-3] = 'O'
    if player1_move >= 6 and player1_move < 9:
        display[2][(player1_move)-6] = 'O'
    finish = check_win(display)
    return display, finish

def player2(display, cache):
    while True:
        player2_move = int(input("Jugador 2, te toca jugar: "))-1
        if player2_move in cache:
            print("Ya tienes colocada una ficha ahí!")
        else:
            cache.append(player2_move)
            break
    if player2_move < 3:
        display[0][player2_move] = 'X'
    if player2_move >= 3 and player2_move < 6:
        display[1][(player2_move)-3] = 'X'
    if player2_move >= 6 and player2_move < 9:
        display[2][(player2_move)-6] = 'X'
    finish = check_win(display)
    return display, finish

def check_win(display):
    win = False
    for i,row in enumerate(display):
        symbol = display[i][0]
        count = 0
        for letter in row:
            if symbol != letter or symbol == '-':
                break
            else:
                count += 1
        if count == 3:
            win = True

    for i in range(len(display[0])):
        symbol = display[0][i]
        count = 0
        for x in range(3):
            if symbol != display[x][i] or symbol == '-':
                break
            else:
                count += 1
        if count == 3:
            win = True

    diagonal1 = display[0][0]
    if diagonal1 == display[1][1] and diagonal1 == display[2][2] and diagonal1 != '-':
        win = True

    diagonal2 = display[2][0]
    if diagonal2 == display[1][1] and diagonal2 == display[0][2] and diagonal2 != '-':
        win = True
    
    return win


def main():
    cache_player1 = []
    cache_player2 = []
    display = create_display()
    print_display(display)
    input("Bienvenido a TicTacToe!, presiona enter para jugar!")
    while True:
        display, win = player1(display, cache_player1)
        print_display(display)
        if win == True:
            print("El jugador 1 gana!")
            break
        display, win = player2(display, cache_player2)
        print_display(display)
        if win == True:
            print("El jugador 2 gana!")
            break
    play_again = input("Presiona enter para jugar otra vez ('q' para dejar de jugar): ").lower()
    if play_again == 'q':
        print("Hasta pronto!")
    else:
        main()AREA = 3


def create_display():
    display = []
    for _ in range(AREA):
        row = []
        for i in range(AREA):
            row.append('-')
        display.append(row)
    return display

def print_display(display):
    for row in display:
        for i,x in enumerate(row):
            if i < 2:
                print(x, end=' | ')
            else: 
                print(x)


def player1(display, cache):
    while True:
        player1_move = input("Jugador 1, te toca jugar: ")
        if not player1_move.isdigit:
            continue
        elif player1_move in cache:
            print("Ya hay una ficha colocada ahí")
        else:
            cache.append(player1_move)
            break
    player1_move = int(player1_move)-1
    if player1_move < 3:
        display[0][player1_move] = 'O'
    if player1_move >= 3 and player1_move < 6:
        display[1][(player1_move)-3] = 'O'
    if player1_move >= 6 and player1_move < 9:
        display[2][(player1_move)-6] = 'O'
    finish = check_win(display)
    return display, finish

def player2(display, cache):
    while True:
        player2_move = input("Jugador 2, te toca jugar: ")
        if not player2_move.isdigit():
            continue
        elif player2_move in cache:
            print("Ya hay una ficha colocada ahí")
        else:
            cache.append(player2_move)
            break
    player2_move = int(player2_move)-1
    if player2_move < 3:
        display[0][player2_move] = 'X'
    if player2_move >= 3 and player2_move < 6:
        display[1][(player2_move)-3] = 'X'
    if player2_move >= 6 and player2_move < 9:
        display[2][(player2_move)-6] = 'X'
    finish = check_win(display)
    return display, finish

def check_win(display):
    win = False
    for i,row in enumerate(display):
        symbol = display[i][0]
        count = 0
        for letter in row:
            if symbol != letter or symbol == '-':
                break
            else:
                count += 1
        if count == 3:
            win = True

    for i in range(len(display[0])):
        symbol = display[0][i]
        count = 0
        for x in range(3):
            if symbol != display[x][i] or symbol == '-':
                break
            else:
                count += 1
        if count == 3:
            win = True

    diagonal1 = display[0][0]
    if diagonal1 == display[1][1] and diagonal1 == display[2][2] and diagonal1 != '-':
        win = True

    diagonal2 = display[2][0]
    if diagonal2 == display[1][1] and diagonal2 == display[0][2] and diagonal2 != '-':
        win = True
    
    return win


def main():
    cache = []
    display = create_display()
    print_display(display)
    input("Bienvenido a TicTacToe!, presiona enter para jugar!")
    while True:
        display, win = player1(display, cache)
        print_display(display)
        if win == True:
            print("El jugador 1 gana!")
            break
        display, win = player2(display, cache)
        print_display(display)
        if win == True:
            print("El jugador 2 gana!")
            break
    play_again = input("Presiona enter para jugar otra vez ('q' para dejar de jugar): ").lower()
    if play_again == 'q':
        print("Hasta pronto!")
    else:
        main()
main()
