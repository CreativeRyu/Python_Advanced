
from random import choice, randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class PasswordGenerator():
    def __init__(self):
        self.pw_letters = [choice(letters) for _ in range(randint(8, 10))]
        self.pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        self.pw_numbers = [choice(letters) for _ in range(randint(2, 4))]

    def generate_password(self) -> str:
        password_list = self.pw_letters + self.pw_symbols + self.pw_numbers

        shuffle(password_list)

        return "".join(password_list)