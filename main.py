from pathlib import Path
import pandas as pd
import defs as d

while True:
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

try:
    df = leitor(tabela)
except:
    print('Houve um erro ao ler o arquivo!')
else:
    d.faturar(df)




