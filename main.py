from pathlib import Path
import pandas as pd
import defs as d

while True:
    d.limpa_tela()
    tabela = (input('Coloque aqui o nome da sua tabela:\n'))
    ext = Path(tabela).suffix
    if ext == '.csv':
        leitor = pd.read_csv
        break
    elif ext == '.xlsx':
        leitor = pd.read_excel
        break
    else:
        print('Nenhum arquivo excel ou csv encontrado!')
d.limpa_tela()
try:
    df = leitor(tabela)
except FileNotFoundError:
    print('Houve um erro ao ler o arquivo!\nArquivo não encontrado...')
else:
    nova_tabela = d.faturar(df)
    if nova_tabela is not None:
        d.graficar(df, nova_tabela)