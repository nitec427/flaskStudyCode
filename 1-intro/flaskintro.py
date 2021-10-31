from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    is_user_logged_in = True
    return 

@app.route('/information')
def info():
    return '<p>Labrador</p>'

# Dynamic routing example

@app.route('/puppy/<name>')
def greetPuppy(name):
    return f'<h1>Welcome big {name[15]} Lord.'

@app.route('/puppy_latin/<name>')
def changeName(name):
    ex_name = name
    if name[-1] != 'y':
        name = name + 'y'
    else:
        name = name[:-1] + 'i'
        name = name + 'ful'
    return f'<h1>Hello {ex_name}! Your latin puppy name is {name}'
if __name__ == '__main__':
    app.run(debug=True)