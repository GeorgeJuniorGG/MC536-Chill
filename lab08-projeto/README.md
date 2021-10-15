# Equipe `MC536 & Chill` - `Chill`
* `André Vila Nova Wagner da Costa` - `213081`
* `Cristiano Sampaio Pinheiro` - `256352`
* `George Gigilas Junior` - `216741`

## Modelo Lógico Combinado do Banco de Dados de Grafos
> Coloque aqui o modelo ou modelos que serão usados pela equipe combinando os individuais, conforme especificação.
> Utilize este [modelo de base](https://docs.google.com/presentation/d/10RN7bDKUka_Ro2_41WyEE76Wxm4AioiJOrsh6BRY3Kk/edit?usp=sharing) para construir o seu.
> Coloque a imagem do PNG do seu modelo lógico como ilustrado abaixo (a imagem estará na pasta `image`):
>
> ![Modelo Lógico de Grafos](images/modelo-logico-grafos.png)

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

>
### Pergunta/Análise 1
> * Dado que uma pessoa X trabalhou com uma pessoa Y e uma pessoa Z, qual a chance de Y trabalhar com Z em um projeto futuro?
>   
>   * Para responder esta pergunta, podemos fazer uma análise da modalidade predição de links que, com base nas conexões do grafo da Figura 2, atribui um valor de 0 a 1 que indica a probabilidade de essas pessoas trabalharem juntas no futuro. 

### Pergunta/Análise 2
> * Como podemos mapear a flexibilidade de atores e diretores quanto ao gênero da obra trablhada?
>   
>   * Para responder esta pergunta, podemos fazer uma análise da modalidade centralidade com relação ao "betweenness" a partir do grafo da Figura 3. Com ele, podemos avaliar o valor do betweenness de cada pessoa e observar a formação de comunidades e das conexões entre elas. 

### Pergunta/Análise 3
> * Quanto a morte ou aposentadoria de um ator ou diretor impacta na produção de novos filmes e séries?
>   
>   * Para responder esta pergunta, podemos fazer uma análise da modalidade vulnerabilidade, a partir do grafo da Figura 2. Com ele, podemos analisar qual o impacto no grafo quando uma pessoa (ator ou diretor) é removida, a partir do índice visto em aula.
