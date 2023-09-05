from flask import Flask, request, render_template
from flask.helpers import url_for
import json
import jsonify

app = Flask(__name__)
p_Open = open('jxt//players.json')
p_List = json.load(p_Open)


@app.route("/", methods=["GET", "POST"])
def main_screen():
  if request.method == "GET":
    return render_template('home.html', players=p_List)


@app.route("/listplayers")
def list_players():
  return render_template('listplayers.html', players=p_List)


@app.route("/settings", methods=["GET", "POST"])
def settings_screen():
  if request.method == "GET":
    return render_template('settings.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
