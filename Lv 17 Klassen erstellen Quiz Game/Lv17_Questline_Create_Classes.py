# # # # Lv 17 Script 1 Create Classes # # # #
"""
+================================+
|                                |
|    Lv 17 Klassen erstellen     |
|                                |
+================================+
"""
# 1 # # Klasse mit dem Schlüsselwort class # # # #
# # # # erstellen und in PascalCase benennen # # # #
class User:
    pass

# 2 # # Objekt Initialisierung # # # #
user_1 = User()

# 3 # # Attribute hinzufügen
user_1.id = "007"
user_1.name = "Marx"

user_2 = User()
user_2.id = "001"
user_2.username = "Ryu" #  hier könnte schnell ein typo entstehen username /= name
# how to force

print(user_1.id)

#---------------------------------------

# 4 # # Konstruktor erstellen # # # #
class Tea:
    def __init__(self):
        print("new Tea being created...")
        
tea_1 = Tea()
print(tea_1)

# __init__ Funktion wird jedes mal aufgerufen, wenn ein neues Objekt einer Klasse erzeugt wird

# Beispiel
class Car:
    def __init__(self, seats):
        self.seats = seats

# Objekt mit Attribut erzeugen Version 1
new_car = Car(5) # erster Parameter wird nicht berücksichtigt, da self

# Objekt mit Attribut erzeugen Version 2
new_car2 = Car()
new_car2.seats = 5

#-----------------------------------------------------------------------------

# 5 # # Am Beispiel unseres Users # # # #
class UserWithConstructor:    
    def __init__(self, user_id, username):
        self.id = user_id # Convention ist hier die self Attribute genau so wie die Parameter zu benennen
        self.username = username
        # 6 # # Methoden hinzufügen # # # #
        # User Account bei Instagram startet -> keine Follower
        self.followers = 0 # Default Values, die nicht jedes Mal mit übergeben werden müssen
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = UserWithConstructor("007", "James")
user2 = UserWithConstructor("001","Ryu")

user1.follow(user2)
print(f"{user1.username} Followers: {user1.followers} Following: {user1.following}")
print(f"{user2.username} Followers: {user2.followers} Following: {user2.following}")

#-----------------------------------------------------------------------------

# -> To Quiz Project -> question_Model