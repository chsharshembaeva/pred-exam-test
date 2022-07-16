from flask_wtf import FlaskForm
import wtforms as wf


class CustomerForm(FlaskForm):
    name = wf.StringField('Покупатель', validators=[wf.validators.DataRequired()])
    phone_number = wf.StringField('Номер телефона', validators=[wf.validators.DataRequired()])
    item = wf.StringField('Предмет покупки', validators=[wf.validators.DataRequired()])
    quantity = wf.IntegerField('Количество', validators=[wf.validators.DataRequired()])
    price = wf.IntegerField('Сумма', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('Добавить')


class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('OK')