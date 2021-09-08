from datetime import datetime
import string
import random


class Randomizer:

    @staticmethod
    def get_random_username():
        username = ''.join(random.choice(string.ascii_letters) for i in range(4))
        current_time = datetime.now().strftime("%d%m%Y%H%M%S")
        return username + current_time

    @staticmethod
    def get_password():
        password_letters = ''.join(random.choice(string.ascii_letters) for i in range(6))
        password_digits = ''.join(random.choice(string.digits) for i in range(2))
        return password_letters+password_digits
