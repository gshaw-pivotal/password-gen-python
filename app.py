from flask import Flask, request

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_password():
    length = request.json.get('length')
    startWithLetterOrNumber = request.json.get('startWithLetterOrNumber')

    print("Length: " + str(length))
    print("Start with letter/number: " + str(startWithLetterOrNumber))

    return request.json


if __name__ == '__main__':
    app.run()
