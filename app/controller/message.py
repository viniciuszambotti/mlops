from marshmallow import Schema, fields


class ClassifyResponseSchema(Schema):
    message = fields.Str(default='Success')


class ClassifyRequestSchema(Schema):
    api_type = fields.Str(required=True, description="API type of awesome API")
