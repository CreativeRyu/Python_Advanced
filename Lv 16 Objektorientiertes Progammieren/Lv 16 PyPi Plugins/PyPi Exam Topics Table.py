# # # # Lv 16 OOP Script 2 # # # #

# 1 # # Über Python Pckages prettytable installieren # # # #
from prettytable import PrettyTable

# 2 # # Objekt aus PrettyTable erstellen und es table nennen # # # #
table = PrettyTable()

# 3 # # Tabelle unter zuhilfenahme der Doku erstellen # # # #
table.add_column("Number",["1",])
table.add_column("Topic",["0110"])
table.add_column("Content",["101010"])
table.align ="l" 

print(table)