from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    show_result = False
    if request.method == "POST":
        show_result = True
    return render_template("index.html", show_result=show_result)

@app.route("/dowry-law")
def dowry_law():
    return render_template("dowry_law.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
