from datetime import datetime

from yacut import db
from settings import MAX_CUSTOM_LENGTH


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(
        db.String(MAX_CUSTOM_LENGTH), unique=True, nullable=False
    )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
