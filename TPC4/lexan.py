import re
import sys

def tokenize(code):
    token_specification = [
        ('COMMENT', r'#.*'),
        ('NUM', r'\b\d+\b'),
        ('CA', r'\{'),
        ('CF', r'\}'),
        ('POINT', r'\.'),
        ('IDIOM', r'@[a-zA-Z]+'),
        ('SELECT', r'\bselect\b', re.IGNORECASE),
        ('WHERE', r'\bwhere\b', re.IGNORECASE),
        ('LIMIT', r'\bLIMIT\b', re.IGNORECASE),
        ('VARS', r'\?[a-zA-Z_][a-zA-Z0-9_]*'),
        ('A', r'\ba\b'),
        ('URIS', r'[a-zA-Z]+:[A-Za-z0-9_/-]*'),
        ('LITS', r'"[^"]*"'),
        ('NEWLINE', r'\n'),
        ('SKIP',  r'[ \t]+'),       
        ('ERRO',  r'.'),
    ]

    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id, expreg, *flags) in token_specification])
    reconhecidos = []
    linha = 1
    mo = re.finditer(tok_regex, code)
    
    for m in mo:
        tipo = m.lastgroup
        valor = m.group(tipo)
        if tipo == 'COMMENT' or tipo == 'SKIP':
            continue
        elif tipo == 'NUM':
            valor = int(valor)
        elif tipo == 'ERRO':
            print(f"Erro léxico na linha {linha}: {valor}", file=sys.stderr)
            continue
        
        reconhecidos.append((tipo, valor, linha, m.span()))
        
        if tipo == 'NEWLINE':
            linha += 1

    return reconhecidos

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <arquivo>", file=sys.stderr)
        sys.exit(1)

    caminho = sys.argv[1]
    try:
        with open(caminho, 'r') as file:
            texto = file.read()
    except IOError as e:
        print(f"Erro ao abrir o arquivo: {e}", file=sys.stderr)
        sys.exit(1)

    tokens = tokenize(texto)

    try:
        with open("resultados.txt", "w") as f:
            for token in tokens:
                f.write(f"{token}\n")
    except IOError as e:
        print(f"Erro ao escrever no arquivo: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
