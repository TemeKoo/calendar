from flask import Flask, render_template, redirect, url_for, request
from datetime import date
from calendar import Calendar, day_name, month_name

app = Flask(__name__)

@app.route("/")
def index():
    today = date.today()
    url = url_for("calendar_page", year=today.year, month=today.month)
    return redirect(url)


@app.route("/calendar", methods=["GET"])
def calendar_page():
    calendar = Calendar()
    month = int(request.args.get("month"))
    year = int(request.args.get("year"))

    weeks = list(calendar.monthdays2calendar(year, month))
    
    while len(weeks) < 6:
        weeks.append([(0, i) for i in range(7)])

    data = {}
    data["weekdays"] = list(day_name)
    data["month"] = month
    data["month_name"] = month_name[month]
    data["year"] = str(year)

    return render_template("index.html", weeks=weeks, data=data)


@app.route("/prevmonth", methods=["GET"])
def prevmonth():
    month = int(request.args.get("month"))
    year = int(request.args.get("year"))

    month -= 1
    if month < 1:
        month = 12
        year -= 1
    
    url = url_for("calendar_page", year=year, month=month)

    return redirect(url)


@app.route("/nextmonth", methods=["GET"])
def nextmonth():
    month = int(request.args.get("month"))
    year = int(request.args.get("year"))

    month += 1
    if month > 12:
        month = 1
        year += 1
    
    url = url_for("calendar_page", year=year, month=month)

    return redirect(url)
