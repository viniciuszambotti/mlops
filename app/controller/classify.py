from .message import ClassifyResponseSchema, ClassifyRequestSchema, ClassifyError406, ClassifyError500

from flask_restful import Resource, marshal_with
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
import pandas as pd

import pickle
from flask import abort
import os
from dotenv import load_dotenv

# Variáveis de ambiente
load_dotenv()
model_path = os.getenv('MODEl_PATH')
test_path = os.getenv('TEST_PATH')
features = ['mana', 'attack', 'health', 'cat_god', 'cat_type']

class Classify(MethodResource, Resource):

    @doc(description='Faz predição de acordo com o id da carta', tags=['Predictions'])
    @use_kwargs(ClassifyRequestSchema, location=('json'))
    @marshal_with(ClassifyResponseSchema, code=200)
    @marshal_with(ClassifyError406, code=406)
    @marshal_with(ClassifyError500, code=500)
    def post(self, card_id):
        
        '''
            Método post que faz as classificações das cartas
            
            params
                card_id (Int): Número da carta para ser classificado
            
            returns
                - Classificação (early ou late)
            
        '''

        # abre arquivo de modelo e teste
        try:
            with open(model_path, 'rb') as handle:
                ml_model = pickle.load(handle)
            
            with open(test_path, 'rb') as handle:
                df_test = pickle.load(handle)

        except Exception as e:
            abort(500, f'Erro na leitura dos arquivos: {e}')

        
        
        value = df_test.query('id == @card_id')[features] # faz a predição

        if value.shape[0] < 1:
            abort(406, 'Não encontrou a carta')

        try:
            pred = ml_model.predict(value)[0]
        except Exception as e:
            abort(500, f'Erro na predição: {e}')

        if pred ==0:
            pred = 'early'
        else:
            pred = 'late'

        return {'card_classification': pred, 'status':200}


    @doc(description='Faz predição de todas as cartas do arquivo de teste', tags=['Predictions'])
    @marshal_with(ClassifyResponseSchema, code=200)
    @marshal_with(ClassifyError500, code=500)
    def get(self):
        
        '''
            Método get que faz as classificações de todas as cartas
            
            params
            
            returns
                - Lista com os ids e classificações (late ou early)
            
        '''

        # abre arquivo de modelo e teste
        try:
            with open(model_path, 'rb') as handle:
                ml_model = pickle.load(handle)
            
            with open(test_path, 'rb') as handle:
                df_test = pickle.load(handle)

        except Exception as e:
            abort(500, f'Erro na leitura dos arquivos: {e}')
        

        try:
            preds = ml_model.predict(df_test[features]) #faz predições
            ids = df_test['id']

        except Exception as e:
            abort(500, f'Erro na predição: {e}')

        # cria json com predições Ex:{id_carta:0, startegy:early}
        try:
            predictions = pd.DataFrame()
            predictions['id'] = ids
            predictions['strategy'] = preds

            predictions['strategy'] = predictions['strategy'].apply(lambda x: 'early' if x == 0 else 'late')

            value = predictions.to_json(orient='records')[1:-1].replace('},{', '} {')

        except Exception as e:
            abort(500, f'Erro na formatação dos dados: {e}')

        return {'card_classification': value, 'status':200}

