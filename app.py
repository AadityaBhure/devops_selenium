from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="")


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '').strip()
    age = request.form.get('age', '').strip()
    phone = request.form.get('phone', '').strip()

    # Debug print (VERY IMPORTANT)
    print("DEBUG INPUT:", name, age, phone)

    if not name:
        message = "Name is required"

    elif not age.isdigit() or int(age) < 18:
        message = "Invalid age"

    elif not phone.isdigit() or len(phone) != 10:
        message = "Invalid phone number"

    else:
        message = "Registration successful"

    print("DEBUG OUTPUT:", message)

    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(port=5000, debug=True)