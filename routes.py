import datetime
import uuid
from collections import defaultdict
from flask import Blueprint, render_template, request, redirect, url_for, current_app, make_response, jsonify

blp = Blueprint("habits", __name__, template_folder="templates", static_folder="static")


def today_at_midnight():
    today = datetime.datetime.today()
    return datetime.datetime(today.year, today.month, today.day)

@blp.context_processor
def add_calc_date_range():
    def date_range(start: datetime.datetime):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates
    
    return  {"date_range": date_range}

@blp.route("/")
def index():
    dateStr = request.args.get("date")
    if dateStr:
        selectedDate = datetime.datetime.fromisoformat(dateStr)
    else:
        selectedDate = today_at_midnight()
    
    habitsOnDate = current_app.db.habits.find({"added": {"$lte": selectedDate}}) 
    completions = [habit["habit"] for habit in current_app.db.completions.find({"date": selectedDate})]
        
    return render_template("index.html", habits=habitsOnDate, title="Habit Tracker - Home",
                           selectedDate=selectedDate, completions=completions)
    
@blp.route("/select", methods=["GET", "POST"])
def selecting_habit():
    dateStr = request.args.get("date")
    if dateStr:
        selectedDate = datetime.datetime.fromisoformat(dateStr)
    else:
        selectedDate = today_at_midnight()
    
    habitsOnDate = current_app.db.habits.find({"added": {"$lte": selectedDate}}) 
    completions = [habit["habit"] for habit in current_app.db.completions.find({"date": selectedDate})]
        
    return render_template("delete_habit.html", habits=habitsOnDate, title="Habit Tracker - Deleting",
                           selectedDate=selectedDate, completions=completions)


@blp.route("/add", methods=["GET", "POST"])
def add_habit():
    today = today_at_midnight()
    
    if request.method == "POST":
        current_app.db.habits.insert_one({"_id": uuid.uuid4().hex, "added": today, "name": request.form.get("habit")})
        
    return render_template("add_habit.html", title="Habit Tracker - Add Habit", selectedDate=today)

@blp.route("/delete", methods=["GET", "POST"])
def delete_habit():
    selectedHabits = request.form.getlist("selected_habits")
    for habit_id in selectedHabits:
        current_app.db.habits.delete_one({"_id": habit_id})
    
    make_response(jsonify({"message": "Habit deleted successfully"}), 200)
    return redirect(url_for('.index'))


@blp.route("/complete", methods=["POST"])
def complete():
    dateString = request.form.get("date")
    habit = request.form.get("habitID")
    date = datetime.datetime.fromisoformat(dateString)
    current_app.db.completions.insert_one({"date": date, "habit": habit})
    
    return redirect(url_for("habits.index", date=dateString))