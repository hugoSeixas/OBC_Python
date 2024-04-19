# 2

import pandas as pd

# 1 - Importando Dados
data = pd.read_excel("data/VendaCarros.xlsx")
# print(type(data))

# 2 - Selecionando colunas especificas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

# 3 - Criando a tabela pivô
pivo = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivo)

# 4 - Exportando tabela pivô em arquivo excel
pivo.to_excel("data/pivo.xlsx", "Relatorio")
