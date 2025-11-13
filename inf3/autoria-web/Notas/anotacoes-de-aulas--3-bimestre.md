# overflow
Tem os seguintes valores para a propriedade:
## visible
É o padrão do Overflow, deixa todo o conteúdo vísivel mesmo que ultrapasse os limites.
## hidden
Esconde tudo o que transborda o container. Não tem barra de rolagem.
### scroll
Adiciona rolagem vertical e horizontal se necessário. 
Há navegadores que irão aparecer só as barras necessárias e outros que irão aparecer a barra vazia (o que é esperado, muitas vezes)
## auto
Adiciona a barra de rolagem apenas onde é necessário. Só vertical, só horizontal ou as duas (quando transborda), apenas as que são necessárias.

# position
## float: (...);
Funciona com qualquer tipo de elemento. (Em bloco ou em linha)
Deixa o conteúdo "flutuante" e pode receber como valores: ```float: left;``` e ```float: right;```
Sendo que o conteúdo que está abaixo irá subir para o lado oposto.

Geralmente é aplicado quando queremos um texto com uma imagem ao lado.

### clear
anula o efeito do float sobre o elemento aplicado (deixando abaixo, e não ao lado).

---
Aula dia 17/10/2025
---
## position: relative;
Leva em consideração a posição do elemento pai. 

Sendo que há as propriedades ```top```, ```left```, ```right``` e ```bottom``` que vão a afastar o tamanho que você colocar do lado/posição da propriedade. Se for ```top: 32px;```, por exemplo, o elemento irá se afastar 32px do topo.

## position: absolute;
Leva em consideração mais coisas, na verdade ele irá procurar o elemento mais próximo do qual ele descende que estiver com o position: relative; para se basear.

Também aceita propriedades ```top```, ```left```, ```right``` e ```bottom```.

## position: fixed;
Deixa o elemento fixo na tela - o tempo todo.

### z-index
Trabalha com as 3 dimensões. 
Ele posiciona os elementos colocando um atrás do outro. Quanto maior o valor do index, mais a frente ele fica.

Para elementos que nós queremos que eles fiquem sempre à frente, coloca-se um valor muito alto, como __1000__ e os outros, nós trabalhamos com números menores. 


## position: sticky;
Ora é um posicionamento estático, ora é um posicionamento fixo. 
Ele é estático enquanto a rolagem não chega até ele, pois quando o alcança, ele se torna fixo.