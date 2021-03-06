import time
import Grid
import checking


# While cell has 0 as number, game is not finished
def finished(numberGrid):
    for i in range(len(numberGrid)):
        for j in range(len(numberGrid)):
            if numberGrid[i][j] == 0:
                return False
    return True


# Solving algorithm
def solving(grid):
    step = 0
    numberGrid = grid.getNumberGrid()
    grid.printGrid(step)
    while not finished(numberGrid):
        for i in range(len(numberGrid)):
            for j in range(len(numberGrid)):
                cursor = (i, j)
                if numberGrid[i][j] == 0:
                    # print(Grid.colors.YELLOW + "Working on: (", i, ",", j, ")")
                    hypothesis = checking.getHypothesis(numberGrid, cursor)
                    currentCell = grid.getCell(cursor)
                    currentCell.setHypothesis(hypothesis)
                    numberGrid[i][j] = currentCell.placeNumber()
                    checking.updateHypothesis(grid, numberGrid[i][j], i, j)
                    # print(Grid.colors.YELLOW + "final hypothesis:", currentCell.getHypothesis())
        checking.updateAll(numberGrid, grid)
        grid.printGrid(step)
        checking.updateTuples(numberGrid, grid)
        step += 1
        grid.printGrid(step)


##################################################
grid = Grid.Grid()
grid.initNumberGrid()
grid.initCellList(grid.gridInit())
if grid.getCellList() == 0:
    print("Parsing failed, script will now stop")
else:
    solving(grid)
