from marshmallow import Schema, fields

'''
    Cria os schemas que serão usados para validar as chamadas e documentar o swagger
'''

class ClassifyResponseSchema(Schema):
    card_classification = fields.Str(default='Success')

class ClassifyRequestSchema(Schema):
    card_id = fields.Int(required=True, description="Id do card para ser classificado")

class ClassifyError406(Schema):
    error = fields.String(required=True, description="Não encontrou a carta")

class ClassifyError500(Schema):
    error = fields.String(required=True, description="mensagem de erro")
