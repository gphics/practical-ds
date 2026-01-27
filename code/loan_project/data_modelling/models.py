#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 18:16:34 2026

@author: xenon
"""
from feature_transformation import X_train, X_test, y_train, y_test
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

selected_cols = ['previous_loan_defaults_on_file_Yes', 'person_income', 'loan_percent_income', 'loan_int_rate',
                 'person_home_ownership_RENT', 'loan_amnt', 'person_home_ownership_OTHER', 'person_home_ownership_OWN']

# creating logistic regression model
logit = LogisticRegression()
logit.fit(X_train, y_train)

# making predictions
logit_pred = logit.predict(X_test)

# getting metrics
logit_report = classification_report(y_test, logit_pred)
# print("Logistic regression model")
# print(logit_report)

# creating random forest model
rforest = RandomForestClassifier()
rforest.fit(X_train, y_train)

# making predictions
rforest_pred = rforest.predict(X_test)

# getting metrics
rforest_report = classification_report(y_test, rforest_pred)
# print("Random forest model")
# print(rforest_report)
