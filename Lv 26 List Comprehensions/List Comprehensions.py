
"""
+================================+
|                                |
|         Lv 4 Toolbox           |
|      Lists and For Loops       |
+================================+
"""
# List Comprehension
squares = [x ** 2 for x in range(10)]

twos = [2 ** i for i in range(8)]

odds = [x for x in squares if x % 2 != 0 ]

# Lists in Lists
# Schachbrett mit 64 Feldern erstellen

board = []
EMPTY = "-"

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
# als List Comprehension
board = [[EMPTY for i in range(8)] for j in range(8)]

#-----------------------------------------------------------------------------

EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)

#-----------------------------------------------------------------------------

# Wetterstation misst im Monat jede Stunde die Temperatur
# Durchschnittstemperatur
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

#-----------------------------------------------------------------------------

# Höchsttemperatur
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

#-----------------------------------------------------------------------------

# Warme Tage zählen
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

#-----------------------------------------------------------------------------