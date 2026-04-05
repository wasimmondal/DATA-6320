#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def add_dummy(a, b):
    result = a + b
    return result



def dummy_drop(df, feature):

    #Find the highest count category
    
    get_ipython().system('pip install --quiet pandas')
    import pandas as pd
    
    df_dummy = pd.DataFrame(df[feature].value_counts().reset_index())
    var_dummy = df_dummy.iloc[0, 0]

    #Create variable to drop the highest count column
    var_dumpre = feature + "_" +  var_dummy

    #Create dummy variables
    dummies = pd.get_dummies(df[feature], drop_first = False, prefix=feature)

    #Drop the highest count dummy variable
    dummies = dummies.drop(var_dumpre, axis = 1)

    display(df_dummy)
    print("----------------------")
    print("Highest Count:")
    print(var_dummy)
    print("----------------------")

    display(dummies.head())
    
    #Concat the dummy variables to the main dataset
    df = pd.concat([df, dummies], axis = 1)
    return(df)


# In[ ]:


def dummy_nodrop(df, feature):

    get_ipython().system('pip install --quiet pandas')
    import pandas as pd
    
    #Create dummy variables
    
    dummies = pd.get_dummies(df[feature], drop_first = False, prefix=feature)

    display(dummies.head())
    
    #Concat the dummy variables to the main dataset
    df = pd.concat([df, dummies], axis = 1)
    return(df)

