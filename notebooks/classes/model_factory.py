import pandas as pd
import numpy as np

from sklearn import metrics

from sklearn import model_selection
from sklearn.metrics import confusion_matrix, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC

'''
    Classe com propósito de trainar modelos de classificação do sk learn
'''

class ModelFactory():
    
    '''
        Construtor que recebe o nome do modelo, o objeto sk learn, parâmetros para o gridseach tunar 
        o os hiperparâmetros e o tipo de métrica a ser levada em consideração
    '''
    def __init__(self, model_name, model, params = None, score = None):
        self.model_name = model_name
        self.model = model
        self.params = params
        self.score = score
    
    '''
        Usa gridSearch para achar os melhores parâmetros para o modelo e faz as predições
        
        params
            X_train (DataFrame): conjunto de features para treino
            y_train (DataFrame): variável target para predição do treino 
            X_teste (DataFrame): conjunto de features para teste
            y_teste (DataFrame): variável target para predição do teste
        
        returns
            - melhor modelo encontrado
            - predições
        
    '''
    def classify(self, X_train, y_train, X_test, y_test):

        grid_search = model_selection.GridSearchCV(estimator= self.model, param_grid= self.params, cv=5, scoring=self.score, n_jobs=-1)

        grid_search.fit(X_train, y_train)
        y_pred = grid_search.predict(X_test)

        if hasattr(grid_search, 'predict_proba'):   
            y_score = grid_search.predict_proba(X_test)[:,1]
        elif hasattr(grid_search, 'decision_function'):
            y_score = grid_search.decision_function(X_test)
        else:
            y_score = y_pred

        predictions = {'y_pred' : y_pred, 'y_score' : y_score}
        df_predictions = pd.DataFrame.from_dict(predictions)

        return grid_search.best_estimator_, df_predictions
    
    
    def metrics(self, y_test, y_pred):
        cm = confusion_matrix(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        dict_report = classification_report(y_test, y_pred, output_dict=True)
        print("Matriz de confusão")
        print(cm)
        print('------------------------------------------')
        print(report)
        
        return pd.DataFrame(dict_report).transpose()
        