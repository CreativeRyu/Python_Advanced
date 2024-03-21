# 4 # # QuizController erstellen mit init # # # #

# Erzeugen Sie eine Klasse QuizController mit einem Konstruktor, diese soll die Attribute 
# question_number und question_list haben, für die question_list wird unsere bereits generierte 
# question_bank übergeben
class QuizController:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0 # Score nach 7 hinzufügen

# 5 # # Erstellen Sie eine Methode, die dem Benutzenden die aktuelle Frage und die Fragennummer anzeigt
# Nutzen Sie die input() Funktion um dem Benutzenden den Fragetext anzuzeigen und die Antwort entgegen zu nehmen
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1 # später bei 6 hinzufügen, da wir nicht mit Frage 0 sondern Frage 1 anfangen wollen
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True | False)")
        self.check_answer(user_answer, current_question.answer) # später bei 7 hinzufügen
        # Hier erstmal ohne user_answer Variable in main testen
        # Programm hört hier an dieser Stelle noch auf weiter Fragen zu stellen
        
#-----------------------------------------------------------------------------

# 6 # # Erstellen Sie eine Methode still_has_questions(), die überprüft,
# ob noch offene Fragen im Fragenpool vorhanden sind. 
# Die Methode soll einen Boolean zurück geben.
# Nutzen Sie anschließend eine While Schleife in der Main Methode um alle Fragen anzeigen zu lassen.
    def still_has_questions(self) -> bool: 
        return self.question_number < len(self.question_list)
    
# 7 # # Erstellen Sie eine Methode check_answer(), die pürft ob die Eingabe des Benutzenden 
# mit der tatsächlichen Antwort übereinstimmt
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Richtige Antwort Sir.")
            self.score += 1 # nach 7 hinzufügen
        else:
            print("Leider nein Sir, diese Antwort ist falsch.")
        print(f"Die richtige Antwort ist {correct_answer}.")
        
        print(f"Ihr akuteller Punktestand beträgt {self.score} von {self.question_number} Punkten Sir.")
        print("\n")