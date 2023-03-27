from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "id" : 1,
    "title" : "Data Analyst",
    "location" : "London",
    "salary" : "70,000 GBP"
  },
  {
    "id" : 2,
    "title" : "Data Scientist",
    "location" : "London",
    "salary" : "80,000 GBP"
  },
{
    "id" : 3,
    "title" : "Data Engineer",
    "location" : "Glasgow",
    "salary" : "50,000 GBP"
  },
{
    "id" : 4,
    "title" : "Full Stack Developer",
    "location" : "Remote",
    "salary" : "100,000 GBP"
  }
]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)