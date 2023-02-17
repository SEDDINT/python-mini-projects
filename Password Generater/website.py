from flask import Flask, render_template, request, url_for
import random
import string


# Start app
app = Flask(__name__)


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        length = request.form['length']
        num = request.form.get('num')
        special = request.form.get('special')

        if not length:
            error = 'please enter the minimum leangth'
            return render_template('fail.html', error=error)

        if num != None:
            num = True
        else:
            num = False
        if special != None:
            special = True
        else:
            special = False

        pwd = generate_password(int(length), bool(num), bool(special))

        return render_template('home.html', pwd=pwd)
    if request.method == 'GET':
        pwd = ''
        return render_template('home.html', pwd=pwd)


if __name__ == '__main__':
    app.run(debug=True)
