from application import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name
        self.price = 0
        self.amount = 0
