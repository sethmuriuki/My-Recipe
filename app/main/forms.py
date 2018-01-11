from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

class CommentForm(FlaskForm):
    comment_section_id = TextAreaField('Add Comment')
    submit = SubmitField('Submit')