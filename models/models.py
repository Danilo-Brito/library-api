from library import db


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
