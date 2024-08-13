import random

from flask import Flask, request

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_password():
    length = request.json.get('length')
    startWithLetterOrNumber = request.json.get('startWithLetterOrNumber')

    lowercaseletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']

    uppercaseletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    specialcharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '?']

    generatedpassword = ""

    for i in range(int(length)):
        if i == 0 and bool(startWithLetterOrNumber):
            # First char of password and must start with letter/number
            charType = random.randint(0,2)
        else:
            # Can be a special char
            charType = random.randint(0, 3)

        match charType:
            case 0:
                # Lowercase letter
                generatedpassword = generatedpassword + random.choice(lowercaseletters)
            case 1:
                # Uppercase letter
                generatedpassword = generatedpassword + random.choice(uppercaseletters)
            case 2:
                # Number
                generatedpassword = generatedpassword + str(random.randint(0, 9))
            case 3:
                # Special character
                generatedpassword = generatedpassword + random.choice(specialcharacters)

    return generatedpassword

if __name__ == '__main__':
    app.run()
