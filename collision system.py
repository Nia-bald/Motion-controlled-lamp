import time
boundary = [['#', '#', '#', '#', '#', '#', '#', '#', '#','#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#','#', '#', '#', '#', '#', '#', '#', '#', '#']]


def insert(object, xcord, ycord):
    global boundary
    boundary[int(ycord)][int(xcord)] = object


zom = 'O'
insert(zom, 1, 4)


def motion(object, ydir, xdir):
    global boundary

    state = ''
    x = 10000
    y = 10000
    u = 1
    while True:
        if (ydir.upper() == 'S' and xdir.upper() == '') or state == 'W ':
            state = 'S '
            while True:
                for i in range(len(boundary)):
                    for j in boundary[i]:
                        print(j, end="")

                    print()

                for o in boundary:
                    if object in o:
                        x = o.index(object)
                        y = boundary.index(o)



                if boundary[y + 1][x] == '#':
                    break
                else:
                    boundary[y + 1][x] = object
                    boundary[y][x] = " "
                time.sleep(u)

        if (ydir.upper() == 'W' and xdir.upper() == '') or state == 'S ':
            state = 'W '
            while True:
                for i in range(len(boundary)):
                    for j in boundary[i]:
                        print(j, end="")

                    print()

                for o in boundary:
                    if object in o:
                        x = o.index(object)
                        y = boundary.index(o)


                if boundary[y - 1][x] == '#':
                    break
                else:
                    boundary[y - 1][x] = object
                    boundary[y][x] = " "
                time.sleep(u)

        if (ydir.upper() == 'S' and xdir.upper() == 'A') or (state == 'SD' and boundary[y][x + 1] == '#')  or (state == 'WD' and boundary[y - 1][x] == '#' and boundary[y][x + 1] == '#') or (state == 'WA' and boundary[y - 1][x] == '#'):
            state = 'SA'
            while True:
                for i in range(len(boundary)):
                    for j in boundary[i]:
                        print(j, end="")

                    print()

                for o in boundary:
                    if object in o:
                        x = o.index(object)
                        y = boundary.index(o)


                if boundary[y + 1][x - 1] == '#':
                    break
                else:
                    boundary[y + 1][x - 1] = object
                    boundary[y][x] = " "

                time.sleep(u)

        if (ydir.upper() == 'W' and xdir.upper() == 'D') or (state == 'WA' and boundary[y][x - 1] == '#') or (state == 'SA' and boundary[y + 1][x] == '#' and boundary[y][x - 1] == '#') or (state == 'SD' and boundary[y + 1][x] == '#'):
            state = 'WD'
            while True:
                for i in range(len(boundary)):
                    for j in boundary[i]:
                        print(j, end="")

                    print()

                for o in boundary:
                    if object in o:
                        x = o.index(object)
                        y = boundary.index(o)


                if boundary[y - 1][x + 1] == '#':
                    break
                else:
                    boundary[y - 1][x + 1] = object
                    boundary[y][x] = " "


                time.sleep(u)


        if (ydir.upper() == 'S' and xdir.upper() == 'D') or (state == 'WA' and boundary[y - 1][x] == '#' and boundary[y][x - 1] == '#') or (state == 'SA' and boundary[y][x - 1] == '#') or (state == 'WD' and boundary[y - 1][x] == '#'):
            state = 'SD'
            while True:
                for i in range(len(boundary)):
                    for j in boundary[i]:
                        print(j, end="")

                    print()

                for o in boundary:
                    if object in o:
                        x = o.index(object)
                        y = boundary.index(o)


                if boundary[y + 1][x + 1] == '#':
                    break
                else:
                    boundary[y + 1][x + 1] = object
                    boundary[y][x] = " "

                time.sleep(u)



        if (ydir.upper() == '' and xdir.upper() == 'A') or state == ' D':
            state = ' A'
            while True:

                for i in range(len(boundary)):
                    for j in boundary[i]:
                        print(j, end="")

                    print()

                for o in boundary:
                    if object in o:
                        x = o.index(object)
                        y = boundary.index(o)


                if boundary[y][x - 1] == '#':
                    break
                else:
                    boundary[y][x - 1] = object
                    boundary[y][x] = " "
                state = ' A'
                time.sleep(u)

        if (ydir.upper() == 'W' and xdir.upper() == 'A') or (state == 'WD' and boundary[y][x + 1] == '#') or (state == 'SD' and boundary[y + 1][x] == '#' and boundary[y][x + 1] == '#') or (state == 'SA' and boundary[y + 1][x] == '#') :

            state = 'WA'
            while True:
                for i in range(len(boundary)):
                    for j in boundary[i]:
                        print(j, end="")

                    print()

                for o in boundary:
                    if object in o:
                        x = o.index(object)
                        y = boundary.index(o)


                if boundary[y - 1][x - 1] == '#':
                    break
                else:
                    boundary[y - 1][x - 1] = object
                    boundary[y][x] = " "

                time.sleep(u)

        if (ydir.upper() == '' and xdir.upper() == 'D') or state == ' A':
            state = ' D'
            while True:
                for i in range(len(boundary)):
                    for j in boundary[i]:
                        print(j, end="")

                    print()

                for o in boundary:
                    if object in o:
                        x = o.index(object)
                        y = boundary.index(o)


                if boundary[y][x + 1] == '#':
                    break
                else:
                    boundary[y][x + 1] = object
                    boundary[y][x] = " "


                time.sleep(u)


l = input()
m = input()
motion(zom,l,m)

