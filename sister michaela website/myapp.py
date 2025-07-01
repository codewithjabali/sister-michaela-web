from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__, template_folder="templates")
app.secret_key = "ABDUL JABAL AL WAHAB"

# Home route - login form
@app.route("/")
def home():
    return render_template("index.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("text")
        email = request.form.get("email")
        if user and email:
            session["user"] = user
            session["email"] = email
            return redirect("/user")
        else:
            return redirect("/")  # missing input fallback

    # If user is already logged in, redirect to /user
    if "user" in session and "email" in session:
        return redirect("/user")
    return redirect("/")

# User dashboard route
@app.route("/user")
def user():
    if "user" in session and "email" in session:
        return render_template("homepage.html", user=session["user"], email=session["email"])
    return redirect("/")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/schoollife")
def schoolife():
    return render_template("schoollife.html")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")
@app.route("/academics")
def academics():
    return render_template("academics.html")

# Logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
