from flask import jsonify, request, url_for

from yacut import app, db
from yacut.models import URLMap
from yacut.views import generate_short_id
from yacut.error_handlers import InvalidAPIUsage
from yacut.validators import isalnum_check


@app.route("/api/id/", methods=("POST",))
def get_short_id():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage("Отсутствует тело запроса", 400)
    custom_id = data.get("custom_id")
    if custom_id is None or len(custom_id) == 0:
        custom_id = generate_short_id()
    if "url" not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!', 400)
    if custom_id is not None and (
        len(custom_id) > 16 or not isalnum_check(custom_id)
    ):
        raise InvalidAPIUsage(
            "Указано недопустимое имя для короткой ссылки", 400
        )
    if URLMap.query.filter_by(short=custom_id).first() is not None:
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.', 400)

    urlmap = URLMap(original=data["url"], short=custom_id)
    db.session.add(urlmap)
    db.session.commit()
    return (
        jsonify(
            {
                "url": urlmap.original,
                "short_link": url_for(
                    "get_original_link", short=urlmap.short, _external=True
                ),
            }
        ),
        201,
    )


@app.route("/api/id/<string:short_id>/", methods=("GET",))
def get_original_url(short_id):
    link = URLMap.query.filter_by(short=short_id).first()
    if link is None:
        raise InvalidAPIUsage("Указанный id не найден", 404)
    return jsonify({"url": link.original})
