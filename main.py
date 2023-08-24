from flask import Flask, request, render_template
from flask.helpers import url_for
import json
import jsonify

app = Flask(__name__)
#p_Open = open('jxt//players.json')
#p_temp = json.load(p_Open)
#p_List = json.loads(p_temp)
p_List = [{
  "p_name": "Francesco",
  "p_faction_a": "A",
  "p_faction_b": "B",
  "p_faction_c": "C",
  "p_blue_1": "U1",
  "p_blue_2": "U2",
  "p_blue_3": "U3",
  "p_red_1": "R1",
  "p_red_2": "R2"
}, {
  "p_name": "Melanie",
  "p_faction_a": "A1",
  "p_faction_b": "B1",
  "p_faction_c": "C1",
  "p_blue_1": "U11",
  "p_blue_2": "U21",
  "p_blue_3": "U31",
  "p_red_1": "R11",
  "p_red_2": "R21"
}, {
  "p_name": "Luciano"
}]


@app.route("/", methods=["GET", "POST"])
def main_screen():
  if request.method=="GET":
    return render_template('home.html', players=p_List)
  


@app.route("/api/players")
def list_players():
  return jsonify(p_List)


@app.route("/settings", methods=["GET", "POST"])
def settings_screen():
  if request.method=="GET":
    return render_template('settings.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
