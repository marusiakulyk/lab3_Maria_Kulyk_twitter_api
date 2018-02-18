from flask import Flask, render_template, request
import Kulyk_Maria_task1_twit as twit
import map_cr
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def form():
    return render_template("form.html")


@app.route('/map', methods=['GET', 'POST'])
def map_():
    nickname = request.form['nickname']
    a = twit.twitter(nickname, 'description')
    map_cr.map_creation(a)
    return render_template("Map.html")


if __name__ == "__main__":
    app.run(debug=True)
