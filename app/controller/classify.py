from .message import ClassifyResponseSchema, ClassifyRequestSchema

from flask_restful import Resource, marshal_with
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs





#  Restful way of creating APIs through Flask Restful
class Classify(MethodResource, Resource):
    @doc(description='My First GET Awesome API.', tags=['Awesome'])
    @marshal_with(ClassifyResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        return {'messsage': 'My First Awesome API'}


    @doc(description='My First GET Awesome API.', tags=['Awesome'])
    @marshal_with(ClassifyResponseSchema)  # marshalling
    @use_kwargs(ClassifyRequestSchema, location=('json'))
    def post(self, api_type):
        '''
        Get method represents a GET API method
        '''
        return {'message': api_type}

