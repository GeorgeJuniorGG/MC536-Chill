import pandas as pd

df_state=pd.read_csv("data/new/generosNew.csv")

#Identifica as tuplas repetidas
Dup_Rows = df_state[df_state.duplicated()]
print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))

#Exclui as tuplas repetidas
DF_RM_DUP = df_state.drop_duplicates(keep='first')

DF_RM_DUP.to_csv("data/new/generosTratados.csv", index=False)


########################### Elimina generos repetidos ###########################
# genres = pd.read_csv("data/generos.csv", keep_default_na=False)
# newGenres = pd.read_csv("data/new/generosNew.csv", keep_default_na=False)

# def inNewGenres(title, genre):
#     for i in range(len(newGenres)):
#         if(newGenres["Titulo"][i]==title and newGenres["Genero"][i] in genre):
#             return True

# deleteIndex = []

# for i in range(2):
#     if(inNewGenres(genres['Titulo'][i],genres['Genero'][i])):
#         deleteIndex.append(i)

# print(deleteIndex)

########################### Elimina atores repetidos ###########################
# cast = pd.read_csv("data/atores.csv", keep_default_na=False)
# newCast = pd.read_csv("data/new/atoresNew.csv", keep_default_na=False)

# def inNewCast(title, cast):
#     for i in range(len(newCast)):
#         if(newCast["Titulo"][i]==title and newCast["Ator"][i] == cast):
#             return True

# deleteIndex = []

# for i in range(len(cast)):
#     if(inNewCast(cast['Titulo'][i],cast['Ator'][i])):
#         print(i)
#         deleteIndex.append(i)

# atores = pd.read_csv("data/atores.csv", keep_default_na=False)

# data = atores.drop(labels=deleteIndex, axis=0)

# data.to_csv("data/new/AtoresTratados.csv", index=False)

#################### Elimina series duplicas após tratar anos que estavam em intervalo #################
# series = pd.read_csv("data/new/seriesTratadas.csv")
# duplicateSeries = pd.read_csv("data/new/seriesNew.csv")

# deleteindex = []

# #Recupe as posições que possui series duplicadas
# for i in range(7040, len(series)):
#     for j in range(len(duplicateSeries)):
#         if(series['Titulo'][i]==duplicateSeries['Titulo'][j] and int(series['Ano'][i])==int(duplicateSeries['Ano'][j])):
#             deleteindex.append(i)

# #Exclui tuplas que possuem series duplicadas
# data = series.drop(labels=deleteindex, axis=0)

# data.to_csv("data/new/final/sertiestratadas.csv", index=False)