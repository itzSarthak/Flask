from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField,SubmitField

# from wtforms.validators import DataRequired, length, email,NumberRange
from wtforms.validators import DataRequired, Length, Email,NumberRange


class FeedbackForm(FlaskForm):
    username = StringField(
        "Full Name",
        validators = [
            DataRequired(message="Name is required "),
            Length(min=4,max=50,message="Name must be between 3 and 50 characters.")
        ]
    )
    email = StringField(
        "Email Id",
        validators=[
            DataRequired(message="Email Id is required "),
            Email(message = "Enter a valid email address")
        ]
    )
    rating = IntegerField(
        "Rating 1-5",
        validators=[
            DataRequired(message="Rating is required "),
            NumberRange(min = 1,max = 5, message="Rating must be between 1 & 5 ")
        ]
    )

    message = TextAreaField(
        "Feedback message",
        validators=[
            DataRequired(message="Feedback can't be empty "),
            Length(min = 10,message = "Must be atleast 10 characters ")
        ]
    )
    submit = SubmitField("Submit Feedback")
