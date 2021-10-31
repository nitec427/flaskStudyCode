from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/<name>')
def myView(name):
    return render_template('home.html',name=name)

@app.route('/puppy')
def puppy():
    return render_template('puppy.html',user_name = "Bra")

if __name__ == '__main__':
    app.run(debug=True)