import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
#print(df.head())

# 2
BMI=10000*df['weight']/df['height']**2
#print(BMI>25)
df['overweight'] = (BMI>25).astype(int)
#print(df.head())

# 3
df['cholesterol']=df['cholesterol']-1
df['gluc']=df['gluc']-1
df.loc[df['cholesterol']>1, 'cholesterol']=1
df.loc[df['gluc']>1, 'gluc']=1
#print(df.head())
#print(df['cholesterol']-1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke','alco', 'active', 'overweight'])
    #print(df_cat)

    # 6
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='counts')
    #print(df_cat)

    # 7
    fig=sns.catplot(df_cat, x='variable', y='counts', col='cardio', hue='value', kind='bar')
    #print(a)
    


    # 8
    #fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    mask=(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025))
    mask2=(df['height'] <= df['height'].quantile(0.975))
    mask3=(df['weight'] <= df['weight'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025))
    df_heat = df[mask & mask2 & mask3]
    #print(df_heat)

    # 12
    corr = df_heat.corr()
    #corr=round(corr,1)

    # 13
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    #print(corr[mask])


    # 14
    fig, ax = plt.subplots(figsize=(10, 10))
    # 15
    sns.heatmap(corr, annot=True, mask=mask, square=True, fmt='.1f')


    # 16
    fig.savefig('heatmap.png')
    return fig
