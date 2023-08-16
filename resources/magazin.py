from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import MagazinModel
from schemas import MagazinSchema, ProdusSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
blp = Blueprint("Magazine", "magazine", description="Operatii pe magazine")


@blp.route("/magazin/<string:magazin_id>")
class Magazin(MethodView):
    @blp.response(200, MagazinSchema)
    def get(self, magazin_id):
        magazin = MagazinModel.query.get_or_404(magazin_id)
        return magazin

    def delete(self, magazin_id):
        magazin = MagazinModel.query.get_or_404(magazin_id)
        db.session.delete(magazin)
        db.session.commit()
        return {"message": "Magazinul a fost sters"}

@blp.route("/magazin")
class MagazinList(MethodView):
    @blp.response(200, ProdusSchema(many=True))
    def get(self):
        return MagazinModel.query.all()

    @blp.arguments(MagazinSchema)
    @blp.response(201, MagazinSchema)
    def post(self, magazin_data):
        magazin = MagazinModel(**magazin_data)
        try:
            db.session.add(magazin)
            db.session.commit()
        except IntegrityError:
            abort(400, message = "Un magazin cu acest nume exista deja")
        except SQLAlchemyError:
            abort(500, message = "A fost intampinata o eroare la crearea unui magazin." )

        return magazin
