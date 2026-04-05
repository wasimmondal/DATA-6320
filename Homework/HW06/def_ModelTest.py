#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def modeltraintest(vartrain, vartest, y_train, y_test, model):

    get_ipython().system('pip install scikit-learn')
    from sklearn.tree import DecisionTreeClassifier # to build a classification tree
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import AdaBoostClassifier

    from sklearn.model_selection import cross_val_score # for cross validation
    from sklearn.metrics import confusion_matrix, classification_report # to create a confusion matrix and classification report
    from sklearn.metrics import ConfusionMatrixDisplay # to draw a confusion matrix
    from sklearn.metrics import precision_score, recall_score, f1_score
    from sklearn.metrics import roc_curve, roc_auc_score
    
    get_ipython().system('pip install matplotlib')
    import matplotlib.pyplot as plt 
    
    #1) Set the properties for the model (model) - by setting vartrain, vartest, and model
    
    
    #2) Fit the model with training data
    model.fit(vartrain, y_train)

    #3) Predict the target variable with test data
    model_pred = model.predict(vartest)
    model_prob = model.predict_proba(vartest)

    #4) Assess the accuracy with the test data
    score = model.score(vartest, y_test)

    print('XXXXXXXXXXXXXXXX ACCURACY SCORE XXXXXXXXXXXXXXXXXX')
    print(round(score, 6))
    print("")


    print('XXXXXXXXXXXXXXXX CONFUSION MATRIX XXXXXXXXXXXXXXXX')
    print(confusion_matrix(y_test, model_pred))
    print("")


    print('XXXXXXXXXXXXXX CLASSIFICATION REPORT XXXXXXXXXXXXXX')
    print(classification_report(y_test, model_pred))
    print('')


    print('XXXXXXXXXXXXXX ROC AUC SCORE AND CHART XXXXXXXXXXXXXXXXXX')
    print('')
    y_pred_prob = model.predict_proba(vartest)[:,1]

    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

    plt.plot([0, 1], [0, 1],'k--')
    plt.plot(fpr, tpr, label='Classification Model')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.show();

    # calculate roc curve
    y_pred_prob = model.predict_proba(vartest)[:,1]
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    roc_auc = roc_auc_score(y_test, y_pred_prob)
    roc_auc_format = 'ROC AUC Score: {0:.4f}'.format(roc_auc)
    print(roc_auc_format)
    print('')


    print('XXXXXXXXXXXXXX CROSS VALIDATION XXXXXXXXXXXXXXXXXX')
    print('')
    cv_scores = cross_val_score(model, vartrain, y_train, cv=5,
    scoring='accuracy')
    print('CV Accuracy Scores:')
    print(cv_scores)
    print('')
    cv_rocauc = cross_val_score(model, vartrain, y_train, cv=5,
    scoring='roc_auc')
    print('CV ROC AUC:')
    print(cv_rocauc)

    print('')
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


# In[ ]:


def shorttraintest(vartrain, vartest, y_train, y_test, model):

    
    get_ipython().system('pip install --quiet scikit-learn')
    from sklearn.tree import DecisionTreeClassifier # to build a classification tree
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import AdaBoostClassifier

    from sklearn.model_selection import cross_val_score # for cross validation
    from sklearn.metrics import confusion_matrix, classification_report # to create a confusion matrix and classification report
    from sklearn.metrics import ConfusionMatrixDisplay # to draw a confusion matrix
    from sklearn.metrics import precision_score, recall_score, f1_score
    from sklearn.metrics import roc_curve, roc_auc_score

    get_ipython().system('pip install --quiet matplotlib')
    import matplotlib.pyplot as plt 
    
    #Fit the model
    model.fit(vartrain, y_train)

    #Predict with the model
    model_pred = model.predict(vartest)
    model_prob = model.predict_proba(vartest)

    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print('Confusion Matrix:')
    print(confusion_matrix(y_test, model_pred))
    print("")

    #Assess with the model
    score = model.score(vartest, y_test)
    score_format = 'Accuracy Score: {0:.4f}'.format(score)
    print(score_format)

    recall = recall_score(y_test, model_pred)
    recall_format = 'Recall Score: {0:.4f}'.format(recall)
    print(recall_format)
    
    precision = precision_score(y_test, model_pred)
    precision_format = 'Precision Score: {0:.4f}'.format(precision)
    print(precision_format)
    
    # calculate roc curve
    y_pred_prob = model.predict_proba(vartest)[:,1]
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    roc_auc = roc_auc_score(y_test, y_pred_prob)
    roc_auc_format = 'ROC AUC Score: {0:.4f}'.format(roc_auc)
    print(roc_auc_format)
    print('')

