from flask import Flask,render_template_string

app = Flask(__name__)

@app.route("/index")
def index():
  return render_template_string("<h1>Hi there!</h1>")

if __name__ == "__main__":
  app.run(port=5000,host="0.0.0.0")
