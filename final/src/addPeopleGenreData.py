import pandas as pd
from imdb import IMDb
import csv
ia = IMDb()

#Recupera o ID da mídia com base no titulo e no ano
def getMediaId(mediaTitle, mediaYear):
    try:  
        findMedia = ia.search_movie(mediaTitle)
        for media in findMedia:
            if(str(media) in mediaTitle and abs(int(media.data['year'])-int(mediaYear[0:4]))<=1):
                return media.movieID
    except:
        return False
    return False

#Recupera os dados de atores, diretores e genero
def getDataMovie(movieId):
    try: 
        movie = ia.get_movie(movieId)
        dataMovie = {}
        cast = []
        genres = []
        directors = []
        try:
            if(len(movie.data["cast"])>=15):
                for i in range(15):
                    cast.append(movie.data["cast"][i]["name"])
            else:
                for person in movie.data["cast"]:
                    cast.append(person["name"])
            dataMovie["cast"] = cast
        except:
            print("Não encontrou atores")
        
        try:
            for director in movie.data['writer']:
                directors.append(director["name"])
            dataMovie["directors"] = directors
        except:
            print("Não encontrou diretores")

        try:    
            for genre in movie.data["genres"]:
                genres.append(genre)
            dataMovie["genres"] = genres
        except:
            print("Não encontrou gêneros")

        return dataMovie
    except:
        print("Erro na requisição")

#Recupera os dados antigos para comparação
def getOldGenres(title, year):
    oldGenres = []
    for i in range(len(genres)):
        if(genres["Titulo"][i]==title and genres["Ano"][i]==year and genres["Genero"][i]!="nan"):
            oldGenres.append(genres["Genero"][i])
    return oldGenres

def getOldCast(title, year):
    oldCast = []
    for i in range(len(cast)):
        if(cast["Titulo"][i]==title and cast["Ano"][i]==year) and cast["Ator"][i]!="nan":
            oldCast.append(cast["Ator"][i])
    return oldCast

def getOldDirectors(title, year):
    oldDirectors = []
    for i in range(len(directors)):
        if(directors["Titulo"][i]==title and directors["Ano"][i]==year and directors["Diretor"][i]!="nan"):
            oldDirectors.append(directors["Diretor"][i])
    return oldDirectors

#Adiciona os novos dados que são diferentes dos já existentes
def addNewCast(title,year,cast):
    oldCast = getOldCast(title, year)
    try:
        for person in cast:
            if (person not in oldCast):
                row = [title, year, person]
                with open('data/new/atoresNew.csv','a') as newCast: 
                    writerNewCast=csv.writer(newCast)
                    writerNewCast.writerow(row)
    except:
        print("Falha ao escrever no CSV")
        
def addNewDirectors(title,year,directors):
    oldDirectors = getOldDirectors(title, year)
    try:
        for director in directors:
            if (director not in oldDirectors):
                with open('data/new/diretoresNew.csv','a') as newCast: 
                    newCast.write(title+","+year+","+director+"\n")
    except:
        print("Falha ao escrever no CSV")

def addNewGenres(title,year,genres):
    oldGenres = getOldGenres(title, year)
    try:
        for genre in genres:
            if (genre not in oldGenres):
                with open('data/new/generosNew.csv','a') as newCast: 
                    newCast.write(title+","+year+","+genre+"\n")
    except:
        print("Falha ao escrever no CSV")

movies = pd.read_csv("data/filmes.csv", keep_default_na=False)
cast = pd.read_csv("data/atores.csv", keep_default_na=False)
directors = pd.read_csv("data/diretores.csv", keep_default_na=False)
genres = pd.read_csv("data/generos.csv", keep_default_na=False)

#Percorre a lista de filmes completando os dados de atores, diretores e genero
for i in range(len(movies)):
    mediaId = getMediaId(movies['Titulo'][i],movies['Ano'][i])
    if(mediaId):
        print(i+2)
        dataMovie = getDataMovie(mediaId)
        try:
            addNewCast(movies['Titulo'][i],str(movies['Ano'][i]),dataMovie["cast"])
        except:
            print("Não há cast")
        try:
            addNewDirectors(movies['Titulo'][i],str(movies['Ano'][i]),dataMovie["directors"])
        except:
            print("Não há directors")
        try:
            addNewGenres(movies['Titulo'][i],str(movies['Ano'][i]),dataMovie["genres"])
        except:
            print("Não há genres")
    else:
        print("Falha ao recuperar o id")