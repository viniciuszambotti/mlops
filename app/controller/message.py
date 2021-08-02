from marshmallow import Schema, fields


class ClassifyResponseSchema(Schema):
    card_classification = fields.Str(default='Success')

class ClassifyRequestSchema(Schema):
    card_id = fields.Int(required=True, description="Id do card para ser classificado")

class ClassifyError406(Schema):
    error = fields.String(required=True, description="Não encontrou a carta")

class ClassifyError500(Schema):
    error = fields.String(required=True, description="mensagem de erro")
