# 3

from openpyxl import load_workbook

# 1 - Lê pasta de trabalho e planilha
wb = load_workbook("data/pivo.xlsx")
shet = wb["Relatorio"]

# 2 - Acessando um valor expecifíco
# print(shet["A3"].value)
# print(shet["B3"].value)

# 3 - Iterando valores por meio de loop
for i in range(2, 6):
    ano = shet["A%s" %i].value
    am = shet["B%s" %i].value
    bt = shet["C%s" %i].value
    print("{} O Aston Martin vendeu: {} e o Bentley vendeu {}".format(ano, am, bt))
