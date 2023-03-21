from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp
from settings import SHORT_ID_REGEX


class YacutForm(FlaskForm):
    original_link = URLField(
        "Длинная ссылка",
        validators=(
            DataRequired(message="Это обязательное поле"),
            URL(require_tld=False, message="Можно добавлять только ссылку"),
        ),
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=(
            Optional(),
            Length(1, 16),
            Regexp(
                SHORT_ID_REGEX,
                message="Может состоять только из латинских букв(без учета регистра) и цифр",
            ),
        ),
    )
    submit = SubmitField("Добавить")
