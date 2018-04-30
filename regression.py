# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:44:04 2017

@author: 21574
"""

import pandas as pd
df0 = pd.read_csv('output1.csv')
df1 = pd.read_csv('star rating.csv')

data = pd.concat([df1['Cat'], df0, df1['star']], axis = 1)
# data.to_csv('project data.csv')

# split dataset by food type
f1, f2, f3, f4, f5, f6 = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
for i in range(10601):
    if 'Chinese' in data.loc[i,'Cat']: f1 = f1.append(data[i:i+1])
    if 'Mexican' in data.loc[i,'Cat']: f2 = f2.append(data[i:i+1])
    if 'American' in data.loc[i,'Cat']: f3 = f3.append(data[i:i+1])
    if 'Japanese' in data.loc[i,'Cat']: f4 = f4.append(data[i:i+1])
    if 'Canadian' in data.loc[i,'Cat']: f5 = f5.append(data[i:i+1])
    if 'French' in data.loc[i,'Cat']: f6 = f6.append(data[i:i+1])

##############################################################################
# get Linear Regression parameters
from sklearn.linear_model import LinearRegression
# analyzing with all data
x = data.drop(['Cat', 'star'], axis = 1)
y = data['star']

lin = LinearRegression()
lin.fit(x, y)
predictions = {}
predictions['intercept'] = lin.intercept_
predictions['coefficient'] = lin.coef_
# {'coefficient': array([  2.88339223e-01,   1.45235597e+00,  
#                         -1.05422501e-03,    3.89908068e-02]), 
# 'intercept': 1.9956853507490262}
#############################################################################
# analyzing data by different types of retuarants
# Chinese 
x1 = f1.drop(['Cat', 'star'], axis = 1)
y1 = f1['star']
lin1 = LinearRegression()
lin1.fit(x1, y1)
predictions1 = {}
predictions1['intercept'] = lin1.intercept_
predictions1['coefficient'] = lin1.coef_
# {'coefficient': array([  -0.02961077,  1.67012532,  
#                         0.44129326,  0.13327907]), 
# 'intercept': 1.6526356142188894}

#Mexican
x2 = f2.drop(['Cat', 'star'], axis = 1)
y2 = f2['star']
lin2 = LinearRegression()
lin2.fit(x2, y2)
predictions2 = {}
predictions2['intercept'] = lin2.intercept_
predictions2['coefficient'] = lin2.coef_
# {'coefficient': array([  0.33737792,  1.37745071,  
#                         1.61453565, -0.11701442]), 
# 'intercept': 2.1250280611149241}

# American
x3 = f3.drop(['Cat', 'star'], axis = 1)
y3 = f3['star']
lin3 = LinearRegression()
lin3.fit(x3, y3)
predictions3 = {}
predictions3['intercept'] = lin3.intercept_
predictions3['coefficient'] = lin3.coef_
# {'coefficient': array([  0.54835081,  0.28064534,  
#                         0.        , -0.03131438]), 
# 'intercept': 3.370051274987687}

# Japanese
x4 = f4.drop(['Cat', 'star'], axis = 1)
y4 = f4['star']
lin4 = LinearRegression()
lin4.fit(x4, y4)
predictions4 = {}
predictions4['intercept'] = lin4.intercept_
predictions4['coefficient'] = lin4.coef_
# {'coefficient': array([  0.38898261,  2.42483743,  
#                         -0.90128308,  0.05888587]), 
# 'intercept': 1.0855210808636606}

# Canadian
x5 = f5.drop(['Cat', 'star'], axis = 1)
y5 = f5['star']
lin5 = LinearRegression()
lin5.fit(x5, y5)
predictions5 = {}
predictions5['intercept'] = lin5.intercept_
predictions5['coefficient'] = lin5.coef_
# {'coefficient': array([  0.4739597 ,  0.        ,  
#                         0.        ,  0.21015441]), 
# 'intercept': 3.8045014394137664}

# French
x6 = f6.drop(['Cat', 'star'], axis = 1)
y6 = f6['star']
lin6 = LinearRegression()
lin6.fit(x6, y6)
predictions6 = {}
predictions6['intercept'] = lin6.intercept_
predictions6['coefficient'] = lin6.coef_
# {'coefficient': array([  0.55943782,  0.2527038 ,  
#                         -0.24279749,  0.04705491]), 
# 'intercept': 3.4966532116960578}

##############################################################################
# get Logistic Regression parameters
from sklearn.linear_model import LogisticRegression
log0 = LogisticRegression()
log0.fit(x, y)
pre0 = {}
pre0['intercept'] = log0.intercept_
pre0['coefficient'] = log0.coef_
'''{'coefficient': array([[-0.41103898, -1.92013168, -0.21326416,  0.29488427],
        [-0.43808311, -0.38645995,  0.11158426, -0.13208866],
        [ 0.01257495,  0.52160017, -0.1709242 , -0.46601833],
        [ 0.12311214,  0.71969529,  0.55330668, -0.18119082],
        [ 0.26142541,  1.08379051, -0.37752754,  0.31613955]]),
'intercept': array([ 0.06685767, -1.61089851, -2.0238085 , -1.62459855, -2.04799995])}'''
###########################################################################
# analysing by food types
# Chinese
log1 = LogisticRegression()
log1.fit(x1, y1)
pre1 = {}
pre1['intercept'] = log1.intercept_
pre1['coefficient'] = log1.coef_
'''{'coefficient': array([[-0.03540752, -1.95875271, -0.65923651,  0.18475713],
        [-0.17326531, -0.77248125,  0.21271311, -0.32381952],
        [ 0.27606639,  0.67770863, -0.68726327, -0.43646713],
        [ 0.04389843,  0.76031569,  1.1616819 , -0.07241861],
        [-0.21609876,  0.62140666, -0.40139025,  0.39772299]]),
 'intercept': array([ 0.22029326, -1.12346599, -2.03633851, -1.69761479, -1.79268216])}'''

# Mexican
log2 = LogisticRegression()
log2.fit(x2, y2)
pre2 = {}
pre2['intercept'] = log2.intercept_
pre2['coefficient'] = log2.coef_
'''{'coefficient': array([[-0.43700778, -1.62378968, -0.17978176,  0.48125046],
        [-0.37267471, -0.43164057, -0.107562  ,  0.08174547],
        [ 0.03854531,  0.19850176, -0.09144436, -0.58854358],
        [ 0.04449257,  0.39128924, -0.19067727, -0.29624227],
        [ 0.33306231,  1.07725339,  0.52732705,  0.17791946]]),
 'intercept': array([-0.19124746, -1.65629451, -1.81364805, -1.34498485, -1.88368831])}'''

# American
log3 = LogisticRegression()
log3.fit(x3, y3)
pre3 = {}
pre3['intercept'] = log3.intercept_
pre3['coefficient'] = log3.coef_
'''{'coefficient': array([[ 0.0376863 , -0.9488847 ,  0.        ,  0.17058625],
        [-1.1573474 , -0.84461491,  0.        ,  0.15250427],
        [-0.85558161, -0.5586428 ,  0.        , -0.390708  ],
        [-0.39112679, -0.41324559,  0.        , -0.26697417],
        [ 0.91592204, -0.15361285,  0.        ,  0.18325976]]),
 'intercept': array([-1.10209039, -1.34046424, -1.0297254 , -0.46929351, -0.50595112])}'''

# Japanese
log4 = LogisticRegression()
log4.fit(x4, y4)
pre4 = {}
pre4['intercept'] = log4.intercept_
pre4['coefficient'] = log4.coef_
'''{'coefficient': array([[-0.52497914, -2.40737664,  0.83538478,  0.32693898],
        [-0.71306438, -0.40831973, -0.32919688, -0.32941102],
        [-0.1996441 , -0.10655347,  0.18472575, -0.30030193],
        [ 0.34736021,  0.27603826, -0.26928902, -0.20074473],
        [ 0.22700161,  0.69197983, -0.35799436,  0.30317068]]),
 'intercept': array([ 0.38138832, -1.51687412, -1.46867244, -1.10747206, -1.60641046])}'''

# Canadian
log5 = LogisticRegression()
log5.fit(x5, y5)
pre5 = {}
pre5['intercept'] = log5.intercept_
pre5['coefficient'] = log5.coef_
'''{'coefficient': array([[-0.39748586, -1.32587554,  0.        ,  0.32220662],
        [-0.30722265, -1.12490877,  0.        , -0.8312779 ],
        [-0.57337264, -0.60937748,  0.        , -1.00337793],
        [ 0.65496117, -0.40680807,  0.        ,  0.09797211],
        [ 0.00767866, -0.30445918,  0.        ,  0.4281771 ]]),
 'intercept': array([-1.32587554, -1.12490877, -0.60937748, -0.40680807, -0.30445918])}'''

# French
log6 = LogisticRegression()
log6.fit(x6, y6)
pre6 = {}
pre6['intercept'] = log6.intercept_
pre6['coefficient'] = log6.coef_
'''{'coefficient': array([[-1.07502902, -1.02580459, -0.26361667,  0.08450217],
        [-0.79650251, -0.48823696,  0.36009561,  0.09856577],
        [-0.35750752, -0.9081871 ,  0.20597731, -0.4164329 ],
        [-0.2364886 , -0.15059017,  0.18582584, -0.16398579],
        [ 0.78891707,  0.11916479, -0.38578147,  0.23820956]]),
 'intercept': array([-1.46324518, -1.75861836, -0.59605609, -0.59195669, -0.79653941])}'''

###############################################################################
# Data visualization
import seaborn as sns
sns.set(color_codes=True)
# all data
sns.regplot(x = 'ambience', y='star', data = data)
sns.regplot(x = 'food', y='star', data = data)
sns.regplot(x = 'price', y='star', data = data)
sns.regplot(x = 'service', y='star', data = data)
sns.regplot(x='star', y='ambience', data=data, logistic=True)
sns.regplot(x='star', y='food', data=data, logistic=True)
sns.regplot(x='star', y='price', data=data, logistic=True)
sns.regplot(x='star', y='service', data=data, logistic=True)

# Chinese food
sns.regplot(x = 'ambience', y='star', data = f1)
sns.regplot(x = 'food', y='star', data = f1)
sns.regplot(x = 'price', y='star', data = f1)
sns.regplot(x = 'service', y='star', data = f1)
sns.regplot(x='star', y='ambience', data=f1, logistic=True)
sns.regplot(x='star', y='food', data=f1, logistic=True)
sns.regplot(x='star', y='price', data=f1, logistic=True)
sns.regplot(x='star', y='service', data=f1, logistic=True)

# Mexican food
sns.regplot(x = 'ambience', y='star', data = f2)
sns.regplot(x = 'food', y='star', data = f2)
sns.regplot(x = 'price', y='star', data = f2)
sns.regplot(x = 'service', y='star', data = f2)
sns.regplot(x='star', y='ambience', data=f2, logistic=True)
sns.regplot(x='star', y='food', data=f2, logistic=True)
sns.regplot(x='star', y='price', data=f2, logistic=True)
sns.regplot(x='star', y='service', data=f2, logistic=True)

# American food
sns.regplot(x = 'ambience', y='star', data = f3)
sns.regplot(x = 'food', y='star', data = f3)
sns.regplot(x = 'price', y='star', data = f3)
sns.regplot(x = 'service', y='star', data = f3)
sns.regplot(x='star', y='ambience', data=f3, logistic=True)
sns.regplot(x='star', y='food', data=f3, logistic=True)
sns.regplot(x='star', y='price', data=f3, logistic=True)
sns.regplot(x='star', y='service', data=f3, logistic=True)

# Japanese food
sns.regplot(x = 'ambience', y='star', data = f4)
sns.regplot(x = 'food', y='star', data = f4)
sns.regplot(x = 'price', y='star', data = f4)
sns.regplot(x = 'service', y='star', data = f4)
sns.regplot(x='star', y='ambience', data=f4, logistic=True)
sns.regplot(x='star', y='food', data=f4, logistic=True)
sns.regplot(x='star', y='price', data=f4, logistic=True)
sns.regplot(x='star', y='service', data=f4, logistic=True)

# Canadian food
sns.regplot(x = 'ambience', y='star', data = f5)
sns.regplot(x = 'food', y='star', data = f5)
sns.regplot(x = 'price', y='star', data = f5)
sns.regplot(x = 'service', y='star', data = f5)
sns.regplot(x='star', y='ambience', data=f5, logistic=True)
sns.regplot(x='star', y='food', data=f5, logistic=True)
sns.regplot(x='star', y='price', data=f5, logistic=True)
sns.regplot(x='star', y='service', data=f5, logistic=True)

# French food
sns.regplot(x = 'ambience', y='star', data = f6)
sns.regplot(x = 'food', y='star', data = f6)
sns.regplot(x = 'price', y='star', data = f6)
sns.regplot(x = 'service', y='star', data = f6)
sns.regplot(x='star', y='ambience', data=f6, logistic=True)
sns.regplot(x='star', y='food', data=f6, logistic=True)
sns.regplot(x='star', y='price', data=f6, logistic=True)
sns.regplot(x='star', y='service', data=f6, logistic=True)