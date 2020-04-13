from flask import Flask, request, render_template
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import schedule
from classes_dataframe import classes_df

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduler.db'
db = SQLAlchemy(app)

class Classes(db.Model):
    # __tablename__ = "classes"
    course_id = db.Column(db.String, primary_key=True)
    days = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    am_pm = db.Column(db.String, nullable=False)
    department = db.Column(db.String)
    professor = db.Column(db.String)
    name = db.Column(db.String)
    link = db.Column(db.String)
    term = db.Column(db.String)
    course_number = db.Column(db.String)

# classes_df.to_sql(name='classes', con=db.engine, index=False)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_excel(request.files.get('file'))
        return render_template('upload.html', schedules=schedule.possible_schedules(df, 3, []))
    return render_template('upload.html')

@app.route('/selection', methods=['GET', 'POST'])
def selection():
    carlist = ['Subaru', 'Chevy']
    if request.method == 'POST':
        manufacturer = request.form['manu']
        return f"{manufacturer} has been selected!"
    return render_template("selection.html", title = 'Home', carlist=carlist)

if __name__ == '__main__':
    app.run(debug=True)
