import re
import sys

def tokenize(code):
    token_specification = [
        ('COMMENT', r'#.*'),
        ('NUM', r'\b\d+\b'),
        ('CA', r'{'),
        ('CF', r'}'),
        ('POINT', r'\.'),
        ('SELECT', r'\bselect\b'),
        ('WHERE', r'\bwhere\b'),
        ('LIMIT', r'\blimit\b'),
        ('IDENTS', r'\b\?\[a-z]+\b'),
        ('A', r'a'),
        ('NEWLINE', r'\n'),
        ('SKIP',  r'[ \t]+'),       
        ('ERRO',  r'.')
    
def main():
    for linha in sys.stdin:
        token = tokenize(linha)
        print(token)

if __name__ == "__main__":
    main()
