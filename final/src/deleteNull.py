import pandas as pd

#Elimina nulos das tabelas
director = pd.read_csv("data/new/diretoresNew.csv",  keep_default_na=False)

deleteIndex = []

#Recupe as posições que possui algum campo especifico nulo
for i in range(len(director)):
    if(not director['Diretor'][i] or director["Diretor"][i]==''):
        deleteIndex.append(i)

#Exclui tuplas que possuem nulos
data = director.drop(labels=deleteIndex, axis=0)

data.to_csv("data/new/diretoresNew.csv", index=False)
