# Equipe `MC536 & Chill` - `Chill`
* `André Vila Nova Wagner da Costa` - `213081`
* `Cristiano Sampaio Pinheiro` - `256352`
* `George Gigilas Junior` - `216741`

## Modelo Lógico Combinado do Banco de Dados de Grafos
> ![Grafo modelo logico](images/grafo_modelo_logico.png)
> 
> _Figura 1: Grafo do modelo lógico_
> 
> ![Grafo projecao midia](images/grafo_projecao_midia.png)
> 
> _Figura 2: Grafo da projeção com relação a participação das pessoas nas mídias_
> 
> ![Grafo projecao genero](images/grafo-projecao-genero.png)
> 
> _Figura 3: Grafo da projeção com relação ao gênero das obras trabalhadas por cada pessoa_

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

>
### Pergunta/Análise 1
> * Dado que uma pessoa X trabalhou com uma pessoa Y e uma pessoa Z, qual a chance de Y trabalhar com Z em um projeto futuro?
>   
>   * Para responder esta pergunta, podemos fazer uma análise da modalidade predição de links que, com base nas conexões do grafo da Figura 2, atribui um valor de 0 a 1 que indica a probabilidade de essas pessoas trabalharem juntas no futuro. 

### Pergunta/Análise 2
> * Como podemos mapear a flexibilidade de atores e diretores quanto ao gênero da obra trabalhada?
>   
>   * Para responder esta pergunta, podemos fazer uma análise de formação de comunidade a partir do grafo da Figura 3. Com ele, podemos avaliar quais atores/diretores tendem a participar mais de obras de um determinado gênero a partir das comunidades formadas.

### Pergunta/Análise 3
> * Quais atores/diretores são mais populares no meio cinematográfico?
>   
>   * Para responder esta pergunta, podemos fazer uma análise de centralidade a partir do grafo da Figura 2. Com ele, podemos criar um sistema que atribui um valor para cada pessoa com base no número de ligações com outras pessoas que essa pessoa possui. Além disso, podemos aplicar um peso ponderado para ligações com pessoas mais populares. A partir disso, poderemos atribuir um valor de popularidade para cada pessoa e ver quem são os atores/diretores mais centrais.
