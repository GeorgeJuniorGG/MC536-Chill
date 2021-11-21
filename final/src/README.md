# Instruções básicas de instalação/execução
O tratamento de dados foi realizado diretamente em python por uma questão de confiabilidade, optamos por executa-los diretamente em nossas maquinas sem o uso de notebooks.

Os códigos então em python 3 e podem ser executados normalmente após adicionar duas bibliotecas.

Instale a biblioteca pandas:
~~~
pip install pandas
~~~
Para mais informações consulte a [documentação](https://pandas.pydata.org/docs/getting_started/install.html).

Instale o pacote IMDbPY:
~~~
pip install imdbpy
~~~
Para mais informações consulte a [documentação](https://imdbpy.readthedocs.io/en/latest/).

_Em alguns códigos pode ser necessário alterar o caminho para os arquivos._

## Arquivos:
* [addMovieData.py](/final/src/addMovieData.py)
  * Agrega dados de duração, classificação indicativa, avaliação do IMDb e enredo a tabela de filmes.
* [addTvShowData.py](/final/src/addTvShowData.py)
  * Agrega dados de duração, número de temporadas, classificação indicativa, avaliação do IMDb e enredo a tabela de séries.
* [addPeopleGenreData.py](/final/src/addPeopleGenreData.py)
  *  Agrega dados de atores, diretores, criadores e gêneros(usada para filmes e séries).
* [fixCertificate.py](/final/src/fixCertificate.py)
  * Converte o formato de classificação indicativa americado para o formato usado no Brasil(usada para filmes e séries).
* [fixYears.py](/final/src/fixYears.py)
  * Ajusta data das mídias que apresetam esse dado como um intervalo de valores(pode ser usado para todas as tabelas).
* [differentYears.py](/final/src/differentYears.py)
  * Trata a consistência dos anos de lançamento das mídias entre as tabelas(usado para tabelas normalizadas).
* [deleteDuplicate.py](/final/srs/deleteDuplicate.py)
  * Trata dados duplicados nas tabelas(pode ser usado para todas as tabelas). 
* [deleteNull.py](/final/src/deleteNull.py)
  * Trata dados nulos nas tabelas(pode ser usado para todas as tabelas).
