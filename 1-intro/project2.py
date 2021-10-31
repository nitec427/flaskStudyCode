from flask import Flask,render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('temp2/index.html')

""" Must have an upper case letter somewhere
Must have a lower case letter somewhere
Must have a number at the end
     """
@app.route('/redirect')
def redirect():
    user_name = request.args.get('user_name')
    any_upper = False
    any_digit = False
    any_lower = False
    for c in user_name:
        if c.isdigit():
            any_digit = True
        elif c.isupper():
            any_upper = True
        elif c.islower():
            any_lower = True
    return render_template('temp2/redirect.html',name = user_name, lower = any_lower, upper = any_upper, digit = any_digit)
if __name__ == '__main__':
    app.run(debug=True)