import random

from flask import Flask, request

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_password():
    length = request.json.get('length')
    start_with_letter_or_number = request.json.get('startWithLetterOrNumber')

    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    # lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    #                       't', 'u', 'v', 'w', 'x', 'y', 'z']

    upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    #                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    special_characters = "!@#$%^&*-_?"
    # special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '?']

    generated_password = ""

    for i in range(int(length)):
        if i == 0 and bool(start_with_letter_or_number):
            # First char of password and must start with letter/number
            char_type = random.randint(0, 2)
        else:
            # Can be a special char
            char_type = random.randint(0, 3)

        match char_type:
            case 0:
                # Lowercase letter
                generated_password = generated_password + random.choice(lower_case_letters)
            case 1:
                # Uppercase letter
                generated_password = generated_password + random.choice(upper_case_letters)
            case 2:
                # Number
                generated_password = generated_password + str(random.randint(0, 9))
            case 3:
                # Special character
                generated_password = generated_password + random.choice(special_characters)

    return generated_password


if __name__ == '__main__':
    app.run()
