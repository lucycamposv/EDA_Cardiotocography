import numpy as np

def ac_lista(df,index):
     df_ac = df[df['index_NSP']==index][['accelerations']].value_counts()
     val_index = [df_ac.iloc[0],df_ac.iloc[1:].sum()]
     return val_index

def lista_NSP(colores,index):
    lista = []
    i=0
    while i <16:
        lista.append(colores[index])
        i+=1
    return lista

def porcentaje(df,var):
    lista = []
    for n in np.arange(5):
        i = 0
        while i<3:
            if len(df[df[var]==(n+1)].groupby('index_NSP')[['index_NSP']].count())==1:
                lista.append(100)
                lista.append(0)
                lista.append(0)
                break
            if len(df[df[var]==(n+1)].groupby('index_NSP')[['index_NSP']].count())==2:
                lista.append(5.71)
                lista.append(0)
                lista.append(94.29)
                break
            else:
                total = df[df[var]==(n+1)].groupby('index_NSP').count().sum()['abnormal_STV']
                num = df[df[var]==(n+1)].groupby('index_NSP').count().iloc[i]['abnormal_STV']
                lista.append((num*100/total).round(2))
            i+=1   
    return lista

def class_STV(df):
    if df['abnormal_STV']<18:
        val = 1
    elif df['abnormal_STV']<36:
        val = 2
    elif df['abnormal_STV']<54:
        val = 3
    elif df['abnormal_STV']<72:
        val = 4
    else:
        val = 5
    return val

def class_LTV(df):
    if df['abnormal_LTV']<18:
        val = 1
    elif df['abnormal_LTV']<36:
        val = 2
    elif df['abnormal_LTV']<54:
        val = 3
    elif df['abnormal_LTV']<72:
        val = 4
    else:
        val = 5
    return val


