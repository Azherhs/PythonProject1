c = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
table = (f'''---------
                | {c[0]} {c[1]} {c[2]} |
                | {c[3]} {c[4]} {c[5]} |
                | {c[6]} {c[7]} {c[8]} |
                    ---------''')
print(table)
while True:
    x = input("Enter the coordinates: ").replace(' ', '')
    if not x[1].isdigit() or not x[1].isdigit():
        print("You should enter numbers!")
        continue

    elif x[0] not in '123' or x[1] not in '123' or len(x) > 2:  # Проверка ввода
        print("Coordinates should be from 1 to 3!")
        continue

    else:
        coordinate = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]  # координаты типа
        for i, n in enumerate(coordinate):   # Финты ушами
            if x == n:
                x = i
        if c[x] != " ":
            print("This cell is occupied! Choose another one!")
            continue

        else:
            if c.count('X') > c.count('O'):
                c[x] = "O"

            else:
                c[x] = "X"

            A = c[0] + c[1] + c[2]
            B = c[3] + c[4] + c[5]
            C = c[6] + c[7] + c[8]
            D = c[0] + c[3] + c[6]
            E = c[1] + c[4] + c[7]
            F = c[2] + c[5] + c[8]
            G = c[0] + c[4] + c[8]
            H = c[2] + c[4] + c[6]

            win = (A, B, C, D, E, F, G, H)


            if "XXX" in win:
                print(table)
                print('X wins')
                break

            elif "OOO" in win:
                print(table)
                print('O wins')
                break

            elif ("XXX" or "OOO" not in win) and c.count(' ') == 0:
                print(table)
                print('Draw')
                break

            else:
                print(table)
                continue
