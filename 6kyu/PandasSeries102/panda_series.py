import pandas as pd

def max_common(df_a, df_b):

    return pd.concat([df_a,df_b]).filter(items=df_a.columns).groupby(level=0).max()
    

df_a = pd.DataFrame(data=[[2.5, 2.0, 2.0], [2.0, 2.0, 2.0]], columns=list('ABC'))
df_b = pd.DataFrame(data=[[1.0, 6.0, 7.0, 1.0], [8.5, 1.0, 9.0, 1.0]], columns=list('CBDE'))
print(max_common(df_a, df_b))