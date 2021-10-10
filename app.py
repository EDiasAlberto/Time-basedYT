from linkFuncs import getLink
from flask import Flask, render_template
import re, time

app = Flask(__name__)

def timeValid(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False


@app.route("/")
@app.route("/<time>")
def hello_world(time=None):
    if time is not None:
        if not timeValid(time):
            return "<h1> INVALID TIME IN URL </h1> <p>Time should be in the format HH:MM</p>"
    video = getLink(time)
    return render_template("index.html", id = video["id"])

if __name__ == '__main__':
    app.run()