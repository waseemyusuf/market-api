from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    inventory_count = db.Column(db.Integer, nullable=False)

    def purchase(self, quantity=1):
        if self.inventory_count >= quantity:
            self.inventory_count -= quantity