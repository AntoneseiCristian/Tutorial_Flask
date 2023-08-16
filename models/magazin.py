from db import db

class MagazinModel(db.Model):
    __tablename__ = "magazin"

    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(80), unique=True, nullable=False)
    produse = db.relationship("ProdusModel", back_populates="magazin", lazy="dynamic", cascade="all, delete")