from application import db
from application.models import Base

class Purchase(Base):

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'),
                           nullable=False)
