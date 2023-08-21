from flask import Flask, render_template
import json

app = Flask(__name__)
pOpen = open('jxt/players.json')
pList = json.load(pOpen)


@app.route("/")
def main_screen():
  return render_template('home.html', players=pList)


@app.route("/settings")
def settings_screen():
  return render_template('settings.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
