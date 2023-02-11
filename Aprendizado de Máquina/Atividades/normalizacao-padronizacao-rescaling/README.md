# Funções de Normalização, Padronização e Rescaling

- Professor: Jefferson de Oliveira Silva
- Disciplina: Projeto Integrado
- Curso: Ciência de Dados e Inteligência Artificial
- Semestre: 3º
- Data da entrega: 27/03/2022 11:59 PM

## Instruções

Implemente em Python as seguintes funções:

NORMALIZAÇÃO

Todos os valores da distribuição devem ser normalizados. Os exemplos a seguir ilustram os resultados:

- [1, 2, 3] => [0.0, 0.5, 1.0]
- [0, 5, 13] => [0.0, 0.38461538461538464, 1.0]

PADRONIZAÇÃO

Todos os valores da distribuição devem ser padronizados. Os exemplos a seguir ilustram os resultados:

- [1, 2, 3] => [-1.0, 0.0, 1.0]
- [0, 5, 13] => [-0.914991421995628, -0.15249857033260467, 1.0674899923282326]


RESCALING

Todos os valores da distribuição devem ser obedecer à nova escala, dado um novo mínimo e máximo. Por exemplo, para um novo min = 0 e um novo máx = 100.

- [1, 2, 3] =>[0.0, 50.00, 100.00]
- [0, 5, 13] =>[0.0, 38.46153846153846, 100.0]

NÃO UTILIZE BIBLIOTECAS PRONTAS PARA OS CÁLCULOS. Somente funções básicas como min, max, stdev podem ser utilizadas.