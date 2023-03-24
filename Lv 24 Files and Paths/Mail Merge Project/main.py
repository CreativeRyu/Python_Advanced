# TODO: Erstelle einen Brief mit starting_letter.txt
# für jeden Namen in invited_names.txt
# soll der Platzhalter [name] durch den tatsächlichen Namen ersetzt werden.
# Speichern Sie die Briefe in dem Ordner "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Holt die Namen aus der Datei und speichert sie in einer Liste
with open("Lv 24 Files and Paths/Mail Merge Project/Input/Names/invited_names.txt") as file:
    names = file.read()
    names = names.split("\n")


# Holt den Text aus der Quelldatei und speichert diesen in einer Variable
with open("Lv 24 Files and Paths/Mail Merge Project/Input/Letters/starting_letter.txt") as source:
    s_letter = source.read()


for name in names:
    t_letter = s_letter.replace("[name]", name)
    # Neue Text Datei erzeugen
    with open(f"Lv 24 Files and Paths/Mail Merge Project/Output/ReadyToSend/{name}_letter.txt", mode="w") as new_letter:
        new_letter.write(t_letter)
