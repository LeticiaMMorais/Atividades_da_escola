A seção (<section>) é identificada porque ele faz parte de um todo e acompanha um título.



Aside traz informações extras. É muito utilizado para propagandas em sites, por exemplo. O aside não é exatamente uma barra de navegação. Você pode colocar links se tiverem algum conteúdo relacionado com o conteúdo da página. A navegação geral do site é com o nav.

---

Elementos em bloco são elementos que independentemente da largura dos elementos, eles ficarão um abaixo do outro.



Elementos em linha permitem que um continue a frente do outro. Eles não aceitam margem esquerda ou direita (então para centralizar uma imagem, pode-se usar **display:block;** para transformar em bloco e usar margem)

img, span, a, Strong, em... São elementos inline









# --------------------------------------------------------------------

# \-            ANOTAÇÕES DA AULA 17/07/2025                       -

# --------------------------------------------------------------------



Agora, na 2ª etapa, vamos fazer o wireframe (o figma é um wireframe) e apresentar as páginas que construímos com a explicação de por que escolhemos as cores, o tema, etc. com 5 minutos de apresentação.

Todos os integrantes devem estar preparados porque será feito um sorteio para decidir quem irá apresentar da equipe (apenas uma pessoa).



---



O cabeçalho é o local que serve para identificar o site e pode vir com o menu (barra de navegação) dentro dele. Mas o menu pode vir separado.



O que muda num site de uma página para outra é o conteúdo. Geralmente os cabeçalhos e rodapés não variam.



O copyright, geralmente, não precisa exatamente de um registro. Ele mostra quem é o dono e desde quando o dono tem aquele site.



O aside não está dentro do conteúdo, é como um extra e ele não faz parte do conteúdo principal. 



Todo o conteúdo da HOME precisa estar no main. Todo o conteúdo que eu tiver, ou seja, tudo o que tenho abaixo do cabeçalho e menu e acima do rodapé, exceto o aside, ficam dentro do **main**.





Pergunta: o que é container? #Você precisa saber

---



A seção precisa ser PARTE de um conteúdo, não o conteúdo todo, e precisa ter um título.



Como podemos fazer para que o cabeçalho e o menu acompanhem o tamanho da tela, faça uma div dentro deles e coloque a largura que você quer (a mesma do conteúdo, por exemplo) e *margin: auto;*



Os elementos inline permitem que tenham outros ao lado. Então se colocar vários links, por exemplo, que caibam no container, no espaço, eles ficarão um à frente do outro. Por isso não dá para adicionar margin em elementos inline. 



Para alterar o tipo do elemento (em bloco ou em linha), usa-se a propriedade **display** que pode ter como valores none, block e inline.





Há uma nova de combinar seletores: em vez de ler na linha da direita para a esquerda
main a {

&nbsp;	display: block;

}



podemos colocar dentro do seletor, como:

main{

&nbsp;	a{

&nbsp;		display:block;

&nbsp;	}

}



Essa forma só estava disponível para uma extensão do CSS, mas agora está com uma forma nativa.

































