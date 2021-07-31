from flask_restful import Resource

# from .models import Produto as ProdutoModel
# from .schemas import ProdutoSchema

class Classify(Resource):

    def get(self):
        return 'hello world'
