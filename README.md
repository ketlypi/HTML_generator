# HTML_generator

Esse aplicativo em Tkinter e aplicação em Python tem por objetivo gerar um HTML de imagens tomando como base as estruturas de repetição presentes nele.

1. Para utilizá-los, precisamos definir a quantidade de tags <td> vão ser geradas por tabela.

2. A quantidade de itens da lista garante que vamos preencher a quantidade de table's do HTML, já o número em cada idexação garante que vamos informar a quantidade de td's em cada table. Por exemplo:

Caso tenhamos 3 tags <table> e na segunda há 2 tags <td>. O campo precisará ser preenchido com: 1, 2, 1
Caso tenhamos 2 tags <table> e na primeira há 2 tags <td>. O campo precisará ser preenchido com: 2, 1

3. No campo URLs to add precisamos colocar todos os href's que estarão presentes no HTML separados por vírgula
Exemplo: https://google.com, https://youtube.com

4. Em posição dos URLs especificaremos que posição (que td) cada um dos URLs vai ocupar.

4.5. Preencher a Image Base (prefixo) das imagens que entrarão na tag <src> do HTML. Para isso, é necessário:
4.1. Que todas as imagens possuam o mesmo prefixo
4.2. Que as imagens estejam ordenas e com terminações 01, 02, 03... até, no máximo, 99.
4.3. Que o upload delas no SFMC já tenha sido realizado.
4.4. É necessário pegar o copy Publishied URL e apagar as terminações e nome de extensão, a fim de que preenchamos o campo somente com o prefixo das imagens.

6. Preencher a UTM Source e UTM Medium com seus respectivos valores.

7. Em Image Type colocaremos o formato das imagens que preencherão as tags <srcs>
Exemplo: jpg, png, gif

8. Em Image Type Alternativos colocaremos o formato de imagens que fogem a regra anterior. Ou seja, se há apenas um gif e as demais imagens são jpg, preencheremos esse campo com: gif. 

9. Em Posições para Image Type Alternativos diremos que posição(ões) os tipos alternativos de imagem vão ocupar no nosso HTML. 
Por exemplo: caso a terceira <td> tenha uma tag <src> com uma imagem em gif (como no exemplo anterior) preencheremos com: 3
Caso seja a terceira e quinta posições, preencheremos com: 3, 5 
E assim sucessivamente.

10. Em file name adicionamos o nome do arquivo sem extensão - que deve corresponder a UTM campaign

11. Por fim selecionamos a pasta de destino onde o arquivo HTML será salvo
