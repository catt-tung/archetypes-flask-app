from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Survival Archetype', choices=[('child', 'Child'), ('saboteur', 'Saboteur'), ('victim', 'Victim'), ('prostitute', 'Prostitute')], validators=[DataRequired()])
    content = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')