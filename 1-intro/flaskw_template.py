from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(name = None):
    return render_template('index.html', name=name)
@app.route('/<name>')
def greetIndex(name = None):
    return render_template('index.html', name=name)

@app.route('/rendered')
def renderedPage():
    name = 'JeanMilburn'
    # We can also pass lists into templates via render_template function
    the_list = list(name)
    return render_template('basic.html',user_name = name, letters=  the_list)


if __name__ == '__main__':
    app.run(debug=True)