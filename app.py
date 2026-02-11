from flask import Flask, render_template, request, redirect, url_for, flash
from forms import FeedbackForm

app = Flask(__name__)
app.secret_key = "supersecretkey"  # REQUIRED for flash


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    
    # Because inside the same route, we must decide:
    # “Is the user asking for the page or submitting the page?”
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        rating = form.rating.data
        message = form.message.data

        flash("Feedback submitted succesfully ! ","success")
        return redirect(url_for("thank_you",user=name,email=email,rating=rating,message=message))
    


    return render_template("feedback.html",form=form)

# Why separate thank you route instead of render thank you html from first api ?
# Now imagine:

# User submits the form
# Browser shows thankyou.html
# User presses refresh

# 💥 The browser re-sends the POST request
# → duplicate submission
# → duplicate flash
# → duplicate database entry (in real apps)

@app.route("/thank_you")
def thank_you():
    user = request.args.get("user")
    email = request.args.get("email")
    rating = request.args.get("rating")
    message = request.args.get("message")

    return render_template("thankyou.html", user=user, email=email,rating=rating,message=message)


if __name__ == "__main__":
    app.run(debug=True)
