# Analisador Léxico e Sintático para Expressões Aritméticas

Este projeto consiste na implementação de um **analisador léxico** (lexer) e um **analisador sintático** (parser) para reconhecer e validar expressões aritméticas simples, como `2 + 5 * 3`. O analisador léxico é responsável por tokenizar a entrada, enquanto o analisador sintático verifica se a sequência de tokens segue as regras gramaticais definidas.

---

## **Funcionalidades**
1. **Análise Léxica**:
   - Reconhece números inteiros (`NUM`).
   - Reconhece operadores aritméticos: `+` (PLUS), `-` (MINUS), `*` (TIMES).
   - Ignora espaços em branco e novas linhas (`\n`).

2. **Análise Sintática**:
   - Valida expressões aritméticas sem parênteses.
   - Respeita a precedência de operadores (multiplicação antes de adição e subtração).

---

## **Como Usar**

### **Estrutura do Projeto**
O projeto é composto por dois ficheiros principais:
1. **`listas_analex.py`**: Implementa o analisador léxico.
2. **`aritmetica_anasin.py`**: Implementa o analisador sintático.


## **Exemplos de Uso**

### **Entrada Válida**
```
Digite uma expressão aritmética (ou 'sair' para terminar): 10 - 2 * 3 + 4
```

#### **Saída**:
```
Reconhecido NUM: 10
Reconhecido MINUS: -
Reconhecido NUM: 2
Reconhecido TIMES: *
Reconhecido NUM: 3
Reconhecido PLUS: +
Reconhecido NUM: 4
Expressão reconhecida com sucesso!
```

### **Entrada Inválida**
```
Digite uma expressão aritmética (ou 'sair' para terminar): 2 + * 3
```

#### **Saída**:
```
Reconhecido NUM: 2
Reconhecido PLUS: +
Erro sintático, token inesperado:  *
```

---

## **Gramática Implementada**
O analisador sintático segue a seguinte gramática:
1. **Expressão** → **Termo** (`+` **Termo** | `-` **Termo`)*
2. **Termo** → **Fator** (`*` **Fator`)*
3. **Fator** → `NUM`

---

## **Limitações**
- Não suporta parênteses para alterar a precedência de operações.
- Não suporta divisão (`/`) ou outros operadores.
- Não realiza cálculos, apenas valida a estrutura da expressão.


