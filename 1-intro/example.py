from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('temp/home.html')

@app.route('/user-signup')
def signup():
    return render_template('temp/user_signup.html')

@app.route('/user-signup',methods = ["POST"])
def my_form_post():
    first_name = request.form['f_name']
    print(first_name)
    last_name = request.form['l_name']
    print(last_name)
    return render_template('temp/user_entered.html',f_name = first_name, l_name = last_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("temp/page_not_found.html"), 404
    
if __name__ == '__main__':
    app.run(debug=True)