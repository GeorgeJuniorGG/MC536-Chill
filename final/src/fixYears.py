import pandas as pd
import csv

cast = pd.read_csv("data/diretores.csv", keep_default_na=False)
# series = pd.read_csv("data/new/seriesNew.csv", keep_default_na=False)

#Percorre a tabela eliminando anos que foram dados em intervalos, assumindo sempre o ano de lançamento
for k in range(17160,len(cast)):
    row = [cast['Titulo'][k], cast['Ano'][k][0:4], cast['Diretor'][k]]
    with open('data/new/teste.csv','a') as newCast: 
        writerNewCast=csv.writer(newCast)
        writerNewCast.writerow(row)