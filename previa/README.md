# Projeto `MC536-Chill`

# Equipe `MC536 & Chill` - `Chill`
* `André Vila Nova Wagner da Costa` - `213081`
* `Cristiano Sampaio Pinheiro` - `256352`
* `George Gigilas Junior` - `216741`

## Resumo do Projeto
> O acesso a filmes e séries foi muito facilitado com a popularização dos serviços de streaming. No entanto, o aumento no número dessas plataformas pode trazer dúvidas sobre quantas e quais assinar. Por isso, o grupo se propôs a avaliar o conteúdo disponível em quatro das principais plataformas de streaming: Netflix, Amazon Prime Video, Hulu e Disney Plus.

> Com isso, pode-se responder a perguntas como quais filmes possuem as melhores (ou piores) avaliações, quanto tempo uma obra demora para ser lançada em uma dessas plataformas, entre outras. No entanto, devido a uma maior disponibilidade de dados sobre o conteúdo da Netflix e da Disney+, o projeto apresentará uma maior quantidade de informações sobre estas plataformas.

## Slides da Apresentação
> [Slides](slides/previa.pdf)

## Modelo Conceitual Preliminar

> ![Modelo Conceitual](assets/modeloconceitual.png)

## Modelos Lógicos Preliminares

> Modelo lógico relacional
~~~
Filmes(_titulo_, _data de lançamento_, enredo, duração, plataforma,  classificação indicativa, avaliação IMDb, Rotten Tomatoes)
Séries(_título_, _data de lançamento_, enredo, temporadas, duração, plataforma, classificação indicativa, avaliação IMDb, Rotten Tomatoes)

Atores(_título_, _data de lançamento_,  _ator_)
Diretores(_título_, _data de lançamento_, _diretor_)

Gênero(_título_, _data de lançamento_, _gênero_)
País(_título_, _data de lançamento_, _país_)

Netflix(_título_, _data de lançamento_,  data de lançamento na plataforma)
Disney Plus(_título_, _data de lançamento_, data de lançamento na plataforma)
~~~

> Modelo de grafos de propriedades
![Modelo de Grafos](assets/modelografo.png)

## Dataset Preliminar a ser Publicado

título do arquivo/base | link | breve descrição
----- | ----- | -----
`Filmes` | [Link](data/interim/filmes.csv) | `Arquivo contendo dados sobre filmes`
`Séries` | [Link](data/interim/series.csv) | `Arquivo contendo dados sobre séries`
`Netflix` | [Link](data/interim/netflix.csv) | `Arquivo contendo data de lançamento para filmes e séries da Netflix`
`DisneyPlus` | [Link](data/interim/disneyplus.csv) | `Arquivo contendo data de lançamento para filmes e séries da Disney+`
`Atores` | [Link](data/interim/atores.csv) | `Arquivo contendo atores e filmes/séries em que trabalharam`
`Diretores` | [Link](data/interim/diretores.csv) | `Arquivo contendo diretores e filmes/séries em que trabalharam`
`Gêneros` | [Link](data/interim/generos.csv) | `Arquivo contendo filmes/séries e seus respectivos gêneros`
`Países` | [Link](data/interim/paises.csv) | `Arquivo contendo filmes/séries e seus respectivos países de produção`

## Bases de Dados

título da base | link | breve descrição
----- | ----- | -----
`TV shows on Netflix, Prime Video, Hulu and Disney+` | [Link](https://www.kaggle.com/ruchi798/tv-shows-on-netflix-prime-video-hulu-and-disney) | `Base de dados para séries`
`Movies on Netflix, Prime Video, Hulu and Disney+` | [Link](https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney) | `Base de dados para filmes`
`Disney Plus Movies and TV Shows` | [Link](https://www.kaggle.com/unanimad/disney-plus-shows) | `Base de dados para filmes e séries da Disney+`
`Netflix Movies and TV Shows` | [Link](https://www.kaggle.com/shivamb/netflix-shows) | `Base de dados para filmes e séries da Netflix`
`IMDb` | [Link](https://www.imdb.com/) | `Base de dados para filmes e séries em geral`

## Operações realizadas para a construção do dataset

> [Link para o arquivo do notebook](notebooks/DatasetBuilder.ipynb) que executa as operações de construção do dataset:
* Extração de dados dos datasets encontrados.
* Transformação dos atributos de gênero, país, atores e diretores para comporem outras tabelas.
* Tratamento de dados para remoção de filmes/séries repetidos entre os datasets encontrados.
* Integração de dados dos datasets encontrados.


## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

### Pergunta/Análise 1
> * Quais gêneros são os mais frequentes em cada plataforma?
>   
```
--Cria tabelas com todas as obras de cada plataforma
DROP Table IF EXISTS allNetflix;
DROP Table IF EXISTS allDisneyPlus;

CREATE VIEW allNetflix AS
SELECT F.Titulo, F.Ano, F.Plataforma
    FROM Filmes F
    WHERE Plataforma = 'Netflix'
UNION
SELECT S.Titulo, S.Ano, S.Plataforma
    FROM Series S
    WHERE Plataforma = 'Netflix';
    
CREATE VIEW allDisneyPlus AS
SELECT F.Titulo, F.Ano, F.Plataforma
    FROM Filmes F
    WHERE Plataforma = 'Disney +'
UNION
SELECT S.Titulo, S.Ano, S.Plataforma
    FROM Series S
    WHERE Plataforma = 'Disney +'
```
```
SELECT Genero, COUNT(Genero) AS Qtd
    FROM Generos G, allNetflix AN
    WHERE G.Titulo=AN.Titulo AND G.Ano=AN.Ano
    GROUP BY Genero
    HAVING COUNT(Genero)
    ORDER BY COUNT(Genero) DESC
```
```
SELECT Genero, COUNT(Genero) AS Qtd
    FROM Generos G, allDisneyPlus AD
    WHERE G.Titulo=AD.Titulo AND G.Ano=AD.Ano
    GROUP BY Genero
    HAVING COUNT(Genero)
    ORDER BY COUNT(Genero) DESC
```

### Pergunta/Análise 2
> * Quais atores/diretores têm as melhores avaliações nos filmes em que participaram?
```
DROP VIEW IF EXISTS AtoresAvaliacoes;
CREATE VIEW AtoresAvaliacoes AS
SELECT A.Ator, (CAST(SUBSTRING(F.IMDb, 1, LENGTH(F.IMDb) - 3) as DECIMAL(9,2)) * 10 + SUBSTRING(F.RottenTomatoes, 1, LENGTH(F.RottenTomatoes) - 4))/2 Avaliacao
        FROM Atores A, Filmes F
        WHERE A.Titulo = F.Titulo AND A.Ano = F.Ano AND F.IMDb != 'nan' AND F.IMDb != '' AND F.RottenTomatoes != 'nan' AND F.RottenTomatoes != ''
        ORDER BY A.Ator;

DROP VIEW IF EXISTS DiretoresAvaliacoes;
CREATE VIEW DiretoresAvaliacoes AS
SELECT D.Diretor, (CAST(SUBSTRING(F.IMDb, 1, LENGTH(F.IMDb) - 3) as DECIMAL(9,2)) * 10 + SUBSTRING(F.RottenTomatoes, 1, LENGTH(F.RottenTomatoes) - 4))/2 Avaliacao
        FROM Diretores D, Filmes F
        WHERE D.Titulo = F.Titulo AND D.Ano = F.Ano AND F.IMDb != 'nan' AND F.IMDb != '' AND F.RottenTomatoes != 'nan' AND F.RottenTomatoes != ''
        ORDER BY D.Diretor;
```
```
SELECT AA.Ator, SUM(AA.Avaliacao)/COUNT(AA.Avaliacao) Media_Avaliacao
    FROM AtoresAvaliacoes AA
    GROUP BY AA.Ator
    ORDER BY Media_Avaliacao DESC
```
```
SELECT DA.Diretor, SUM(DA.Avaliacao)/COUNT(DA.Avaliacao) Media_Avaliacao
    FROM DiretoresAvaliacoes DA
    GROUP BY DA.Diretor
    ORDER BY Media_Avaliacao DESC
```

### Pergunta/Análise 3
> * As plataformas Disney+ e Netflix concentram a disponibilização de conteúdo em alguma época do ano?

>   Número de lançamentos em cada mês na plataforma Disney+
```
DROP VIEW IF EXISTS mesDisneyPlus;

CREATE VIEW mesDisneyPlus AS
SELECT SUBSTRING(LancamentoNaPlataforma, 1, CHARINDEX(' ', LancamentoNaPlataforma)) AS Mes
FROM DisneyPlus
```
```
SELECT D.Mes, COUNT(D.Mes) As Lancamentos
    FROM mesDisneyPlus D
    GROUP BY D.Mes
    ORDER BY Lancamentos DESC
```
> Número de lançamentos em cada mês na plataforma Netflix
```
DROP VIEW IF EXISTS mesNetflix;

CREATE VIEW mesNetflix AS
SELECT SUBSTRING(LancamentoNaPlataforma, 1, CHARINDEX(' ', LancamentoNaPlataforma)) As Mes
FROM Netflix
WHERE LancamentoNaPlataforma NOT LIKE ''
```
```
SELECT N.Mes, COUNT(N.Mes) As Lancamentos
    FROM mesNetflix N
    GROUP BY N.Mes
    ORDER BY Lancamentos DESC
```
```
DROP VIEW mesDisneyPlus;
DROP VIEW mesNetflix;
```

### Pergunta/Análise 4
> * Qual a distribuição estatística das avaliações das mídias?

>  Distribuição das avaliações de filmes
```
DROP VIEW IF EXISTS avFilmesString;

CREATE VIEW avFilmesString AS
SELECT SUBSTRING(F.IMDb, 1, 3) AS AvaliacaoString
FROM Filmes F
WHERE F.IMDb NOT LIKE 'nan/10'
```
```
DROP VIEW IF EXISTS avFilmes;

CREATE VIEW avFilmes AS
SELECT CAST(AvaliacaoString AS FLOAT) AS Avaliacao
FROM avFilmesString
```
```
SELECT
    CASE 
        WHEN Avaliacao between 0 and 0.4 then '0.0 - 0.4'
        WHEN Avaliacao between 0.5 and 0.9 then '0.5 - 0.9'
        WHEN Avaliacao between 1 and 1.4 then '1.0 - 1.4'
        WHEN Avaliacao between 1.5 and 1.9 then '1.5 - 1.9'
        WHEN Avaliacao between 2 and 2.4 then '2.0 - 2.4'
        WHEN Avaliacao between 2.5 and 2.9 then '2.5 - 2.9'
        WHEN Avaliacao between 3 and 3.4 then '3.0 - 3.4'
        WHEN Avaliacao between 3.5 and 3.9 then '3.5 - 3.9'
        WHEN Avaliacao between 4 and 4.4 then '4.0 - 4.4'
        WHEN Avaliacao between 4.5 and 4.9 then '4.5 - 4.9'
        WHEN Avaliacao between 5 and 5.4 then '5.0 - 5.4'
        WHEN Avaliacao between 5.5 and 5.9 then '5.0 - 5.9'
        WHEN Avaliacao between 6 and 6.4 then '6.0 - 6.4'
        WHEN Avaliacao between 6.5 and 6.9 then '6.5 - 6.9'
        WHEN Avaliacao between 7 and 7.4 then '7.0 - 7.4'
        WHEN Avaliacao between 7.5 and 7.9 then '7.5 - 7.9'
        WHEN Avaliacao between 8 and 8.4 then '8.0 - 8.4'
        WHEN Avaliacao between 8.5 and 8.9 then '8.5 - 8.9'
        WHEN Avaliacao between 9 and 9.4 then '9.0 - 9.4'
        ELSE '9.5 - 10'
    END AS IntervaloAvaliacao,
    COUNT(*) AS Qtd
FROM avFilmes
GROUP BY Avaliacao
ORDER BY Avaliacao
```
> Distribuição das avaliações de séries
```
DROP VIEW IF EXISTS avSeriesStr;

CREATE VIEW avSeriesStr AS
SELECT SUBSTRING(S.IMDb, 1, 3) AS AvaliacaoString
FROM Series S
WHERE S.IMDb NOT LIKE 'nan/10'
```
```
DROP VIEW IF EXISTS avSeries;

CREATE VIEW avSeries AS
SELECT CAST(AvaliacaoString AS FLOAT) AS Avaliacao
FROM avSeriesStr
```
```
SELECT
    CASE 
        WHEN Avaliacao between 0 and 0.4 then '0.0 - 0.4'
        WHEN Avaliacao between 0.5 and 0.9 then '0.5 - 0.9'
        WHEN Avaliacao between 1 and 1.4 then '1.0 - 1.4'
        WHEN Avaliacao between 1.5 and 1.9 then '1.5 - 1.9'
        WHEN Avaliacao between 2 and 2.4 then '2.0 - 2.4'
        WHEN Avaliacao between 2.5 and 2.9 then '2.5 - 2.9'
        WHEN Avaliacao between 3 and 3.4 then '3.0 - 3.4'
        WHEN Avaliacao between 3.5 and 3.9 then '3.5 - 3.9'
        WHEN Avaliacao between 4 and 4.4 then '4.0 - 4.4'
        WHEN Avaliacao between 4.5 and 4.9 then '4.5 - 4.9'
        WHEN Avaliacao between 5 and 5.4 then '5.0 - 5.4'
        WHEN Avaliacao between 5.5 and 5.9 then '5.0 - 5.9'
        WHEN Avaliacao between 6 and 6.4 then '6.0 - 6.4'
        WHEN Avaliacao between 6.5 and 6.9 then '6.5 - 6.9'
        WHEN Avaliacao between 7 and 7.4 then '7.0 - 7.4'
        WHEN Avaliacao between 7.5 and 7.9 then '7.5 - 7.9'
        WHEN Avaliacao between 8 and 8.4 then '8.0 - 8.4'
        WHEN Avaliacao between 8.5 and 8.9 then '8.5 - 8.9'
        WHEN Avaliacao between 9 and 9.4 then '9.0 - 9.4'
        ELSE '9.5 - 10'
    END AS IntervaloAvaliacao,
    COUNT(*) AS Qtd
FROM avSeries
GROUP BY Avaliacao
ORDER BY Avaliacao
```
```
DROP VIEW IF EXISTS avFilmes;
DROP VIEW IF EXISTS avFilmesString;
DROP VIEW IF EXISTS avSeries;
DROP VIEW IF EXISTS avSeriesStr;
```

### Pergunta/Análise 5
> * Levando em conta a taxa de classificação indicativa por ano, como o mercado lida com o envelhecimento do público?

>   Classificação Indicativa dos filmes para cada ano
```
DROP VIEW IF EXISTS ciFilmes;

CREATE VIEW ciFilmes AS
SELECT ClassificacaoIndicativa, Ano
FROM Filmes
WHERE ClassificacaoIndicativa NOT LIKE '' AND ClassificacaoIndicativa NOT LIKE '%min%'
```
```
SELECT Ano, ClassificacaoIndicativa, COUNT(ClassificacaoIndicativa) AS Qtd
FROM ciFilmes
GROUP BY Ano, ClassificacaoIndicativa
ORDER BY Ano
```
> Classificação Indicativa dos séries para cada ano
```
DROP VIEW IF EXISTS ciSeries;

CREATE VIEW ciSeries AS
SELECT ClassificacaoIndicativa, SUBSTRING(Ano, 1, 4) AS Ano
FROM Series
WHERE ClassificacaoIndicativa NOT LIKE ''
```
```
SELECT Ano, ClassificacaoIndicativa, COUNT(ClassificacaoIndicativa) AS Qtd
FROM ciSeries
GROUP BY Ano, ClassificacaoIndicativa
ORDER BY Ano
```
```
DROP VIEW IF EXISTS ciFilmes;
DROP VIEW IF EXISTS ciSeries;
```

### Pergunta/Análise 6
> * Comparando as avaliações do Rotten Tomatoes e do IMDb, quais são as obras mais controversas?
  
>   Filmes
```
SELECT F.Titulo, ABS(CAST(SUBSTRING(F.IMDb, 1, LENGTH(F.IMDb) - 3) as DECIMAL(9,2)) * 10 - SUBSTRING(F.RottenTomatoes, 1, LENGTH(F.RottenTomatoes) - 4)) DiferencaAvaliacao
    FROM Filmes F
    WHERE F.IMDb != 'nan' AND F.IMDb != '' AND F.RottenTomatoes != 'nan' AND F.RottenTomatoes != ''
    ORDER BY DiferencaAvaliacao DESC;
```
> Series
```
SELECT S.Titulo, ABS(CAST(SUBSTRING(S.IMDb, 1, LENGTH(S.IMDb) - 3) as DECIMAL(9,2)) * 10 - SUBSTRING(S.RottenTomatoes, 1, LENGTH(S.RottenTomatoes) - 4)) DiferencaAvaliacao
    FROM Series S
    WHERE S.IMDb != 'nan' AND S.IMDb != '' AND S.RottenTomatoes != 'nan' AND S.RottenTomatoes != ''
    ORDER BY DiferencaAvaliacao DESC;
```

### Pergunta/Análise 7
> * Existe alguma relação entre popularidade e exclusividade dos serviços de streaming?
```
--Cria tabelas com todas as obras de cada plataforma contendo a media da avaliação
DROP Table IF EXISTS allNetflix;
DROP Table IF EXISTS allDisneyPlus;
DROP Table IF EXISTS allOthers;


CREATE VIEW allNetflix AS
SELECT F.Titulo, F.Ano, F.Plataforma, (CAST(SUBSTRING(F.IMDB,1,LENGTH(F.IMDB)-3) AS DECIMAL(9,2))*10 + SUBSTRING(F.RottenTomatoes, 1, LENGTH(F.RottenTomatoes)-4))/2 Avaliacao
    FROM Filmes F
    WHERE F.Plataforma = 'Netflix' AND F.IMDB != 'nan' AND F.IMDB != '' AND F.IMDB != 'nan/10' AND F.RottenTomatoes != 'nan' AND F.RottenTomatoes != ''
UNION
SELECT S.Titulo, S.Ano, S.Plataforma, (CAST(SUBSTRING(S.IMDB,1,LENGTH(S.IMDB)-3) AS DECIMAL(9,2))*10 + SUBSTRING(S.RottenTomatoes, 1, LENGTH(S.RottenTomatoes)-4))/2 Avaliacao
    FROM Series S
    WHERE S.Plataforma = 'Netflix' AND S.IMDB != 'nan' AND S.IMDB != '' AND S.IMDB != 'nan/10' AND S.RottenTomatoes != 'nan' AND S.RottenTomatoes != '';

CREATE VIEW allDisneyPlus AS
SELECT F.Titulo, F.Ano, F.Plataforma, (CAST(SUBSTRING(F.IMDB,1,LENGTH(F.IMDB)-3) AS DECIMAL(9,2))*10 + SUBSTRING(F.RottenTomatoes, 1, LENGTH(F.RottenTomatoes)-4))/2 Avaliacao
    FROM Filmes F
    WHERE F.Plataforma = 'Disney +' AND F.IMDB != 'nan' AND F.IMDB != '' AND F.IMDB != 'nan/10' AND F.RottenTomatoes != 'nan' AND F.RottenTomatoes != ''
UNION
SELECT S.Titulo, S.Ano, S.Plataforma, (CAST(SUBSTRING(S.IMDB,1,LENGTH(S.IMDB)-3) AS DECIMAL(9,2))*10 + SUBSTRING(S.RottenTomatoes, 1, LENGTH(S.RottenTomatoes)-4))/2 Avaliacao
    FROM Series S
    WHERE S.Plataforma = 'Disney +' AND S.IMDB != 'nan' AND S.IMDB != '' AND S.IMDB != 'nan/10' AND S.RottenTomatoes != 'nan' AND S.RottenTomatoes != '';
    
CREATE VIEW allOthers AS
SELECT F.Titulo, F.Ano, F.Plataforma, (CAST(SUBSTRING(F.IMDB,1,LENGTH(F.IMDB)-3) AS DECIMAL(9,2))*10 + SUBSTRING(F.RottenTomatoes, 1, LENGTH(F.RottenTomatoes)-4))/2 Avaliacao
    FROM Filmes F
    WHERE F.Plataforma = 'Netflix,Disney+' OR F.Plataforma='Outra' AND F.IMDB != 'nan' AND F.IMDB != '' AND F.IMDB != 'nan/10' AND F.RottenTomatoes != 'nan' AND F.RottenTomatoes != ''
UNION
SELECT S.Titulo, S.Ano, S.Plataforma, (CAST(SUBSTRING(S.IMDB,1,LENGTH(S.IMDB)-3) AS DECIMAL(9,2))*10 + SUBSTRING(S.RottenTomatoes, 1, LENGTH(S.RottenTomatoes)-4))/2 Avaliacao
    FROM Series S
    WHERE S.Plataforma = 'Netflix,Disney+' OR S.Plataforma='Outra' AND S.IMDB != 'nan' AND S.IMDB != '' AND S.IMDB != 'nan/10' AND S.RottenTomatoes != 'nan' AND S.RottenTomatoes != '';
```
```
SELECT AVG(Avaliacao) FROM allNetflix;
SELECT AVG(Avaliacao) FROM allDisneyPlus;
SELECT AVG(Avaliacao) FROM allOthers;
```

### Pergunta/Análise 8
> * Qual a palavra mais utilizada em títulos?
>   
>   * Seria necessário realizar uma análise estatística em cima de cada palavra de cada título, possivelmente eliminando artigos e números, para possibilitar uma análise mais interessante.
.

### Pergunta/Análise 9
> * Dado que uma pessoa X trabalhou com uma pessoa Y e com uma pessoa Z, qual a chance de Y trabalhar com Z em um projeto futuro?
>   
>   * Para responder esta pergunta, podemos fazer uma análise da modalidade predição de links que, com base nas conexões do grafo da Figura 3 (que relaciona pessoas pela obra trabalhada), atribui um valor de 0 a 1 que indica a probabilidade de essas pessoas trabalharem juntas no futuro.

### Pergunta/Análise 10
> * Como podemos mapear a flexibilidade de atores e diretores quanto ao gênero da obra trabalhada?
>   
>   * Para responder esta pergunta, podemos fazer uma análise de formação de comunidade a partir do grafo da Figura 4 (que relaciona pessoas pelo gênero da obra trabalhada). Com ele, podemos avaliar quais atores/diretores tendem a participar mais de obras de um determinado gênero a partir das comunidades formadas.

### Pergunta/Análise 11
> * Quais atores/diretores são mais populares no meio cinematográfico?
>   
>   * Para responder esta pergunta, podemos fazer uma análise de centralidade a partir do grafo da Figura 3 (que relaciona pessoas com a obra trabalhada). Com ele, podemos criar um sistema que atribui um valor para cada pessoa com base no número de ligações com outras pessoas que essa pessoa possui. Além disso, podemos aplicar um peso ponderado para ligações com pessoas mais populares. A partir disso, poderemos atribuir um valor de popularidade para cada pessoa e ver quem são os atores/diretores mais centrais.

### Pergunta/Análise 12
> * Existe alguma relação entre duração e avaliação?
>   
>   * Podemos fazer uma análise estatística em cima da avaliação dos filmes de determinados intervalos de duração e estudar se existe alguma correlação entre duração e avaliação.

### Pergunta/Análise 13
> * Existe alguma relação entre gênero e avaliação?
>   
>   * Podemos fazer uma análise estatística em cima da avaliação dos filmes de cada gênero e estudar se existe alguma correlação entre gênero e avaliação.

### Pergunta/Análise 14
> * Como os gêneros mais populares mudaram ao longo dos anos?
>   
>   * Poderíamos fazer uma análise de quais gêneros mais populares em cada intervalo de anos (de 5 em 5 anos, por exemplo) e analisar as tendências.

### Pergunta/Análise 15
> * Existe alguma relação entre país e gênero?
>   
>   * Podemos analisar quais são os principais gêneros de cada país e quais são os principais países de cada gênero e estudar as relações dos resultados encontrados.

### Pergunta/Análise 16
> * Quais propriedades são comuns a filmes de sucesso/boa avaliação?
>   
>   * Poderíamos reunir os filmes mais populares e fazer uma análise estatística de cada campo disponível no dataset, possivelmente até fazer um gráfico de quais características comuns mais aparecem.

### Pergunta/Análise 17
> * Quais são os elementos em comum das mídias que não estão disponíveis em nenhuma das plataformas analisadas?
>   
>   * Poderíamos reunir os filmes cuja plataforma está listada como “Outra”, em nosso dataset, e fazer uma análise estatística de cada campo disponível.

### Pergunta/Análise 18
> * Como a popularização das séries impactou o mercado de filmes?
>   
>   * Poderíamos buscar a primeira data de lançamento de uma série na Netflix e supor que este é o ponto em que as séries começaram a se popularizar. Tendo essa data, podemos analisar os filmes que lançaram após essa data quanto à avaliação, número de filmes lançados e outros aspectos que possam ser interessantes.


### Pergunta/Análise 19
> * Dado que um usuário gostou de um filme, qual seria uma boa recomendação de outro filme para ele assistir?
>   
>   * Podemos analisar aspectos em comuns dos filmes (como gênero, atores/diretores envolvidos, avaliação, entre outros) para propor outros filmes, possivelmente até com técnicas de machine learning.

[Notebook com queries](notebooks/Queries.ipynb)
