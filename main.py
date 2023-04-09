from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "id" : 1,
    "title" : "Data Analyst",
    "location" : "London",
    "salary" : "70,000 GBP"
  },
  
]

@app.route("/")
def home():
  return render_template("home.html", jobs=JOBS)

@app.route("/enter")
def enter():
  return render_template("enter.html")

@app.route("/explore")
def explore():
  return render_template("explore.html")

@app.route("/quiz")
def quiz():
  return render_template("quiz.html")



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)