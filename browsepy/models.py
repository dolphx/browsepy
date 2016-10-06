from browsepy import db


class Metadata(db.Model):
    path = db.Column(db.String(), primary_key=True)
    desc = db.Column(db.String())
