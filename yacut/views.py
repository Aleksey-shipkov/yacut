import random
import string

from flask import render_template, redirect, flash

from yacut import app, db
from yacut.forms import YacutForm
from yacut.models import URLMap
from settings import MAX_LENGTH


def generate_short_id():
    items = string.ascii_letters + string.digits
    short_id = "".join(random.choice(items) for i in range(MAX_LENGTH))
    if URLMap.query.filter_by(short=short_id).first():
        return generate_short_id()
    return short_id


@app.route("/", methods=("GET", "POST"))
def get_unique_short_id():
    form = YacutForm()
    if not form.validate_on_submit():
        return render_template("index.html", form=form)
    short_id = form.custom_id.data
    if short_id and URLMap.query.filter_by(short=short_id).first():
        flash(f"Имя {short_id} уже занято!")
        return render_template("index.html", form=form)
    if not short_id or len(short_id) == 0:
        short_id = generate_short_id()
    unique_short_id = URLMap(original=form.original_link.data, short=short_id)
    db.session.add(unique_short_id)
    db.session.commit()
    context = {"short_id": short_id}
    return render_template("index.html", form=form, **context)


@app.route("/<string:short>", methods=("GET",))
def get_original_link(short):
    link = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(link.original, code=302)
