from flask import Flask,request,Response,render_template,session,url_for,redirect
app = Flask(__name__)

app.secret_key = "supersecret"

USERS = {
    "sarthak":"123",
    "amit":"5678",
    "admin":"@123"
}

ITEMS = {
    "sarthak": ["Book","Laptop","Pen"],
    "amit": ["Pencil","Mobile"],
    "neha": ["Notebook","Cofee"]
}

@app.route("/")
def home():
    return render_template("home.html",error = None)

@app.route("/submit", methods = ["POST"])
def submit():
    username = request.form.get("username").lower()
    password = request.form.get("password")

    if username in USERS and USERS[username] == password:
        session["username"] = username
        return redirect(url_for("welcome"))
    else:
        return render_template("home.html", error = "Invalid Username or Password !")

@app.route("/welcome")
def welcome():
    if "username" in session:
        user = session["username"]
        return render_template("welcome.html",user = user,items = ITEMS.get(user,[]))
    
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("home"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"),404


if __name__ == "__main__":
    app.run(debug=True)


