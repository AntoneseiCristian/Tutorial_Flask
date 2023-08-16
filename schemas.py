from marshmallow import Schema, fields


class BaseProdusSchema(Schema):
    id = fields.Str(dump_only=True)
    nume = fields.Str(required=True)
    pret = fields.Float(required=True)

class BaseMagazinSchema(Schema):
    id = fields.Str(dump_only=True)
    nume = fields.Str()

class ProdusSchema(BaseProdusSchema):
    magazin_id = fields.Int(required=True, load_only=True)
    magazin = fields.Nested(BaseMagazinSchema(), dump_only=True)

class ProdusUpdateSchema(Schema):
    nume = fields.Str()
    pret = fields.Float()
    produs_id = fields.Int()

class MagazinSchema(BaseMagazinSchema):
    produse = fields.List(fields.Nested(BaseProdusSchema()), dump_only=True)