from application import db
from application.models import Base

class Product(Base):

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)
    
    purchases = db.relationship("Purchase", backref='product', lazy=True)

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
