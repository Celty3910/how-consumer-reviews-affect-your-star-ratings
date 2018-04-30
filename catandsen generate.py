
# coding: utf-8

# In[1]:


# import data
import pandas as pd
df1 = pd.read_csv('output1.csv')
df2 = pd.read_csv('output2.csv')
df3 = pd.read_csv('stars only.csv')
df4 = pd.read_csv('reviews+categories.csv')

###############################################################################
# replace 1 under categories by sentiment values
sen = df2['positive']
rate = sen.replace(to_replace=0, value=2)

amb, foo, pri, ser = df1['ambience'], df1['food'], df1['price'], df1['service']
l1, l2, l3, l4 = [], [], [], []
for i in range(len(df1)):
    if amb[i] == 1: l1.append(rate[i])
    else: l1.append(amb[i])
    if foo[i] == 1: l2.append(rate[i])
    else: l2.append(foo[i])
    if pri[i] == 1: l3.append(rate[i])
    else: l3.append(pri[i])
    if ser[i] == 1: l4.append(rate[i])
    else: l4.append(ser[i])
l1, l2, l3, l4 = pd.DataFrame(l1),pd.DataFrame(l2),pd.DataFrame(l3),pd.DataFrame(l4)
catsen = pd.concat([l1,l2,l3,l4],axis = 1)
catsen.columns = ['ambience', 'food', 'price', 'service']
catsen.to_csv('project data.csv', index = None)

