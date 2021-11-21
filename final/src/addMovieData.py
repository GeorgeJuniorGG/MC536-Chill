import pandas as pd
from imdb import IMDb
ia = IMDb()

#Recupero ID da midia com base no título e ano
def getMediaId(mediaTitle, mediaYear):
    try:  
        findMedia = ia.search_movie(mediaTitle)
        for media in findMedia:
            if(str(media) in mediaTitle and abs(int(media.data['year'])-int(mediaYear))<=1):
                return media.movieID
    except:
        return False
    return False

#Trata o formato de retorno da classificação indicativa
def getCertificate(certificates):
    for certificate in certificates:
        if('United States:' in certificate):
            return certificate.split(':')[1]

#Recupera os dados da mídia
def getDataMovie(movieId):
    try:
        movie = ia.get_movie(movieId)
        dataMovie = {}
        try: dataMovie['runtimes']= str(movie.data['runtimes'])[2:-2]+'.0'
        except:
            print("Não encontrou a duração")
        try: dataMovie['certificate']= getCertificate(movie.data['certificates'])
        except:
            print("Não encontrou a classificação indicativa")
        try: dataMovie['ratingIMDB']= str(movie.data['rating'])+'/10'
        except: 
            print("Não encontrou o IMDb")
        try: dataMovie['plot']= str(movie.data['plot outline'])
        except:
            print("Não encontrou o enredo")
        return dataMovie
    except:
        print("Erro na requisição")



movies = pd.read_csv("data/filmes.csv", keep_default_na=False)

#Percorre todos os filmes completando os dados
for i in range(len(movies)):
    if(not movies['Duracao'][i] or not movies['Classificacao Indicativa'][i] or not movies['IMDb'][i] or not movies['Enredo'][i]):
        print('Atual: ',i+2)
        mediaId = getMediaId(movies['Titulo'][i],movies['Ano'][i])
        if(mediaId):
            dataSerie = getDataMovie(mediaId)
            if(not movies['Duracao'][i]):
                try: movies.loc[i, 'Duracao'] = dataSerie['runtimes']
                except:
                    pass
            if(not movies['Classificacao Indicativa'][i]):
                try:movies.loc[i, 'Classificacao Indicativa'] = dataSerie['certificate']
                except:
                    pass
            if(not movies['IMDb'][i]):
                try:movies.loc[i, 'IMDb'] = dataSerie['ratingIMDB']
                except:
                    pass
            if(not movies['Enredo'][i]):
                try:movies.loc[i, 'Enredo'] = dataSerie['plot']
                except:
                    pass
        else:
            print("Falha ao recuperar o id")

movies.to_csv("data/new/filmesNew.csv", index=False)