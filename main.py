a = "_________"
hod = 0
count = 0
q = [x for x in a]
print('---------')
print('| {0} {1} {2} |'.format(q[0], q[1], q[2]))
print('| {0} {1} {2} |'.format(q[3], q[4], q[5]))
print('| {0} {1} {2} |'.format(q[6], q[7], q[8]))
print('---------')

while True:
    b = input()

    z = "".join(b.split())
    if not z.isdigit():
        print("You should enter numbers!")
        continue
    d, c = b.split()
    if not d.isdigit():
        print("You should enter numbers!")
        continue
    else:
        d = int(d)
        c = int(c)

    if d > 3 or c > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    if hod % 2 == 0:
        if d == 1 and c == 1 and q[0] == '_':
            q[0] = 'X'
            hod += 1
        elif d == 1 and c == 2 and q[1] == '_':
            q[1] = 'X'
            hod += 1
        elif d == 1 and c == 3 and q[2] == '_':
            q[2] = 'X'
            hod += 1
        elif d == 2 and c == 1 and q[3] == '_':
            q[3] = 'X'
            hod += 1
        elif d == 2 and c == 2 and q[4] == '_':
            q[4] = 'X'
            hod += 1
        elif d == 2 and c == 3 and q[5] == '_':
            q[5] = 'X'
            hod += 1
        elif d == 3 and c == 1 and q[6] == '_':
            q[6] = 'X'
            hod += 1
        elif d == 3 and c == 2 and q[7] == '_':
            q[7] = 'X'
            hod += 1
        elif d == 3 and c == 3 and q[8] == '_':
            q[8] = 'X'
            hod += 1
        else:
            print("This cell is occupied! Choose another one!")
            continue
        print('---------')
        print('| {0} {1} {2} |'.format(q[0], q[1], q[2]))
        print('| {0} {1} {2} |'.format(q[3], q[4], q[5]))
        print('| {0} {1} {2} |'.format(q[6], q[7], q[8]))
        print('---------')
    elif hod % 2 == 1:
        if d == 1 and c == 1 and q[0] == '_':
            q[0] = 'O'
            hod += 1
        elif d == 1 and c == 2 and q[1] == '_':
            q[1] = 'O'
            hod += 1
        elif d == 1 and c == 3 and q[2] == '_':
            q[2] = 'O'
            hod += 1
        elif d == 2 and c == 1 and q[3] == '_':
            q[3] = 'O'
            hod += 1
        elif d == 2 and c == 2 and q[4] == '_':
            q[4] = 'O'
            hod += 1
        elif d == 2 and c == 3 and q[5] == '_':
            q[5] = 'O'
            hod += 1
        elif d == 3 and c == 1 and q[6] == '_':
            q[6] = 'O'
            hod += 1
        elif d == 3 and c == 2 and q[7] == '_':
            q[7] = 'O'
            hod += 1
        elif d == 3 and c == 3 and q[8] == '_':
            q[8] = 'O'
            hod += 1
        else:
            print("This cell is occupied! Choose another one!")
            continue
        print('---------')
        print('| {0} {1} {2} |'.format(q[0], q[1], q[2]))
        print('| {0} {1} {2} |'.format(q[3], q[4], q[5]))
        print('| {0} {1} {2} |'.format(q[6], q[7], q[8]))
        print('---------')
    print('Enter the coordinates: {0}'.format(b))

    if q[0] == q[3] == q[6] == "X" or q[0] == q[3] == q[6] == "O":
        b = q[0]
        count += 1
    if q[1] == q[4] == q[7] == "X" or q[1] == q[4] == q[7] == "O":
        b = q[1]
        count += 1
    if q[2] == q[5] == q[8] == "X" or q[2] == q[5] == q[8] == "O":
        b = q[2]
        count += 1
    if q[0] == q[1] == q[2] == "X" or q[0] == q[1] == q[2] == "O":
        b = q[0]
        count += 1
    if q[3] == q[4] == q[5] == "X" or q[3] == q[4] == q[5] == "O":
        b = q[3]
        count += 1
    if q[6] == q[7] == q[8] == "X" or q[6] == q[7] == q[8] == "O":
        b = q[6]
        count += 1
    if q[0] == q[4] == q[8] == "X" or q[0] == q[4] == q[8] == "O":
        b = q[0]
        count += 1
    if q[2] == q[4] == q[6] == "X" or q[2] == q[4] == q[6] == "O":
        b = q[2]
        count += 1
    if count >= 1:
        print('---------')
        print('| {0} {1} {2} |'.format(q[0], q[1], q[2]))
        print('| {0} {1} {2} |'.format(q[3], q[4], q[5]))
        print('| {0} {1} {2} |'.format(q[6], q[7], q[8]))
        print('---------')
        print(b, "wins")
        break
    elif ((q.count("X") - q.count("O")) > 1) or ((q.count("O") - q.count("X") > 1) or count > 1):
        print("Impossible")
        break
    elif q[0] == "_" or q[1] == "_" or q[2] == "_" or q[3] == "_" or q[4] == "_" or q[5] == "_" or q[6] == "_" or q[7] == "_" or q[8] == "_" or q[8] == "_":
        print("Game not finished")
    else:
        print("Draw")
        break
