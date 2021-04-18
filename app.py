from flask import Flask, render_template
from datetime import date
from calendar import Calendar, day_name, month_name

app = Flask(__name__)

@app.route("/")
def index():
    calendar = Calendar()
    day = date.today()
    weeks = list(calendar.monthdays2calendar(day.year, day.month))
    
    while len(weeks) < 6:
        weeks.append([(0, i) for i in range(7)])
    
    names = {}

    names["weekdays"] = list(day_name)
    names["month"] = month_name[day.month]

    return render_template("index.html", weeks=weeks, names=names)