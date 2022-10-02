#!/usr/bin/env python
# coding: utf-8

# In[1]:


import env
import pandas as pd
from fredapi import Fred
import requests
import seaborn as sns


# In[2]:


# create fred API to acquire information from the Federal Reserve Economic Data
fred = Fred(api_key=env.fredkey)


def gdp_based():
    unem=fred.get_series('UNRATE')
    indpro=fred.get_series('INDPRO')
    rgdp=fred.get_series('GDPC1')
    gdp=fred.get_series('GDP')
    is_recession=fred.get_series('USREC')
    gdp_based_df=pd.DataFrame(data=[unem,indpro,rgdp,gdp,is_recession],index=['unem','indpro','rgdp','gdp','is_recession']).T
    gdp_based_df['quarterly'] = pd.PeriodIndex(gdp_based_df.index, freq='q')
    gdp_based_df=gdp_based_df.groupby('quarterly').agg('mean')
    gdp_based_df.is_recession[round(gdp_based_df.is_recession,2)==0.67]=1
    gdp_based_df.is_recession[round(gdp_based_df.is_recession,2)==0.33]=1
    gdp_based_df['gdp_pct_change']=gdp_based_df.rgdp.pct_change()
    gdp_based_df=gdp_based_df.dropna()
    gdp_based_df.index=gdp_based_df.index.astype('datetime64')
    return gdp_based_df
    

def split_gdp_based(gdp_based_df):
    train_size = int(len(gdp_based_df) * .5)
    validate_size = int(len(gdp_based_df) * .25)
    test_size = int(len(gdp_based_df) - train_size - validate_size)
    validate_end_index = train_size + validate_size
    gdp_train = gdp_based_df[: train_size]
    gdp_validate = gdp_based_df[train_size : validate_end_index]
    gdp_test = gdp_based_df[validate_end_index :]
    gdp_train_val=pd.concat([gdp_train,gdp_validate],axis=0)
    return gdp_train,gdp_validate,gdp_test,gdp_train_val


# In[ ]:

def gen_based():
    cpi=fred.get_series('CPIAUCSL')
    moneysup=fred.get_series('M2REAL')
    corecpi=fred.get_series('CPILFESL')
    gdp_def=fred.get_series('A191RI1Q225SBEA')
    unem=fred.get_series('UNRATE')
    indpro=fred.get_series('INDPRO')
    rgdp=fred.get_series('GDPC1')
    gdp=fred.get_series('GDP')
    rate=fred.get_series('FEDFUNDS')
    is_recession=fred.get_series('USREC')
    gdp_based_df=pd.DataFrame(data=[cpi,moneysup,corecpi,gdp_def,unem,indpro,rgdp,gdp,rate,is_recession],index=['cpi','moneysup','corecpi','gdp_def','unem','indpro','rgdp','gdp','rate','is_recession']).T
    gdp_based_df['quarterly'] = pd.PeriodIndex(gdp_based_df.index, freq='q')
    gdp_based_df=gdp_based_df.groupby('quarterly').agg('mean')
    gdp_based_df.is_recession[round(gdp_based_df.is_recession,2)==0.67]=1
    gdp_based_df.is_recession[round(gdp_based_df.is_recession,2)==0.33]=1
    gdp_based_df['gdp_pct_change']=gdp_based_df.rgdp.pct_change()
    gdp_based_df['monp_pct_change']=gdp_based_df.moneysup.pct_change()
    gdp_based_df=gdp_based_df.dropna()
    gdp_based_df.index=gdp_based_df.index.astype('datetime64')
    return gdp_based_df
    
def split_gen_based(gen_based_df):
    train_size = int(len(gen_based_df) * .5)
    validate_size = int(len(gen_based_df) * .25)
    test_size = int(len(gen_based_df) - train_size - validate_size)
    validate_end_index = train_size + validate_size
    gen_train = gen_based_df[: train_size]
    gen_validate = gen_based_df[train_size : validate_end_index]
    gen_test = gen_based_df[validate_end_index :]
    gen_train_val=pd.concat([gen_train,gen_validate],axis=0)
    return gen_train,gen_validate,gen_test,gen_train_val


def nber_based():
    rgdp=fred.get_series('GDPC1')
    rgdi=fred.get_series('A261RX1Q020SBEA')
    rmanufacture=fred.get_series('CMRMTSPL')
    indpro=fred.get_series('INDPRO')
    personincome=fred.get_series('W875RX1')
    weeklyprivate=fred.get_series('AWHI')
    payroll=fred.get_series('PAYEMS')
    empp=fred.get_series('EMRATIO')
    is_recession=fred.get_series('USREC')
    gdp_based_df=pd.DataFrame(data=[rgdp,rgdi,rmanufacture,indpro,personincome,weeklyprivate,payroll,empp,is_recession],index=['rgdp','rgdi','rmanufacture','indpro','personincome','weeklyprivate','payroll','empp','is_recession']).T
    gdp_based_df['quarterly'] = pd.PeriodIndex(gdp_based_df.index, freq='q')
    gdp_based_df=gdp_based_df.groupby('quarterly').agg('mean')
    gdp_based_df.is_recession[round(gdp_based_df.is_recession,2)==0.67]=1
    gdp_based_df.is_recession[round(gdp_based_df.is_recession,2)==0.33]=1
    gdp_based_df['gdp_pct_change']=gdp_based_df.rgdp.pct_change()
    gdp_based_df['gdi_pct_change']=gdp_based_df.rgdi.pct_change()
    gdp_based_df['manu_pct_change']=gdp_based_df.rmanufacture.pct_change()
    gdp_based_df['indpro_pct_change']=gdp_based_df.indpro.pct_change()
    gdp_based_df['payroll_pct_change']=gdp_based_df.payroll.pct_change()
    gdp_based_df['empp_pct_change']=gdp_based_df.empp.pct_change()
    gdp_based_df=gdp_based_df.dropna()
    gdp_based_df.index=gdp_based_df.index.astype('datetime64')
    return gdp_based_df
