import pandas as pd
from imdb import IMDb
ia = IMDb()

#Recupero ID da midia com base no título e ano
def getMediaId(mediaTitle, mediaYear):
    findMedia = ia.search_movie(mediaTitle)
    try: 
        for media in findMedia:
            if(str(media) in mediaTitle and abs(int(media.data['year'])-int(mediaYear))<=1):
                return media.movieID
    except:
        return False
    return False

#Trata o formato de retorno da classificação indicativa
def getCertificate(certificates):
    for certificate in certificates:
        if('United Kingdom:' in certificate):
            return certificate.split(':')[1]+'+'

#Recupera os dados da mídia
def getDataTvShow(tvShowId):
    tvShow = ia.get_movie(tvShowId)
    dataTvShow = {}
    try: dataTvShow['runtimes']= str(tvShow.data['runtimes'])[2:-2]+' min'
    except:
        print("Não encontrou a duração")
    try: dataTvShow['number of seasons']= str(tvShow.data['number of seasons'])+' Seasons'
    except:
        print("Não encontrou o número de temporadas")
    try: dataTvShow['certificate']= getCertificate(tvShow.data['certificates'])
    except:
        print("Não encontrou a classificação indicativa")
    try: dataTvShow['ratingIMDB']= str(tvShow.data['rating'])+'/10'
    except: 
        print("Não encontrou o IMDb")
    try: dataTvShow['plot']= str(tvShow.data['plot outline'])
    except:
        print("Não encontrou o enredo")

    return dataTvShow

series = pd.read_csv("data/series.csv", keep_default_na=False)

#Percorre todos as series completando os dados
for i in range(len(series)):
    if(not series['Duracao'][i] or not series['Temporadas'][i] or not series['Classificacao Indicativa'][i] or not series['IMDb'][i] or not series['Enredo'][i]):
        mediaId = getMediaId(series['Titulo'][i],series['Ano'][i])
        if(mediaId):
            dataSerie = getDataTvShow(mediaId)
            if(not series['Duracao'][i]):
                try: series.loc[i, 'Duracao'] = dataSerie['runtimes']
                except:
                    pass
            if(not series['Temporadas'][i]):
                try:series.loc[i, 'Temporadas'] = dataSerie['number of seasons']
                except:
                    pass
            if(not series['Classificacao Indicativa'][i]):
                try:series.loc[i, 'Classificacao Indicativa'] = dataSerie['certificate']
                except:
                    pass
            if(not series['IMDb'][i]):
                try:series.loc[i, 'IMDb'] = dataSerie['ratingIMDB']
                except:
                    pass
            if(not series['Enredo'][i]):
                try:series.loc[i, 'Enredo'] = dataSerie['plot']
                except:
                    pass
        else:
            print("Falha ao recuperar o id")

series.to_csv("data/series2.0.csv", index=False)