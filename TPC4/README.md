# Analisador Léxico para SPARQL

## Descrição
Este projeto consiste em um analisador léxico para a linguagem SPARQL, implementado em Python. O analisador identifica e categoriza os tokens presentes em um código SPARQL, como palavras-chave, variáveis, números, literais, URIs, entre outros. Ele também detecta e reporta erros léxicos.

## Funcionalidades
- Reconhece palavras-chave como `SELECT`, `WHERE` e `LIMIT`.
- Identifica variáveis (`?var`) e URIs (`prefixo:recurso`).
- Processa literais (`"texto"`), números e símbolos especiais (`{}`, `.`).
- Ignora espaços em branco e comentários.
- Reporta erros léxicos encontrados no código.

## Como Usar
1. Certifique-se de ter o Python instalado.
2. Salve o código do analisador em um arquivo `lexer.py`.
3. Execute o script e forneça a entrada via `stdin`, por exemplo:
   ```sh
   echo 'SELECT ?x WHERE { ?x a "Pessoa" . }' | python3 lexer.py
   ```
4. O programa imprimirá os tokens reconhecidos.

## Exemplo de Saída
Para a entrada:
```sparql
SELECT ?x WHERE { ?x a "Pessoa" . }
```
A saída será algo como:
```sh
('SELECT', 'SELECT', 1, (0, 6))
('VARS', '?x', 1, (7, 9))
('WHERE', 'WHERE', 1, (10, 15))
('CA', '{', 1, (16, 17))
('VARS', '?x', 1, (18, 20))
('A', 'a', 1, (21, 22))
('LITS', 'Pessoa', 1, (23, 31))
('POINT', '.', 1, (32, 33))
('CF', '}', 1, (34, 35))
```

## Estrutura do Código
- **tokenize(code):** Função principal que recebe um código SPARQL e retorna uma lista de tokens.
- **main():** Lê a entrada do usuário e imprime os tokens processados.

## Conclusão

Este analisador léxico serve como uma base sólida para a análise de consultas SPARQL, permitindo identificar corretamente os componentes fundamentais da linguagem.
