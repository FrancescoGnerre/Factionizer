from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for
import json
import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
db = SQLAlchemy(app)
#p_Open = open('jxt//players.json')
#p_Open = open('test.json')
#p_List = json.load(p_Open)
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


class Player(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  player_name = db.Column(db.String(200), nullable=False)

  def __repr__(self):
    return '<Task %r>' % self.id


@app.route("/", methods=["GET", "POST"])
def main_screen():
  if request.method == "POST":
    new_player_to_add = request.form['add_new_player']
    new_player = Player(player_name=new_player_to_add)

    try:
      db.session.add(new_player)
      db.session.commit()
      return redirect("/")
    except:
      return "There was an error. Please try again."

  else:
    players_all = Player.query.order_by(Player.player_name)
    return render_template('home.html', players=p_List)


@app.route("/listplayers")
def list_players():
  return render_template('listplayers.html', players=p_List)


@app.route("/settings", methods=["GET", "POST"])
def settings_screen():
  if request.method == "GET":
    return render_template('settings.html')


@app.route("/start", methods=["GET", "POST"])
def start_screen():
  if request.method == "GET":
    return render_template('listplayers.html', players=p_List)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
