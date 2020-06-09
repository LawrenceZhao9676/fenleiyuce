#!/usr/bin/env python
# coding: utf-8

# # Video Game Sales 电子游戏销售分析
# 导入所需要的包

# In[29]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import seaborn as sns 
import pyecharts
import datetime
from pyecharts.charts import Pie


# 导入数据，给出数据摘要,并检查完整性

# In[30]:


df=pd.read_csv('./vgsales.csv')
df.info()
print("缺失数据及个数：\n",df.isnull().sum())


# 由于缺失数据不多，所以删除不会影响数据的平衡，在此直接删除有缺失数据的行

# In[31]:


df=df.dropna()
df.info()


# ## 用户喜好游戏类型

# In[35]:


FGE=pd.pivot_table(df,index='Year',columns='Genre',values='Global_Sales',aggfunc=np.sum).sum().sort_values(ascending=False)
FGE=pd.DataFrame(data=FGE,columns={'Genre_sales'})
FGE_near5=pd.pivot_table(df,index='Year',columns='Genre',values='Global_Sales',aggfunc=np.sum).iloc[-5:,:].sum().sort_values(ascending=False)
FGE_near5=pd.DataFrame(data=FGE_near5,columns={'Genre_sales'})
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(12,6))
sns.barplot(x=FGE.index,y='Genre_sales',data=FGE,ax=ax1)
sns.barplot(x=FGE_near5.index,y='Genre_sales',data=FGE_near5,ax=ax2)


# 动作类游戏一直占据榜首，射击类游戏超过了运动类游戏

# ## 用户喜欢的游戏平台

# In[36]:


FPF=pd.pivot_table(df,index='Year',columns='Platform',values='Global_Sales',aggfunc=np.sum).sum().sort_values(ascending=False)
FPF=pd.DataFrame(data=FPF,columns={'Global_Sales'})
FPF_near5=pd.pivot_table(df,index='Year',columns='Platform',values='Global_Sales',aggfunc=np.sum).iloc[-5:,:].sum().sort_values(ascending=False)
FPF_near5=pd.DataFrame(data=FPF_near5,columns={'Global_Sales'})
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(12,6))
sns.barplot(x=FPF.index,y='Global_Sales',data=FPF,ax=ax1)
sns.barplot(x=FPF_near5.index,y='Global_Sales',data=FPF_near5,ax=ax2)


# 随着时代的变化，最喜欢的平台由PS2变为了PS4，但是X360仍然在占有不少份额

# ## 游戏市场发展趋势

# In[39]:


M=['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']
#绘制各地区销量走势图
df5market_p=pd.pivot_table(df,index='Year',values=M,aggfunc=np.sum)
fig=plt.figure(figsize=(10,6))
sns.lineplot(data=df5market_p)
plt.title('五大市场发展趋势')


# # 五大发行商的历史销售情况

# In[40]:


P=['Nintendo','Electronic Arts','Activision','Sony Computer Entertainment','Ubisoft']
df5PBL=df[df['Publisher'].isin(P)]
df5PBL_p=pd.pivot_table(data=df5PBL,index='Year',columns='Publisher',values='Global_Sales',aggfunc=np.sum)
df5PBL_p.plot(title='五大发行商历史销售情况',figsize=(12,6))


# # 五大发行商的市场占额

# In[44]:


PBL_near5_5p=df[(df['Year']>2013)&(df['Publisher'].isin(P))]
PBL_near5_5p_G_M_p=pd.pivot_table(data=PBL_near5_5p,index=['Genre','Publisher'],values=M,aggfunc=np.sum)
PBL_near5_5p_G_M_p_pct=PBL_near5_5p_G_M_p.div(PBL_near5_5p_G_M_p.groupby(level=0).sum()).round(2)
PBL_near5_5p_G_M_p_pct=PBL_near5_5p_G_M_p_pct.sort_values(by=['Genre','Global_Sales'],ascending=False)
PBL_near5_5p_G_M_p_pct[:20]


# In[ ]:




