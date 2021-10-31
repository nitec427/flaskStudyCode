from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextField, TextAreaField, RadioField, DateTimeField, BooleanField

from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'madafaka'
class InfoForm(FlaskForm):
    
    # In here data required instance is created and passed into validators array
    breed  = StringField("What breed are you ? ", validators = [DataRequired()])
    
    neutered = BooleanField("Have you been neutered")
    
    mood = RadioField("Please choose your mood: ", choices = [('mood_one','Happy'), ('mood_two','Sad'), ('mood_three','Excited')])
    
    food_choice = SelectField(u'Pick your favorite food: ', choices = [('chi','Chicken'),('fish','Fish'), ('bf','Beef')])
    
    feedback = TextAreaField()
    
    submit = SubmitField('Submit')
    
@app.route('/',methods=['POST','GET'])
def index():
        
    form = InfoForm()
        
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        
        return redirect(url_for('thankyou'))
    return render_template('index.html', form=form)
    
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
if __name__ == '__main__':
    app.run(debug=True)