from application import db
from application.models import Base
from sqlalchemy.sql import text

class Purchase(Base):

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'),
                           nullable=False)
    @staticmethod
    def most_purchased_products():
        stmt = text("SELECT COUNT(purchase.product_id), name, purchase.product_id"
                " FROM purchase"
                " INNER JOIN product on product_id = purchase.product_id"
                " GROUP BY purchase.product_id, name")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"amount" : row[0], "name": row[1]})
        return response

    
    @staticmethod
    def top_five_customers():
        stmt = text("SELECT COUNT(purchase.account_id), name, purchase.account_id"
                " FROM purchase"
                " INNER JOIN account on account_id = purchase.account_id"
                " GROUP BY purchase.account_id, name"
                " LIMIT 5")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"amount" : row[0], "name": row[1]})
        return response

