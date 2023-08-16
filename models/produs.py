from db import db

class ProdusModel(db.Model):
    __tablename__ = "produse"

    id = db.Column(db.Integer, primary_key = True)
    nume = db.Column(db.String(80), unique = True, nullable = False)
    pret = db.Column(db.Float(precision=2), unique = False, nullable = False)
    magazin_id = db.Column(db.Integer, db.ForeignKey("magazin.id"), unique = False, nullable = False)
    magazin = db.relationship("MagazinModel", back_populates = "produse")