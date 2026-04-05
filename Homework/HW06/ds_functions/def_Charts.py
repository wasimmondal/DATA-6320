#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def heatmap (vardata):
    
    get_ipython().system('pip install --quiet matplotlib')
    import matplotlib.pyplot as plt 
    get_ipython().system('pip install --quiet seaborn')
    import seaborn as sns
    colormap = plt.cm.viridis
    plt.figure(figsize=(14,12))
    sns.heatmap(vardata.astype(float).corr(),linewidths=0.1,vmax=1.0, vmin=0, square=True, cmap=colormap, linecolor='white', annot=True)


# In[ ]:


def pairplot (vardata):
    
    get_ipython().system('pip install --quiet matplotlib')
    import matplotlib.pyplot as plt 
    get_ipython().system('pip install --quiet seaborn')
    import seaborn as sns
    sns.pairplot(vardata)
    


# In[ ]:


def pairplot_hue (vardata, varhue):
    
    get_ipython().system('pip install --quiet matplotlib')
    import matplotlib.pyplot as plt 
    get_ipython().system('pip install --quiet seaborn')
    import seaborn as sns
    sns.pairplot(vardata, hue = varhue)


# In[ ]:


def scatterplot (varx, vary, vardata):
    
    get_ipython().system('pip install --quiet matplotlib')
    import matplotlib.pyplot as plt 
    get_ipython().system('pip install --quiet seaborn')
    import seaborn as sns
    
    sns.set(style='whitegrid')
    plt.figure(figsize=(20,10)) #changes area of scatterplot
    sns.scatterplot(x=varx, y=vary, data=vardata, alpha=.5, s = 250, edgecolor='white', linewidth=2)
    plt.title('Seaborn Scatter plot', color = 'green', fontsize='18')
    plt.show()

# In[ ]:


def scatterplot_hue (varx, vary, varhue, vardata):
    
    get_ipython().system('pip install --quiet matplotlib')
    import matplotlib.pyplot as plt 
    get_ipython().system('pip install --quiet seaborn')
    import seaborn as sns
    
    sns.set(style='whitegrid')
    plt.figure(figsize=(20,10)) #changes area of scatterplot
    sns.scatterplot(x=varx, y=vary, data=vardata, alpha=.5, s = 250, edgecolor='white', linewidth=2, hue=varhue)
    plt.title('Seaborn Scatter plot', color = 'green', fontsize='18')
    plt.show()
# In[ ]:


def boxplot (varx, vary, vardata):
    
    get_ipython().system('pip install --quiet matplotlib')
    import matplotlib.pyplot as plt 
    get_ipython().system('pip install --quiet seaborn')
    import seaborn as sns
    
    plt.figure(figsize=(20,8))
    chart = sns.boxplot(y = vary, x = varx, data = vardata, palette = 'coolwarm')
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90, fontsize='17')

