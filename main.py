from flask import Flask, render_template
import json

app = Flask(__name__)
#p_Open = open('jxt//players.json')
#p_temp = json.load(p_Open)
#p_List = json.loads(p_temp)
p_List = [{
  "p_name": "Francesco",
  "p_faction_a": "A",
  "p_faction_b": "B",
  "p_faction_c": "C"
}, {
  "p_name": "Melanie",
  "p_faction_a": "A1",
  "p_faction_b": "B1",
  "p_faction_c": "C"
}]


@app.route("/")
def main_screen():
  return render_template('home.html', players=p_List)


@app.route("/settings")
def settings_screen():
  return render_template('settings.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
