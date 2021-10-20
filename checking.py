def checkLine(numberGrid, coordinates):
    i = coordinates[0]

    boolean = False     # not on line
    hypothesis = []

    for number in range(1, 9):
        print(number)
        while not boolean:                          # while number is not found on line, we keep looking
            for jx in len(range(numberGrid[i])):
                if number == numberGrid[i][jx]:     # found number on line
                    boolean = True
            if not boolean:
                hypothesis.append(number)
    return hypothesis


def checkColumn(numberGrid, coordinates):
    j = coordinates[1]

    boolean = False     # not on column
    hypothesis = []

    for number in range(1, 9):
        print(number)
        while not boolean:                          # while number is not found on column, we keep looking
            for ix in len(range(numberGrid[j])):
                if number == numberGrid[ix][j]:     # found number on column
                    boolean = True
            if not boolean:
                hypothesis.append(number)
    return hypothesis


def checkBox(numberGrid, coordinates):
    i = coordinates[0]
    j = coordinates[1]

    boolean = False  # not on column
    hypothesis = []

    return hypothesis