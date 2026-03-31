from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = """
<form method="POST">
    Name: <input type="text" name="name"><br>
    Age: <input type="text" name="age"><br>
    Phone: <input type="text" name="phone"><br>
    <input type="submit" value="Submit">
</form>
<p>{{ message }}</p>
"""

@app.route('/', methods=['GET', 'POST'])
def form():
    message = ""

    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        phone = request.form.get('phone')

        # Name validation
        if not name:
            message = "Name is required"

        # Age validation
        elif not age.isdigit() or int(age) < 18:
            message = "Invalid age"

        # Phone validation
        elif not phone.isdigit() or len(phone) != 10:
            message = "Invalid phone number"

        else:
            message = "Registration successful"

    return render_template_string(HTML_FORM, message=message)

if __name__ == "__main__":
    app.run(port=5000)