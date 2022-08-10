# Laboratório 12 de Python: Dia do Progresso I

12° projeto para submissão em Python de MC102 (Algoritmos e Programação de Computadores), curso ministrado pela UNICAMP.

Dando continuidade aos projetos desenvolvidos nos laboratórios de MC102 (explicação no repositório [IniciandoEmPython](https://github.com/laratoledom/IniciandoEmPython/blob/main/README.md)), temos como proposta de desenvolvimento do código o seguinte problema:
___

"Com a sua ajuda na fase da Batalha de Piltover, o projeto de desenvolvimento do jogo avançou. Com isso, o seu chefe te colocou em uma nova fase do projeto. Nesta fase, você precisará testar se Jayce, principal cientista de Piltover, conseguirá chegar na cidade para o Dia do Progresso, que é um feriado onde as principais invenções do ano são apresentadas para a população.

Jayce possui um mapa que contém um caminho, porém ele não sabe se o mapa o levará para Piltover. No mapa, existem indicações para onde Jayce deve andar:
-	<strong>N:</strong> Jayce deve andar para o Norte.
- <strong>S:</strong> Jayce deve andar para o Sul.
-	<strong>L:</strong> Jayce deve andar para o Leste.
-	<strong>O:</strong> Jayce deve andar para o Oeste.

Além dessas marcações <strong>(N, S, L e O)</strong>, existem <strong>bloqueios (indicados pelo caractere #)</strong>, a <strong>localização de Piltover (indicado pelo caractere *)</strong> e <strong>portais HexTechs (indicados por caracteres diferentes de N, S, L, O, # e *)</strong>. Os portais HexTech funcionam como teletransporte entre duas regiões e sempre aparecem em pares, ou seja, ao entrar em um portal no sentido norte, o personagem sairá no outro portal também no sentido norte.

O exemplo a seguir mostra um mapa que Jayce recebeu, sendo que a posição inicial dele é (2, 1) (em todos os casos, a contagem de linhas e colunas começam em 0, ou seja, a primeira posição do mapa é (0, 0)).<br><br>

<p align="center"> 
#&nbsp; #&nbsp; #&nbsp; # #&nbsp; #&nbsp; #&nbsp; * # <br>
# L&nbsp; L&nbsp; S #&nbsp; #&nbsp; #&nbsp; Q O <br>
# N&nbsp; S&nbsp; L&nbsp; L&nbsp; L&nbsp; L&nbsp; L N <br>
#&nbsp; # #&nbsp; # #&nbsp; # #&nbsp; # # <br>
T O O O O O O O Q <br>
#&nbsp; L&nbsp; L&nbsp; L&nbsp; L&nbsp; L&nbsp; L&nbsp; L&nbsp; N <br>
#&nbsp; N O O O O O O T </p>
<br>

Jayce andará para o norte, depois duas vezes para o leste, uma vez para o sul, cinco vezes para o leste, uma vez para o norte e uma vez para oeste, até encontrar o portal HexTech Q. Como Jayce entrou no portal vindo pelo oeste, ele sairá a oeste do outro portal Q (localizado na posição (4, 8)), ou seja, ele sairá na posição (4, 7). Na sequência, ele andará sete vezes para oeste e entrará no portal HexTech T, onde sairá na posição (6, 7), a oeste do outro portal T (localizado na posição (6,8)). Depois, andará seis vezes para oeste, uma vez para norte, sete vezes para leste e uma vez para norte, até encontrar o portal Q, saindo ao norte do outro portal Q (localizado na posição (1, 7)), ou seja, saindo na posição (0,7), onde está localizada a cidade de Piltover.

Caso Jayce saia do mapa, entre em loop (repita um caminho já feito) ou encontre um bloqueio, ele não conseguirá chegar em Piltover.

Portanto, sua tarefa será, dado um mapa, indicar se Jayce chegará ou não em Piltover. Para isto, seu código deverá ler um valor L, indicando quantas linhas o mapa possui, seguido por L linhas. Depois, o seu código deverá ler a posição inicial de Jayce.

Caso Jayce consiga chegar em Piltover, seu código deverá imprimir: <strong>"Jayce conseguiu chegar em Piltover"</strong>

Caso contrário, seu código deverá imprimir: <strong>"Jayce nao conseguiu chegar em Piltover"</strong>
<br><br>

<strong>Dica:</strong> Construa um dicionário com as posições de cada par de portais. Por exemplo, no exemplo acima, o dicionário teria o seguinte conteúdo: <br>
> print(portais) <br>
# {'Q': [[1, 7], [4, 8]], 'T': [[4, 0], [6, 8]]} <br>
> print(portais["T"]) <br>
# [[4, 0], [6, 8]] <br>
> print(portais["T"][0]) <br>
# [4, 0] <br>
> print(portais["T"][1]) <br>
# [6, 8] <br>
___

<strong>Observações:</strong> O arquivo foi executado através do PyCharm e no arquivo "testes" podem ser encontrados alguns exemplos de testes que verificam o código.


