#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


# In[ ]:


def model_split_(df_train,df_validate,df_test):
    x_train = df_train.select_dtypes(exclude=['object']).drop(columns=['is_recession'])
    y_train = df_train.select_dtypes(exclude=['object']).is_recession

    x_validate = df_validate.select_dtypes(exclude=['object']).drop(columns=['is_recession'])
    y_validate = df_validate.select_dtypes(exclude=['object']).is_recession

    x_test = df_test.select_dtypes(exclude=['object']).drop(columns=['is_recession'])
    y_test = df_test.select_dtypes(exclude=['object']).is_recession
    return x_train, y_train, x_validate, y_validate,x_test,y_test


# In[2]:


def modeling(x_train, y_train, x_validate, y_validate):
    logrreg_m= LogisticRegression(random_state=123)
    dectre_m = DecisionTreeClassifier(max_depth=5, random_state=123)
    ranfor_m = RandomForestClassifier(max_depth=6, random_state=123)
    knn_m= KNeighborsClassifier(n_neighbors=20, weights='uniform')
    models = [logrreg_m, dectre_m, ranfor_m, knn_m]
    for model in models:
        model.fit(x_train, y_train)
        actual_train = y_train
        pred_train = model.predict(x_train)
        actual_val = y_validate
        pred_val = model.predict(x_validate)
        print(model)
        print('                           ')
        print('train score: ')
        print(classification_report(actual_train, pred_train))
        print('val score: ')
        print(classification_report(actual_val, pred_val))
        print('                        ')
    return logrreg_m, dectre_m, ranfor_m, knn_m


# In[ ]:




