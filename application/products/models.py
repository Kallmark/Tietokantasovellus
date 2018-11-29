from application import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)
    
    purchases = db.relationship("Purchase", backref='product', lazy=True)

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
