from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Survival Archetype', choices=[('Child', 'Child'), ('Saboteur', 'Saboteur'), ('Victim', 'Victim'), ('Prostitute', 'Prostitute')], validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class PostUpdateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Survival Archetype', choices=[('Child', 'Child'), ('Saboteur', 'Saboteur'), ('Victim', 'Victim'), ('Prostitute', 'Prostitute')], validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Update this Story')