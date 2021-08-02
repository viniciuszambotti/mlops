from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with

from .controller.classify import Classify

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


app = Flask(__name__)

api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Luiza labs',
        version='v1.0',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',   
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  
})
docs = FlaskApiSpec(app)



api.add_resource(Classify, '/classify')
docs.register(Classify)
