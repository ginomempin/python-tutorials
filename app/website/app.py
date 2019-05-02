
from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for


app = Flask(
    __name__,
    static_url_path="/public",
    static_folder="public",
    template_folder="templates"
)


@app.route("/")
def root():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
