from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp
from settings import SHORT_ID_REGEX, MAX_CUSTOM_LENGTH


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
            Length(
                1,
                MAX_CUSTOM_LENGTH,
                message=(
                    f"Максимальная длинна короткой ссылки \n"
                    f"не должна превышать {MAX_CUSTOM_LENGTH} знаков."
                ),
            ),
            Regexp(
                SHORT_ID_REGEX,
                message=(
                    "Может состоять только из латинских \
                        букв(без учета регистра) и цифр"
                ),
            ),
        ),
    )
    submit = SubmitField("Добавить")
