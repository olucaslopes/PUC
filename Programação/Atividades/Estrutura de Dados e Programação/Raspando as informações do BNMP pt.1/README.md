# Raspando as informações do BNMP pt.1

A partir da seleção de um Estado no portalbnmp, contido no caderno Jupyter desenvolvido em aula, escreva o código que faça a raspagem de todos os números de mandados (internação e prisão) contidos na primeira página. 

A atividade pode ser feita em grupos, que devem ser devidamente identificados no seu caderno. Somente uma pessoa por grupo precisa entregar o caderno.


## Minha submissão

### Repositório atualizado disponível em: https://github.com/olucaslopes/BNMP-Scraper

### GRUPO: LUCAS LOPES E GUSTAVO TESSITORE

Para que o programa funcione é preciso adicionar um cookie válido(e não expirado) em utils/envVars.py, seguem as instruções:

1) Acesse https://portalbnmp.cnj.jus.br/#/pesquisa-peca e passe pelo captcha

2) Selecione um estado aleatório na aba "Pesquisar peças"

3) Entre no modo desenvolvedor do seu navegador(tecla F12) e vá até a aba Network do modo desenvolvedor

4) Com a aba Network aberta e o estado selecionado, clique em pesquisar

5) Uma requisição com nome começando com "filter?" deve aparecer na aba Network, clique nessa requisição

6) Na aba Headers da requisição, encontre a opção "Request Headers"

7) Dentro das "Request Headers" procure por um valor chamado "cookie", clique com o botão direito e copie esse valor

8) Agora dentro do diretório do programa, entre na pasta utils e em seguida abra o arquivo envVars.py

9) Na linha 29 você deve encontrar uma variável chamada "cookie" já atribuída a uma string, apague ela e cole esse
valor que você copiou(não esqueça de colar "entre aspas" como string)

10) Pronto, agora o programa está pronto pra funcionar :). Só é preciso rodar o arquivo IdsPostRequestsGetter.py