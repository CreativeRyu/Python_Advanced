# # # # Lv 16 OOP Script 1 # # # #

# 1 # # vorerst nur Turtle oder sogar nur turtle importieren # # # #
from turtle import Turtle, Screen

# 2 # # Objekt Deklaration # # # #
myDude = Turtle()

##########################################################################################

# 6 # # Nach der exitonclick() Methode # # # #
myDude.shape("turtle")

# 7 # # Miniaufgabe anhand der Dokumentation die Farbe der Schildkröte ändern # # # #
# 8 # # Miniaufgabe die Schildkröte um 100 einheiten vorwärts bewegen # # # #
myDude.color("DarkSeaGreen")
myDude.forward(100)
myDude.right(90)
myDude.forward(100)
myDude.right(90)
myDude.forward(100)
myDude.right(90)
myDude.forward(100)

##########################################################################################

# 3 # # Zeigen an Welcher auf dem Speicher das Objekt abgelegt wird # # # #
print(myDude)

# 4 # # hier den Screen importieren # # # #
# # # # Zugriff auf die Attribute eines Objektes mit object.attribute erläutern # # # #
myScreen = Screen()
print(myScreen.canvheight)

# 5 # # Zugriff auf die Methode eines Objektes # # # #
myScreen.exitonclick()