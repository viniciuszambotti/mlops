from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with

from .controller.classify import Classify

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mock.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.app = app
# db.init_app(app)

# ma.init_app(app)

api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Awesome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)



api.add_resource(Classify, '/classify')
docs.register(Classify)
