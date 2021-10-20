# Returns number possibilities of given cell depending of line
def checkLine(numberGrid, coordinates):
    i = coordinates[0]
    hypothesis = []
    for number in range(1, 9):
        boolean = False  # not on line
        for jx in range(len(numberGrid[i])):
            if number == numberGrid[i][jx]:     # found number on line
                boolean = True
        if not boolean:
            hypothesis.append(number)
        elif boolean and number in hypothesis:  # if number was placed after hypothesis init
            hypothesis.remove(number)
    return hypothesis


# Returns number possibilities of given cell depending of column
def checkColumn(numberGrid, coordinates):
    j = coordinates[1]
    hypothesis = []
    for number in range(1, 9):
        boolean = False  # not on column
        for ix in range(len(numberGrid[j])):
            if number == numberGrid[ix][j]:  # found number on column
                boolean = True
        if not boolean:
            hypothesis.append(number)
        elif boolean and number in hypothesis:  # if number was placed after hypothesis init
            hypothesis.remove(number)
    return hypothesis


# Returns number possibilities of given cell depending of box
def checkBox(numberGrid, coordinates):
    i = coordinates[0]
    j = coordinates[1]

    boolean = False  # not in box
    hypothesis = []

    # TO DO

    return hypothesis


# Returns numbers that are common to 3 checking lists
def getHypothesis(numberGrid, cursor):
    lineHypo = checkLine(numberGrid, cursor)
    columnHypo = checkColumn(numberGrid, cursor)
    #boxHypo = checkBox(numberGrid, cursor)
    hypothesis = []
    for hypo in lineHypo:
        if hypo in columnHypo :
            #and hypo in boxHypo
            hypothesis.append(hypo)
    print("coordinates", cursor, "hypothesis are: ", hypothesis)
    return hypothesis
