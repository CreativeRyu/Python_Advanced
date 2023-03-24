from dataPool import resources

# TODO 1: Print Report

command_choice = ""
ON = True
money = 0

# Prüft die Eingabe des Benutzers
def chose_command():
    command = input("Wir haben Espresso, Latte und Cappuccino:\n")
    command = command.lower()
    if command == "espresso":
        return 1
    elif command == "latte":
        return 2
    elif command == "cappuccino":
        return 3
    elif command == "off":
        return 4
    elif command == "report":
        return 5

def generate_report(money):
    for key in resources:
         resource = key.capitalize()
         value = resources[key]
         print(f"{resource} : {value}")
    print(f"Money : {money} €")

while ON:
    print("\n##############################################\n")
    print("Guten Morgen Sir, was für einen Kaffee hätten Sie gerne ?\n")

    command_choice = chose_command()
    if command_choice == 4:
        ON = False
        break
    elif command_choice == 5:
        generate_report(money)

# TODO 2: Check resources sufficient

# TODO 3: Process Coins

# TODO 4: Check transaction successful