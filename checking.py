# Returns number possibilities of given cell depending of line
def checkLine(numberGrid, coordinates):
    i = coordinates[0]
    hypothesis = []
    for number in range(1, 10):
        boolean = False  # not on line
        for jx in range(len(numberGrid[i])):
            if number == numberGrid[i][jx]:  # found number on line
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
    for number in range(1, 10):
        boolean = False  # not on column
        for ix in range(len(numberGrid[j])):
            if number == numberGrid[ix][j]:  # found number on column
                boolean = True
        if not boolean:
            hypothesis.append(number)
        elif boolean and number in hypothesis:  # if number was placed after hypothesis init
            hypothesis.remove(number)
    return hypothesis


# Functions to find neighbours coordinates in the box
def getIList(i):
    if i % 3 == 0:
        return [i, i + 1, i + 2]
    elif i % 3 == 1:
        return [i, i - 1, i + 1]
    elif i % 3 == 2:
        return [i, i - 1, i - 2]


def getJList(j):
    if j % 3 == 0:
        return [j, j + 1, j + 2]
    elif j % 3 == 1:
        return [j, j - 1, j + 1]
    elif j % 3 == 2:
        return [j, j - 1, j - 2]


def mergeLists(iList, jList):
    checkingList = []
    for i in iList:
        for j in jList:
            checkingList.append((i, j))
    return checkingList


# Returns number possibilities of given cell depending of box
def checkBox(numberGrid, coordinates):
    i = coordinates[0]
    j = coordinates[1]
    iList = getIList(i)
    jList = getJList(j)
    checkingList = mergeLists(iList, jList)
    checkingList.remove((i, j))
    checkingList.sort()
    hypothesis = []

    for number in range(1, 10):
        boolean = False  # not in box
        for cell in checkingList:
            ix = cell[0]
            jx = cell[1]
            if number == numberGrid[ix][jx]:  # found number in box
                boolean = True
        if not boolean and number not in hypothesis:
            hypothesis.append(number)
        elif boolean and number in hypothesis:  # if number was placed after hypothesis init
            hypothesis.remove(number)
    return hypothesis


# Returns numbers that are common to 3 checking lists
def getHypothesis(numberGrid, cursor):
    lineHypo = checkLine(numberGrid, cursor)
    columnHypo = checkColumn(numberGrid, cursor)
    boxHypo = checkBox(numberGrid, cursor)
    hypothesis = []
    for hypo in lineHypo:
        if hypo in columnHypo and hypo in boxHypo:
            hypothesis.append(hypo)
    #print("coordinates", cursor, "hypothesis are: ", hypothesis)
    return hypothesis
