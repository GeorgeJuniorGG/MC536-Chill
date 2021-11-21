import pandas as pd
import csv

#Trata anos diferentes
cast = pd.read_csv("data/new/atoresSemDuplicados.csv", keep_default_na=False)
series = pd.read_csv("data/new/seriesNew.csv", keep_default_na=False)

#Corrige anos errados usando como base a tabela de series
def getCorrectYear(title, year1, year2):
    for i in range(len(series)):
        if(series['Titulo'][i]==title and int(series['Ano'][i])==int(year1)):
            return year1
        elif(series['Titulo'][i]==title and int(series['Ano'][i])==int(year2)):
            return year2
    print("Não encontrou nas series")
    return min(int(year1),int(year2))
    
#Percorre tabelas(atores,geenros) verificando se há diferenças nos anos de lançamento
i=0
while i < len(cast):
    print(i+2)
    j = i+1
    newYear = cast['Ano'][i]
    while cast['Titulo'][i] == cast['Titulo'][j]:
        j+=1
    for k in range(i,j):
        if(cast['Ano'][i]!=cast['Ano'][k]):
            newYear = getCorrectYear(cast['Titulo'][i], cast['Ano'][i], cast['Ano'][k])
            break
    try:
        for k in range(i,j):
            row = [cast['Titulo'][k], newYear, cast['Genero'][k]]
            with open('data/new/atoresAnosCorretos.csv','a') as newCast: 
                writerNewCast=csv.writer(newCast)
                writerNewCast.writerow(row)
    except:
        print("Falha ao escrever no CSV")
    i=j