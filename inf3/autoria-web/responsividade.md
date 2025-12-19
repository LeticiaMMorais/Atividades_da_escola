# RESPONSIVIDADE

## Grandezas

### Grandezas absolutas

Os valores absolutos são aqueles que não muda mesmo que a tela seja maior ou menor.

- px
- cm
- mm
- in
- pt
- pc

Nós, quando precisamos de uma medida absoluta, usamos o **px** (pixel).

### Grandezas relativas

Se adaptam de acordo com o tamanho da tela.

- em
- ex
- ch
- fr
- rem
- vw
- vh
- vmin
- vmax
- %

Nós, dessas grandezas, trabalhamos bem com o vh e o vw...

o vh e o vw se refere a 1% da **tela**, já o *%* trabalha como o tamanho do elemento pai.

O correto para a responsividade é usar o rem... O rem usa como base a **fonte base**, então 1rem = _tamanho da fonte base_, que a gente pode alterar em uma pseudo classe chamada `:root`. (Também dá certo no seletor html, mas a :root é mais usasda) 

Ex:

    :root {
        font-size: 20px; 
        /*Estou alterando a fonte base para 20px, 
        sendo que o padrão é 16px*/
    }


## Variáveis
Na `:root` também podemos definir variáveis. As variáveis são definidas ao colocar dois hifens (--) antes do nome da variável:
    
    :root {
        font-size: 20px;
        --color-text: #222
    }

## Tamanho mínimo e máximo
`min-height` -- define a altura mínima

`max-height` -- define a altura máxima

`min-width` -- define a largura mínima

`max-width` -- define a largura máxima

São usadas com um valor absoluto em conjunto com o tamanho (height ou width) definido em um valor relativo.

## Elemento &lt;picture&gt;
Já não é muito utilizada, mas seria colocar várias opções de imagem. 
Geralmente é utilizada quando queremos mudar a imagem de acordo com uma o tamanho da tela e não só redimensiná-la.

## Breakpoint - media query
Um dos tamanhos de breakpoint (largura mínima) são: 320px | 720px | 1200px | 1980px

Quero dizer:
- Resolução FULL DESKTOP - mínimo de 1980px
- Resolução DESKTOP menor - mínimo de 1200px e máximo de 1979px
- Resolução TABLET - mínimo de 720px e máximo de 1199px
- Resolução CELULAR - mínimo de 320px e máximo de 719px

Para aplicar essas resoluções e definirmos um estilo específico para cada resolução, usamos a regra de mídia: `@media` (media query). Se comparar, é como se fosse uma função que será executada quando tiver uma condição atendida.

    
    @media(<condição>) {
        <código>
    }

exemplo real: 
    
    @media(max-width: 720px) {
        img {
            max-heigth: 500px;
        }
    }