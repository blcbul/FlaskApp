from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateCategory(FlaskForm):
    category = StringField('Categoría', validators=[DataRequired()])
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Guardar')