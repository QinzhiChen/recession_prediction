#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
from scipy.stats import norm
from scipy.stats import shapiro

def norm(df):
    w,p= shapiro(df)
    if p <= 0.05:
        print("we assume the distribution of our variable is not normal/gaussian")
    else:
        print("we assume the distribution of our variable is normal/gaussian.")


def hypo1(df):
    gdp_re = df[df.is_recession >= 1].gdp_pct_change
    gdp_nre= df[df.is_recession == 0].gdp_pct_change
    sns.histplot(x='gdp_pct_change',hue='is_recession',data=df,kde=True)
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    t, p = stats.mannwhitneyu(gdp_re, gdp_nre)
    if p > 0.05:
        print("The average two consecutive GDP in recession is same as the average two consecutive GDP in no recession")
    else:
        print("The average two consecutive GDP in a recession is not the same as the average two consecutive GDP in no recession")

def bin_plot(gen_train_val):
    gen_train_val['rate_bin'] = pd.qcut(gen_train_val.rate, 3, labels=['low', 'moderate', 'high'])
    ax=sns.catplot(data=gen_train_val, x="rate_bin", y="gdp_def", hue="is_recession", kind="box")
    ax.set(xlabel='interest rate',ylabel='gdp_pct_change')
    ax.set_titles('interest rate and gdp deflator')
    plt.show()

def genhypo1(df):
    pro=df[df.is_recession==1]
    w,p= shapiro(pro.rate)
    if p <= 0.05:
        print("we assume the distribution of our variable is not normal/gaussian")
    else:
        print("we assume the distribution of our variable is normal/gaussian.")

def nber_hypo1(df):
    ind_re = df[df.is_recession >= 1].indpro
    ind_nre= df[df.is_recession == 0].indpro
    sns.histplot(x='indpro',hue='is_recession',data=df,kde=True)
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    print('recession industrial production variance:',ind_re.var())
    print('no recession industrial production variance:', ind_nre.var())
    t, p = stats.mannwhitneyu(ind_re, ind_nre)
    if p > 0.05:
        print("The average industrial production in no recession is the same as the average industrial production in a recession")
    else:
        print("The average industrial production in no recession is not the same as the average industrial production in a recession")
