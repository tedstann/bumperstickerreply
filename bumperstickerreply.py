import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgres import JSONB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['DEBUG'] = True

try:
    import local_settings
    local_settings.setup(app)
except ImportError:
    pass

db = SQLAlchemy(app)


class Sticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(1023))
    initial_comment = db.Column(db.String(140))
    comments = db.Column(JSONB)
    tag = db.Column(db.String(80))
    view_count = db.Column(db.Integer)
    created = db.Column(db.DateTime)

@app.route('/')
def index():
    pics = Sticker.query.all()
    return render_template(
        'index.html',
        pics=pics)


if __name__ == '__main__':
    app.run()
