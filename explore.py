#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


def hypo1(df):
    gdp_re = df[df.is_recession >= 1].gdp_pct_change
    gdp_nre= df[df.is_recession == 0].gdp_pct_change
    sns.histplot(x='gdp_pct_change',hue='is_recession',data=df,kde=True)
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    print('recession GDP variance:',gdp_re.var())
    print('no recession GDP variance:', gdp_nre.var())
    t, p = stats.ttest_ind(gdp_re, gdp_nre, equal_var=False)
    if p / 2 > 0.05:
        print("The average GDP in a recession is the same or less than the average GDP in no recession")
    elif t < 0:
        print("The average GDP in a recession is the same or less than the average GDP in no recession")
    else:
        print("The average GDP in a recession is the greater than the average GDP in no recession")



