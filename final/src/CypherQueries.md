# Queries em Cypher para responder perguntas propostas

## Retornando atores que já atuaram ao lado de Tom Hanks
```cypher
MATCH (tom:Ator {Ator: "Tom Hanks"})-[:Atuou]->(:Titulo)<-[:Atuou]-(p:Ator) return p
```

## Retornando ator que fez mais filmes/séries
```cypher
MATCH (b)-[:Atuou]->(a)
RETURN b, COLLECT(a) as atores
ORDER BY SIZE(atores) DESC LIMIT 1
```

## Retornando ator que participou de mais gêneros de filmes/séries
```cypher
MATCH (b)-[:Atuou]->(a)<-[:Genero]-(c)
RETURN b, COLLECT(c) as atores
ORDER BY SIZE(atores) DESC LIMIT 1
```

## Retornando elementos que estão até 2 arestas de distância de Alba Flores
```cypher
MATCH (p:Ator {Ator: 'Alba Flores'})-[*1..2]-(hollywood) return DISTINCT p, hollywood
```

## Retornando atores que já co-atuaram com Mark Hamill
```cypher
MATCH c=(p:Ator {Ator: 'Mark Hamill'})-[:CoAtuou]-(q:Ator) return c
```
