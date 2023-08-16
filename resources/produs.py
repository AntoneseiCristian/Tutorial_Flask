from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ProdusModel
from db import db
from schemas import ProdusSchema, ProdusUpdateSchema
from sqlalchemy.exc import SQLAlchemyError
blp = Blueprint("Produse", "produse", description="Operatii pe produse")


@blp.route("/produs/<string:produs_id>")
class Produs(MethodView):
    @blp.response(200, ProdusSchema)
    def get(self, produs_id):
        produs = ProdusModel.query.get_or_404(produs_id)
        return produs
    def delete(self, produs_id):
        produs = ProdusModel.query.get_or_404(produs_id)
        db.session.delete(produs)
        db.session.commit()
        return {"message": "Produsul a fost sters"}


    @blp.arguments(ProdusUpdateSchema)
    @blp.response(200, ProdusSchema)
    def put (self, produs_data, produs_id):
        produs = ProdusModel.querry.get(produs_id)
        if produs:
            produs.pret = produs_data["pret"]
            produs.id = produs_data["nume"]
        else:
            produs = ProdusModel(id = produs_id, **produs_data)

        db.session.add(produs)
        db.session.commit()

        return produs


    @blp.route("/produs")
    class ProdusList(MethodView):
        @blp.response(200, ProdusSchema(many=True))
        def get(self):
            return ProdusModel.query.all()

        @blp.arguments(ProdusSchema)
        @blp.response(201, ProdusSchema)
        def post(self, produs_data):
            produs = ProdusModel(**produs_data)

            try:
                db.session.add(produs)
                db.session.commit()
            except SQLAlchemyError:
                abort(500, message="Inserarea unui element a produs o eroare")

            return produs

