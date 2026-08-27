import matplotlib.pyplot as plt
import pandas as pd
def faturar(df):
    faturamento = df['preco'] * df['quantidade_vendida']
    faturamento = faturamento.sort_values(ascending=False).head()
    tab = pd.DataFrame(data={'Produto': df['produto'].loc[faturamento.index], 'Faturamento': faturamento})
    return tab

def graficar(df, novodf):
    totfat = (df['preco'] * df['quantidade_vendida']).sum()
    porcentagens = [*[valor / totfat * 100 for valor in novodf['Faturamento']], totfat]
    nomes = [*[nomes for nomes in novodf['nomes']], 'outros']
    plt.pie(porcentagens, labels=nomes, autopct='%1.1f%%')
    plt.show()



