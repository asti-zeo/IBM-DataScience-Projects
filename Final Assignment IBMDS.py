#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[2]:


#pip install -U yfinance pandas


# In[3]:


tesla = yf.Ticker('TSLA')
tesla.history(period = 'max')


# In[4]:


tesla_data = pd.DataFrame(tesla.history(period = 'max'))
tesla_data.reset_index(inplace = True)
tesla_data.head()


# # Extract quarterly Revenue Data - Tesla
# 

# In[6]:


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'


# In[105]:


#df = pd.read_html(url)[1].tail() #without match function
#df
# match function is important if i cannot locate the values using index
tesla_revenue = pd.read_html(url, match = 'Quarterly ')[0]
tesla_revenue.columns = [['Date','Revenue']]
tesla_revenue.tail()


# In[106]:


#tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")


# In[107]:


tesla_revenue['Date'].values[0]


# In[108]:


tesla_revenue['Revenue'].values[0][0]


# In[109]:


tesla_revenue.dropna(inplace=True)


# In[135]:


rev_list_tesla = []
for i in tesla_revenue['Revenue'].values:
    new_val = float(str(i[0]).replace(',','').replace('$',''))
    
    rev_list_tesla.append(new_val)
rev_list_tesla[:3]


# In[111]:


from datetime import datetime
date_list_tesla = []
for i in tesla_revenue['Date'].values:
    new_val = datetime.strptime(i[0],'%Y-%m-%d').date()
    
    date_list_tesla.append(new_val)
date_list_tesla[:5]


# In[112]:


rev_list_tesla[:3]


# In[137]:


tesla_revenue['Revenue'] = rev_list_tesla


# In[138]:


#tesla_revenue.dropna(inplace=True)

#tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

tesla_revenue.info()


# In[140]:


new_tesla_revenue = tesla_revenue
new_tesla_revenue['Date'] = date_list_tesla


# In[115]:


#pd.to_datetime(tesla_data.Date, format='%d.%m.%Y %H:%M:%S.%f')


# ## Data cleaning for graph

# In[130]:


pd.Series(new_tesla_revenue['Date'].values.reshape(53,))[:3]


# In[ ]:





# In[145]:


pd.Series(new_tesla_revenue['Revenue'].values.reshape(53,))[:3]


# In[71]:


pd.to_datetime(tesla_data.Date)


# In[72]:


tesla_data.Date


# In[78]:


import matplotlib.pyplot as plt
plt.plot(tesla_data["Date"], tesla_data['Close'])


# In[116]:


#pd.to_datetime(tesla_data.Date, infer_datetime_format= True)


# In[157]:


fig = make_subplots(rows = 2, cols = 1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"),                   vertical_spacing = .3)

fig.add_trace(go.Scatter(x = tesla_data['Date'], y = tesla_data['Close']), row =1, col =1,)
fig.add_trace(go.Scatter(x = pd.Series(new_tesla_revenue['Date'].values.reshape(53,)),                         y = pd.Series(new_tesla_revenue['Revenue'].values.reshape(53,))), row =2, col =1)

fig.update_xaxes(title_text="Date", row=1, col=1)
fig.update_xaxes(title_text="Date", row=2, col=1)
fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
fig.update_layout(showlegend  = False, height = 900, title = "Tesla", xaxis_rangeslider_visible = True)


# # GAMESTOP

# In[158]:


gme = yf.Ticker('GME')


# In[159]:


gme_data = pd.DataFrame(gme.history(period = 'max'))
gme_data.head()


# In[160]:


gme_data.reset_index(inplace= True)
gme_data.head()


# In[161]:


url_2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'


# In[162]:


gme_revenue = pd.read_html(url_2, match = 'Quarterly')[0]
gme_revenue.columns = [['Date', 'Revenue']]
gme_revenue.tail()


# In[163]:


rev_list_gme = []
for i in gme_revenue['Revenue'].values:
    new_val = float(str(i[0]).replace(',','').replace('$',''))
    
    rev_list_gme.append(new_val)
rev_list_gme[:3]

from datetime import datetime
date_list_gme = []
for i in gme_revenue['Date'].values:
    new_val = datetime.strptime(i[0],'%Y-%m-%d').date()
    
    date_list_gme.append(new_val)
date_list_gme[:5]


# In[165]:


gme_revenue['Revenue'] = rev_list_gme
gme_revenue.head()


# In[168]:


fig = make_subplots(rows = 2, cols = 1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"),                   vertical_spacing = .3)

fig.add_trace(go.Scatter(x = gme_data['Date'], y = gme_data['Close']), row =1, col =1,)
fig.add_trace(go.Scatter(x = pd.Series(gme_revenue['Date'].values.reshape(62,)),                         y = pd.Series(gme_revenue['Revenue'].values.reshape(62,))), row =2, col =1)

fig.update_xaxes(title_text="Date", row=1, col=1)
fig.update_xaxes(title_text="Date", row=2, col=1)
fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
fig.update_layout(showlegend  = False, height = 900, title = "GME", xaxis_rangeslider_visible = True)


# In[ ]:




