import matplotlib.pyplot as plt
import pandas as pd
import os

def faturar(df):
    try:
        faturamento = df['preco'] * df['quantidade_vendida']
        faturamento = faturamento.sort_values(ascending=False).head(10)
        tab = pd.DataFrame(data={'Produto': df['produto'].loc[faturamento.index], 'Faturamento': faturamento})
    except TypeError:
        limpa_tela()
        print('Alguma das informações fornecidas está incorreta!')
    except KeyError:
        limpa_tela()
        print('Faltando alguma das seguintes informações\npreco\nquantidade_vendida\nproduto')
    else:
        return tab

def graficar(df, novodf):

    totfat = (df['preco'] * df['quantidade_vendida']).sum()
    valores = [*[valor for valor in novodf['Faturamento']], totfat - novodf['Faturamento'].sum()]
    nomes = [*[nomes for nomes in novodf['Produto']], 'Outros']
    plt.figure(figsize = [10, 10])
    plt.pie(valores, labels=nomes, autopct='%1.1f%%', wedgeprops={'width': 0.3}, textprops={'fontsize': 7})
    plt.legend([f'Soma dos valores: {novodf["Faturamento"].sum()/totfat*100:.2f}% do total.'], loc='upper left')
    plt.show()

def limpa_tela():
    os.system('cls')