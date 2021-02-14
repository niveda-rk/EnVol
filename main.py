from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html',**locals())

@app.route('/', methods=["GET", "POST"]) 
def gfg(): 
    if request.method == "POST":  
       first_name = request.form.get("fname")  
       last_name = request.form.get("lname")
       residence = request.form.get("residence")
       password = request.form.get("pwd")
       return redirect("/upcoming-events/")
    return render_template("index.html")

@app.route("/upcoming-events/")
def upcoming_events():
    return render_template('eventCat.html',**locals())

@app.route("/About/")
def about():
    return render_template('about.html',**locals())

@app.route("/upcoming-events/profile/")
def profile():
    return render_template('userProfile.html',**locals())

@app.route("/upcoming-events/newEvent/")
def new_event():
    return render_template('newEvent.html',**locals())

@app.route("/upcoming-events/Education/")
def foodBank():
    return render_template('education.html',**locals())

if __name__ == "__main__":
    app.run()