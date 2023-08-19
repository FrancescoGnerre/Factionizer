from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_screen():
  return render_template('home.html')


@app.route("/settings")
def settings_screen():
  return render_template('settings.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
