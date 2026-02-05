from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    user_message = request.form.get("message", "")

    if not user_message.strip():
        reply = "Please enter a message"
    else:
        reply = f"I accept your text: {user_message}"

    return render_template("result.html", message=reply)
if __name__ == "__main__":
    app.run(debug=True)
