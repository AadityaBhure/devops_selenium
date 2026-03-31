from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')
        password = request.form.get('password')

        if not all([name, age, gender, phone, email, address, password]):
            return "Error: All fields are required ❌"

        if not age.isdigit() or int(age) < 18:
            return "Error: Age must be 18+ ❌"

        if len(phone) != 10 or not phone.isdigit():
            return "Error: Invalid phone number ❌"

        if "@" not in email:
            return "Error: Invalid email ❌"

        if len(password) < 6:
            return "Error: Password must be at least 6 characters ❌"

        return f"Registration successful! Welcome {name} 🎉"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)