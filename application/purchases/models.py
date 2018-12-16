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
        stmt = text("SELECT COUNT(purchase.product_id), product.name"
                " FROM purchase"
                " INNER JOIN product on product_id = purchase.product_id"
                " GROUP BY purchase.product_id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"amount" : row[0], "name": row[1]})
        return response


    @staticmethod
    def top_five_customers():
        stmt = text("SELECT COUNT(purchase.account_id), account.name"
                " FROM purchase"
                " INNER JOIN account on account_id = purchase.account_id"
                " GROUP BY purchase.account_id"
                " LIMIT 5")
        res = db.engine.execute(stmt)

        #print(res)

        response = []
        for row in res:
            response.append({"amount" : row[0], "name": row[1]})
        return response

