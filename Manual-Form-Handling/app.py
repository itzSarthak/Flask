from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # REQUIRED for flash


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    
    # Because inside the same route, we must decide:
    # “Is the user asking for the page or submitting the page?”

    if request.method == "POST":
        name = request.form.get("username")
        message = request.form.get("message")

        # Manual validation
        if not name:
            flash("Name can't be empty!", "error")
            return redirect(url_for("feedback"))

        flash(f"Thanks {name}, your feedback was saved.", "success")
        return redirect(url_for("thank_you", user=name, message=message))

    return render_template("feedback.html")

# Why separate thank you route instead of render thank you html from first api ?
# Now imagine:

# User submits the form

# Browser shows thankyou.html

# User presses refresh

# 💥 The browser re-sends the POST request
# → duplicate submission
# → duplicate flash
# → duplicate database entry (in real apps)

@app.route("/thank-you")
def thank_you():
    user = request.args.get("user")
    message = request.args.get("message")
    return render_template("thankyou.html", user=user, message=message)


if __name__ == "__main__":
    app.run(debug=True)
