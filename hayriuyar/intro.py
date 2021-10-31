from flask import Flask, render_template, url_for
from datetime import datetime

# An application gets instantiated
app = Flask(__name__)

@app.route('/')
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template('home.html', day = day_name)
@app.route('/movies')
def movies_page():
    return render_template("movies.html")
if __name__ == '__main__':
    app.run(debug=True, host ="0.0.0.0",port=8080)
    # The application starts on the localhost and waits for requests
    # When a request comes for '/', the homepage function is called
    # Host 0.0.0.0 is publicly available