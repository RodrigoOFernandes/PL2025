# Conversor de Markdown para HTML

Este projeto é um conversor simples de Markdown para HTML, utilizando expressões regulares com grupos nomeados e a função `re.sub` da biblioteca padrão do Python.

## Funcionalidades

O script converte os seguintes elementos do Markdown para HTML:
- **Cabeçalhos** (`#`, `##`, `###`) → `<h1>`, `<h2>`, `<h3>`
- **Negrito** (`**texto**`) → `<b>texto</b>`
- **Itálico** (`*texto*`) → `<i>texto</i>`
- **Listas numeradas** (`1. item`) → `<ol><li>item</li></ol>`
- **Links** (`[texto](url)`) → `<a href="url">texto</a>`
- **Imagens** (`![alt](src)`) → `<img src="src" alt="alt"/>`

## Uso de `re.sub` e Grupos Nomeados

O script utiliza `re.sub()` para substituir padrões Markdown por seus equivalentes HTML. Os grupos nomeados tornam as expressões regulares mais legíveis e fáceis de manipular:

- **Cabeçalhos:**
  ```python
  re.sub(r'^(?P<hlevel>#{1,3})\s+(?P<text>.+)$',
         lambda m: f"<h{len(m.group('hlevel'))}>{m.group('text')}</h{len(m.group('hlevel'))}>",
         md_text, flags=re.MULTILINE)
  ```
  Aqui, `hlevel` captura o nível do cabeçalho (`#`, `##`, `###`), e `text` captura o conteúdo. O comprimento do `hlevel` determina a tag HTML (`h1`, `h2`, `h3`).

- **Negrito e Itálico:**
  ```python
  re.sub(r'\*\*(?P<text>.*?)\*\*', r'<b>\g<text></b>', md_text)
  re.sub(r'\*(?P<text>.*?)\*', r'<i>\g<text></i>', md_text)
  ```
  `text` captura o conteúdo entre `**` (negrito) ou `*` (itálico) e o substitui pela respectiva tag HTML.

- **Listas numeradas:**
  ```python
  re.sub(r'(?P<items>(?:\d+\.\s+.+\n?)+)', replace_list, md_text)
  ```
  `items` captura toda a lista numerada e a função `replace_list` processa os itens individualmente.

- **Links e Imagens:**
  ```python
  re.sub(r'\[(?P<text>.*?)\]\((?P<url>.*?)\)', r'<a href="\g<url>">\g<text></a>', md_text)
  re.sub(r'!\[(?P<alt>.*?)\]\((?P<src>.*?)\)', r'<img src="\g<src>" alt="\g<alt>"/>', md_text)
  ```
  Aqui, `text` captura o texto visível do link e `url` o endereço. Para imagens, `alt` captura o texto alternativo e `src` o caminho da imagem.

## Como Usar

Execute o script fornecendo um ficheiro Markdown como argumento:

```sh
python script.py exemplo.md
```

O script gera um ficheiro HTML com o mesmo nome do ficheiro Markdown, substituindo a extensão `.md` por `.html`.

## Exemplo de Entrada e Saída

**Entrada (`teste.md`):**
```md
# Título
Texto com **negrito** e *itálico*.

1. Item 1
2. Item 2

[Link](http://exemplo.com)
![Imagem](http://exemplo.com/imagem.jpg)
```

**Saída (`teste.html`):**
```html
<h1>Título</h1>
<p>Texto com <b>negrito</b> e <i>itálico</i>.</p>

<ol>
<li>Item 1</li>
<li>Item 2</li>
</ol>

<a href="http://exemplo.com">Link</a>
<img src="http://exemplo.com/imagem.jpg" alt="Imagem"/>
```

## Requisitos
- Python 3.x

## Conclusão
Este conversor usa expressões regulares e `re.sub()` com grupos nomeados para tornar a conversão eficiente e legível. É uma solução simples e extensível para converter sintaxe básica de Markdown em HTML.

