# Lógica Quantificacional

Grupo: Lucas Lopes Amorim, Isaac Higuchi, Gustavo Tessitore

## Especificação

O projeto consiste no desenvolvimento (em Python) de um prompt de comando em que se pode inserir frases, formuladas numa sintaxe próxima da linguagem natural (que definiremos abaixo), que irão compor uma ``base de crenças'' de uma pessoa. Para cada nova inserção p, deve-se verificar:

1. se p é uma tautologia ou contradição; se esse for o caso, não adicionar p na base de dados e imprimir ``p não possui conteúdo informacional''.
2. se p é uma consequência dedutiva de outras sentenças já inseridas; se esse for o caso, não adicionar p na base de dados e imprimir ``informação redundante'';
3. se a adição de p faz a base de dados ficar inconsistente; nesse caso, não adicionar p na base de dados e imprimir ``informação conflitante com a base de crenças'' (opcional: deixar o usuário escolher entre desistir de adicionar p ou remover outras frases já inseridas até que a inserção de p não torne mais a base de crenças inconsistente).

Para realizar a tarefa, sugere-se iniciar com o projeto já implementado de lógica proposicional (ou com a solução proposta pelo professor, disponibilizada no canal). Deve-se implementar a técnica de tableaux para realizar a tarefa. Deve-se considerar que as frases que serão inseridas são do tipo:

1. S é P (ex.: "Sócrates é homem.")
2. S não é P (ex.: "Raul não é cientista.")
3. Todo S é P / Todos os S são Ps (ex.: "Todos os homens são mortais.")
4. Todo S não é P / Todos os S não são Ps (ex.: "Todos os homens não são répteis.")
5. Algum S é P (ex.: "Algum homem é mortal")
6. Algum S não é P (ex.: "Algum homem não é palmeirense.")
7. Nenhum S é P (ex.: "Nenhum homem é réptil.")
8. Nenhum S não é P (ex.: "Nenhum homem não é humano.")

Lembrem-se de que vocês também terão que fazer a apresentação no dia 01/12 do projeto. As apresentações ocorrerão no Laboratório 10. A ordem das apresentações será decidida em sala de aula. Não hesitem em me enviar mensagem em caso de dúvida. Como combinado na aula anterior, no dia 17/11 eu ficarei disponível no Teams em horário de aula para dúvidas em relação à implementação do projeto.

## Exemplos de erros ao adicionar premissas

### Contradição

```
$ Algum homem não é homem
Error: A frase entra em conflito consigo mesma e não possui conteúdo informacional
```

### Redundância

```
$ Sócrates é homem
$ Todo homem é mortal
$ Sócrates é mortal
Error: Sócrates é mortal é uma informação que pode ser inferida
com base nas premisas anteriores
```

### Tautologia

````
$ Todo homem é homem
Error: A frase é uma repetição desnecessária de uma ideia e não possui conteúdo informacional
````

### Inconsistência

```
$ Sócrates é homem
$ Todo homem é mortal
$ Sócrates não é mortal
Error: Informação conflitante com as premisas anteriores
```

## Apresentação

- 10min no máximo (5min de apresentação e 5min para o professor testar)
- grupos de 4 a 5 pessoas
- dinâmica da apresentação: "Olha, vamos testar com essa frase aqui, com essas premisas"
- o código deve estar funcionando porque eu vou pedir que vocês insiram algumas crenças


## Referências

- https://www.nltk.org/book_1ed/ch10.html
- https://www.nltk.org/howto/inference.html

## Ideia dada pelo professor de como começar a implementação
- Entender a referência de implementação da Lógica Proposicional disponibilizada pelo professor
- Entender o objetivo do trabalho que se dará modelado numa função main
- Entender o funcionamento da função TableauProver (biblioteca: Nltk)
- Refletir sobre a estrutura de implementação
- Criar uma função de tradução da linguagem lógica para a linguagem lógica do TableauProver
- Testar usando o Nltk TableauProver
- Criar a função main do programa
- Desenvolver testes unitários utilizando pytest

### Função main

A cada frase inserida verifica 4 coisas:
- É uma Tautologia?
- É uma Contradição?
- A fase tem valor informacional baseado nas outras crenças já estabelecidas? (teste de redundancia: todo homem é mortal; socrátes é homem; sócrates é mortal)
- Contradiz outras crenças já estabelecidas? (teste de consistência)

Professor: "O tableau faz essas 4 verificações, e você tem que montar 4 Tableaus":

1) pra tautologia, argumentos (c, [])
2) pra contradição (~c, [])
3) pra redundancia (c, [p1, p2,...])
4) pra consistência (~c, [p1, p2, ...])

## Desafio da Consistência
**(Este é um desafio que refinará o trabalho, não é o objetivo principal do programa, por isso deve ser considerado após todo o desenvolvimento)**

Para identificação das crenças que causam uma inconsistência, basta retirar as crenças existentes da base de crenças e verificar se ainda a inconsistência num laço. Como exemplo teremos:

```
    Crenças = [p1, p2, p3, p4] -> TableauProver(~c, Crenças) -> Inconsistente
              [p1, p2, p4] -> TableauProver(~c, Crenças) -> Consistente
              [p1, p3, p4] -> TableauProver(~c, Crenças) -> Consistente
              [p2, p3, p4] -> TableauProver(~c, Crenças) -> Inconsistente
```

Ou seja, quando inserimos a nova crença *p4* em nossa Base de Crenças ela se torna Inconsistente devido a outras crenças já estabelecidas.

Ao retirar a crença *p3*, a base volta a ser consistente, assim também como a crença *p2* quando retirada.

Portanto, para adicionar a crença *p4* à Base de Crenças, o usuário deverá escolher uma das crenças, *p2* ou *p3*, à ser descartada. Caso não queira que uma das crenças estabelecidas sejam descartadas, o usuário deverá optar pelo descarte da nova crença *p4*.