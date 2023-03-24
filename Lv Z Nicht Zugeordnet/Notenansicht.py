# Benutzername eingeben
# wenn Name vorhanden ist
# weiter zur PW Eingabe
# Wenn nicht info, dass Name nicht vorhanden

# PW Generator # # # # # # # # # # # # # # # #
def generate_password(user_data):
    print(user_data)
    pw_1st = user_data[2][0].lower()
    pw_2nd = user_data[1][0].lower()
    return pw_1st + pw_2nd + "?note"

# CSV Handling # # # # # # # # # # # # # # # #
csv_data = []

with open("Lv Z Nicht Zugeordnet/noten.csv") as file:
        for zeile in file:            
            daten = zeile.rstrip().split(";")
            csv_data.append(daten)

benutzer = input("Gebe den Benutzernamen ein: \n")
is_name_in_list = False

for line in csv_data:
    if line[0] == benutzer:
        is_name_in_list = True
        user_data = line     
        break
    
if is_name_in_list == True:
    print(f"{benutzer} ist vorhanden")
elif is_name_in_list == False:
    print(f"{benutzer} ist nicht vorhanden")
            
print(csv_data)
password = generate_password(user_data)

print(f"Dein Passwort lautet: {password}")

