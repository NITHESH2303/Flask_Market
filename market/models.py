from market import db


class user(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False, default='guest' + str(id))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False, )
    budget = db.Column(db.Integer(), nullable=False, default=100)
    items = db.relationship('item', backref='owned_user', lazy=True)
# lazy = "True" --> Tells when to get the object , similar fetch = "select" --> how to get the object


class item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True, default='N/A')
    price = db.Column(db.Integer(), nullable=False, default='Coming Soon')
    barcode = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(1000), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
# ForeignKey refers to the primary_key of another table

    def __repr__(self):
        return f'item: {self.name}'
