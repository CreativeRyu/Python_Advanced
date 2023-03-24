# # # # Lv 16 OOP Script 2 # # # #

# 1 # # Über Python Pckages prettytable installieren # # # #
from prettytable import PrettyTable

# 2 # # Objekt aus PrettyTable erstellen und es table nennen # # # #
table = PrettyTable()

# 3 # # Tabelle unter zuhilfenahme der Doku erstellen # # # #
table.add_column("Number",["1","2","3","4","5","6","7","8","9"])
table.add_column("Pokemon Name",["Bisasam","Bisaknosp","Bisaflor","Glumanda","Glutexo","Glurak","Schiggie","Schillok","Turtok"])
table.add_column("Type",["Pflanze | Gift","Pflanze | Gift","Pflanze | Gift","Feuer","Feuer","Feuer | Flug","Wasser","Wasser","Wasser"])
table.align ="l" 

print(table)