import pandas as pd
import numpy as np
import json
import pickle

# this file will be a handler "API"
class Cardio_Catch_Diseases(object):
    def __init__(self):
        self.home_path              = ''
        self.age_scaling            = pickle.load(open(self.home_path + 'parameters/age_scaling.pkl', 'rb'))
        self.bmi_scaling            = pickle.load(open(self.home_path + 'parameters/bmi_scaling.pkl', 'rb'))
        self.difference_scaling     = pickle.load(open(self.home_path + 'parameters/difference_scaling.pkl', 'rb'))
        self.height_scaling         = pickle.load(open(self.home_path + 'parameters/height_scaling.pkl', 'rb'))
        self.hight_pressure_scaling = pickle.load(open(self.home_path + 'parameters/hight_pressure_scaling.pkl', 'rb'))
        self.low_pressure_scaling   = pickle.load(open(self.home_path + 'parameters/low_pressure_scaling.pkl', 'rb'))
        self.weight_scaling         = pickle.load(open(self.home_path + 'parameters/weight_scaling.pkl', 'rb'))
        self.gender_encoder         = pickle.load(open(self.home_path + 'parameters/gender_encoder.pkl', 'rb'))


    
    def data_cleaning(self, df_train):
        '''df_train: is the input data from user on website'''


        # height - change centimeters to meters
        df_train['height'] = (df_train['height'] / 100)

        return df_train

    def feature_engineering(self, df_train):
        '''Get the dataframe from data cleaning and create a new features'''


        # feature engineering
        df_train['difference'] = df_train['hight_pressure'] - df_train['low_pressure']
        df_train['convergent'] = df_train['difference'].apply(lambda x: 1 if x <= 30 else 0)
        df_train['divergent'] = df_train['difference'].apply(lambda x: 1 if x >= 60 else 0)
        df_train['bmi'] = (df_train['weight']/(df_train['height'] * df_train['height']))
        df_train['bmi_level'] = df_train['bmi'].apply(lambda x: 
                                                      'underweight' if x <= 18.5 else
                                                      'normal'      if x >  18.5 and x <= 24.9 else
                                                      'overweight'  if x >= 25.0 and x <= 29.9 else
                                                      'obesity')
        df_train['hypertension'] = df_train.apply(lambda x: 1 if x[4] >=140 and x[5] >= 90 else 0, axis=1)
        df_train['hypotension'] = df_train.apply(lambda x: 1 if x[4] <=90 and x[5] <= 60 else 0, axis=1)
        df_train['age_range'] = df_train['age'].apply(lambda x: 'age_0_50'    if x <= 50 
                                                           else 'age_51_59'   if x >= 51 and x <= 59 
                                                           else 'age_60_over' if x >= 60 
                                                           else x)

        df_train['weight_range'] = df_train['weight'].apply(
            lambda x:   0.50 if x <= 50  else
                        0.75 if x >= 51  and x <= 75 else
                        1.00 if x >= 76  and x <= 100 else
                        1.25 if x >= 101 and x <= 125 else
                        1.50 if x >= 126 and x <= 150 else
                        1.75 if x >= 151 and x <= 175 else 2.00)

        # Data Filtering rows, values or columns
        df_train = df_train.drop('id', axis=1)

        return df_train


    def data_rescaling(self, df_train):
        '''
        Rescaling data
        Return: json file with x_test data to input the prediction
        '''


        # Transforming data to will be in correct data scaler to input at model
        df_train['age']            = self.age_scaling.transform(df_train[['age']].values)
        df_train['height']         = self.height_scaling.transform(df_train[['height']].values)
        df_train['weight']         = self.weight_scaling.transform(df_train[['weight']].values)
        df_train['low_pressure']   = self.low_pressure_scaling.transform(df_train[['low_pressure']].values)
        df_train['hight_pressure'] = self.hight_pressure_scaling.transform(df_train[['hight_pressure']].values)
        df_train['difference']     = self.difference_scaling.transform(df_train[['difference']].values)
        df_train['bmi']            = self.bmi_scaling.transform(df_train[['bmi']].values)
        df_train['gender']         = self.gender_encoder.transform(df_train[['gender']].values)
        df_train['age_range']      = df_train['age_range'].map(
            {'age_0_50':1, 'age_51_59':1, 'age_60_over':3})
        df_train['bmi_level']      = df_train['bmi_level'].map(
            {'underweight':1, 'normal':2, 'overweight':3, 'obesity':4})

        # Deleting target
        x_test = df_train.drop('cardio', axis=1).copy()
        #data_json = json.dumps(x_test.to_dict(orient='records')) # converto to json

        return x_test