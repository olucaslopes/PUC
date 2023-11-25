# Lógica

site: https://nltk.org/howto/inference.html

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

Lembrem-se de que vocês também terão que fazer a apresentação no dia 24/11 do projeto. As apresentações ocorrerão no Laboratório 10. A ordem das apresentações será decidida em sala de aula. Não hesitem em me enviar mensagem em caso de dúvida. Como combinado na aula anterior, no dia 17/11 eu ficarei disponível no Teams em horário de aula para dúvidas em relação à implementação do projeto.


## Apresentação

10min no máximo (5 de apresentação e 5 pro prof testar)
- grupos de 4 a 5 pessoas

"Olha, vamos testar com essa frase aqui, com essas premisas"
- o código deve estar funcionando porque eu vou pedir que vocês insiram algumas crenças


## Referências

- https://www.nltk.org/book_1ed/ch10.html
- https://www.nltk.org/howto/inference.html


## Dicionário
- tautologia

## Como começar
- dar uma olhada no c´doigo da lógica proposicional
- ver função main
- pensar em como implementar
- fazer uma função de tradução
- testa usando a nltk
- pensar em como alterar o gabarito da lógica proposicional no teams para abarcar a lógica quantificacional
- rodar lógica


A cada fraase inserida verifica 4 coisas:
- tautologia?
- contradição?
- segue das outras crenças (teste de redundancia: todo homem é mortal; socrátes é homem; sócrates é mortal)
- contradiz as outras crenãs? (consistencia)

Professor: "O tableau faz essas 4 verificações, mas você tem que montar 4 Tableaus":

i) pra tautologia, argumentos (c, [])
ii) pra contradição (~c, [])
iii) pra redundancia (c, [p1, p2,...])
iv) pra consistência (~c, [p1, p2, ...])