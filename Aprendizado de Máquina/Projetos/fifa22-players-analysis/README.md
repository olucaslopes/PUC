# Machine Learning: Desvendando o FIFA 22

<p align="center">
    <img src="img/cover-wide.png" width="60%">
</p>

Análise e predição dos atributos dos jogadores do jogo FIFA 22.

[ESSE PROJETO POSSUI UM REPOSITÓRIO PRÓPRIO, PARA ACESSÁ-LO CLIQUE AQUI](https://github.com/olucaslopes/fifa22-players-analysis)

> Esse projeto foi desenvolvido durante o 3 semestre da graduação em Ciência de Dados e Inteligência Artificial na PUC-SP e entregue no dia 17/06/2022

## 1. Contextualização

O mercado de *E-sports* é muito competitivo e necessita que cada decisão seja tomada cuidadosamente. Para o apoio da tomada de decisão, é preciso analisar uma quantidade muito grande de atributos, o que torna difícil para um ser humano, mesmo sendo um jogador profissional, assimilar todas as "regras de negócio" do jogo para que ele possa manifestar o seu melhor desempenho.

O modo *Ultimate Team* é particularmente mais desafiador. Nele o jogador inicia o jogo com um time modesto e precisa além de desempenhar bem nos jogos, de uma grande capacidade de gerenciamento do seu time para poder evoluir, além de conhecimento sobre futebol porque nem toda carta (jogador de futebol dentro do jogo) boa se encaixa no time por uma questão de entrosamento, estilo de jogo e seu gosto pessoal. Quando olhamos para o alto nível de desempenho dos jogadores profissionais então, cada pequena melhora, cada oportunidade, pode mudar totalmente o resultado da partida. Então, como aspirantes a cientistas de dados, decidimos desenvolver um software baseado em modelos de machine learning para recomendar a melhor carta para diversas situações de jogo, como cobranças de falta e escanteios, ajudando os jogadores à alcançarem o ápice de seu desempenho atingindo níveis ainda mais altos.

Dessa forma, iremos prever:
- o valor de mercado (€) dos jogadores
- os atributos dos goleiros (pace, shooting, passing, dribbling, defending, physic)
- se um jogador é ou não considerado especialista em tiro livre

## 2. Requisitos do projeto

Ao desenvolver esse projeto precisamos cumprir uma série de requisitos das disciplinas de Projeto Integrado (Machine Learning), Engenharia de Software e Banco de Dados. A lista completa de requisitos está no arquivo <a href="task-description.pdf">task-description.pdf</a>


## 3. Descrição dos dados

<img align="right" src="img/features.png" width="40%" >

O dataset usado nesse projeto [pode ser encontrado no Kaggle](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset)

Número de instâncias (linhas): 19.239

Número de atributos (preditores): 91

Número de atributos após pré-processamento : 337

Variáveis alvo:
- valor de mercado (€): `value_eur`
- atributos dos goleiros: `pace`, `shooting`, `passing`, `dribbling`, `defending`, `physic`
- especialista em tiro livre: `#FK Specialist` (gerada a partir do OneHotEncode da coluna _player_tags_)

## 5. Modelagem e Avaliação de Modelos

### Algorítmos usados:
- Floresta Aleatória de Regressão
- Regressão Linear
- Regressão Logística
- Floresta Aleatória de Classificação

## 6. Resultados

### 6.1 Prevendo valor de mercado (€) dos jogadores com diferentes modelos:

| modelo/métrica | R² | MSE | MAE |
| -- | -- | -- | -- |
| DummyRegressor | -0.0000 | 6.356740e+13 | 3.168331e+06 |
| LinearRegression | 0.9715 | 1.530026e+12 | 4.978524e+05 |
| RandomForestRegressor | 0.9743 | 1.651936e+12 | 1.887077e+05 |

### 6.2 Prevendo atributos dos jogadores com Regressão Linear:

| atributo/métrica | R² | MSE | MAE |
| -- | -- | -- | -- |
| pace | 0.9993 | 0.0863 | 0.2511 |
| shooting | 0.9990 | 0.1897 | 0.3485 |
| passing | 0.9958 | 0.4239 | 0.4824 |
| dribbling | 0.9991 | 0.0873	 | 0.2548 |
| defending | 0.9997 | 0.0861 | 0.2542 |
| physic | 0.9991 | 0.0852 | 0.2524 |

### 6.3 Prevendo jogadores rolutados como especialistas de tiro livre:

> No relatório, construímos os modelos de modo que eles pudessem prever qualquer uma dos rótulos (tags) dos jogadores porém, resolvemos nos aprofundar no rótudo `#FK Specialist` (em português, _especialista em tiro livre_)

| modelo/métrica | acurácia | precisão | revocação | f1-score |
| -- | -- | -- | -- | -- |
| LogisticRegression | 1.00 | 0.92 | 0.93| 0.93 |
| LogisticRegressionCV | 1.00 | 1.00 | 1.00 | 1.00 |
| RandomForestClassifier | 1.00 | 1.00 | 1.00 | 1.00 |

Discussão:

As métricas realmente mostram-se muito boas. Modelos mais robustos, como `LogisticRegressionCV` e `RandomForestClassifier` foram capazes de obter 100% de acurária, o que parece irreal. A partir daí, surgiram 3 hipóteses para explicar o porquê isso poderia ter acontecido:

- nosso modelo tinha aprendido a regra de negócio
- overfitting
- haviam poucos dados para avaliarmos a eficácia do modelo

Como exploramos no caderno, para prever o rótulo de `#FK Specialist` para os jogadores do nosso dataset, uma só feature parece ser responsável por essa classificação

<p align="center"><img src="img/skill-fk-vs-tag-fk-spec.png" width="40%"></p>

Logo, nosso modelo pode ter aprendido a regra do negócio, e por isso ele acerta com tamanha precisão os resultados.

Porém, é preciso cautela ao afirmar isso, pois o dataset é muito desbalanceado (a classe positiva para `# FK Specialist` é rara). Logo, se pudessemos coletar mais dados poderíamos afirmar com mais precisão que aprendemos a regra do negócio.

## 7. Apresentação em Vídeo

<p align="center">
    <a href="https://youtu.be/h9QZWgI6Wlw"><img alt="Apresentação projeto" width="75%" src="img/video-thumbnail.png" /></a>
</p>