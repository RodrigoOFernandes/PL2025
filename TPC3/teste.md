# 📄 TPC2 - Filtro de Obras Musicais por Período

## Resumo

Este script em Python lê um arquivo CSV (`obras.csv`) contendo informações sobre obras musicais, incluindo o título da obra, o período musical e o compositor. Utilizando expressões regulares (regex), o script processa o arquivo para garantir que apenas linhas corretamente formatadas sejam lidas. O programa gera um arquivo `resultado.txt` com as seguintes informações:

1. **Lista alfabética de compositores** cujas obras estão nos períodos selecionados.
2. **Distribuição das obras por período**, indicando quantas obras existem em cada período.
3. **Dicionário de períodos com títulos de obras ordenados**, mostrando as obras associadas a cada período.

## Expressão Regular Utilizada

Para garantir que cada linha contém exatamente 7 campos separados por `;`, utilizamos a seguinte regex:

```python
pattern = re.compile(r'([^;\n]*(?:\n[^;\n]+)*;){6}.+$', re.MULTILINE)
```

Essa regex assegura que cada linha corresponde ao formato esperado do CSV, permitindo que apenas registros válidos sejam processados.

### Funcionalidades

- Filtra obras musicais com base em períodos específicos.
- Utiliza regex para extrair apenas as linhas corretamente formatadas.
- Gera uma lista ordenada alfabeticamente dos compositores.
- Contabiliza o número de obras por período.
- Organiza as obras por período e as ordena alfabeticamente.
- Salva os resultados em um arquivo `resultado.txt`.

### Períodos Considerados

- Barroco
- Clássico
- Medieval
- Renascimento
- Século XX
- Contemporâneo
- Romântico

### Exemplo de Arquivo de Entrada (`obras.csv`)

```
Título;Instrumentação;Duração;Período;Compositor;Ano;Local
Sinfonia Nº 5;Orquestra;30min;Clássico;Beethoven;1808;Viena
As Quatro Estações;Orquestra;40min;Barroco;Vivaldi;1723;Veneza
Cantigas de Santa Maria;Voz e Instrumentos;20min;Medieval;Afonso X;1280;Espanha
```

### Saída Esperada no `resultado.txt`

```
Lista ordenada alfabeticamente dos compositores musicais:
Afonso X
Beethoven
Vivaldi

Distribuição das obras por período:
Barroco: 1 obras
Clássico: 1 obras
Medieval: 1 obras

Dicionário de períodos com títulos de obras ordenados:
Barroco: As Quatro Estações
Clássico: Sinfonia Nº 5
Medieval: Cantigas de Santa Maria
```

## Observações

- O script ignora a primeira linha do CSV, que geralmente contém cabeçalhos.
- Utiliza regex para garantir que apenas registros com 7 campos sejam processados corretamente.
- Caso o arquivo `obras.csv` não seja encontrado, o script exibirá uma mensagem de erro.

