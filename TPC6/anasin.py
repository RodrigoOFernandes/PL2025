# aritmetica_anasin.py
# Parser para expressões aritméticas simples (+, -, *)
# ----------------------
from listas_analex import lexer

# Variável global para armazenar o próximo token
prox_simb = ('Erro', '', 0, 0)

# Função para tratar erros sintáticos
def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

# Função para reconhecer um token específico
def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)

# Regra para Fator → NUM
def rec_Fator():
    global prox_simb
    if prox_simb.type == 'NUM':
        print(f"Reconhecido NUM: {prox_simb.value}")
        rec_term('NUM')
    else:
        parserError(prox_simb)

# Regra para Termo → Fator ('*' Fator)*
def rec_Termo():
    global prox_simb
    rec_Fator()
    while prox_simb.type == 'TIMES':
        print("Reconhecido TIMES: *")
        rec_term('TIMES')
        rec_Fator()

# Regra para Expressão → Termo ('+' Termo | '-' Termo)*
def rec_Expressao():
    global prox_simb
    rec_Termo()
    while prox_simb.type in ('PLUS', 'MINUS'):
        if prox_simb.type == 'PLUS':
            print("Reconhecido PLUS: +")
            rec_term('PLUS')
        elif prox_simb.type == 'MINUS':
            print("Reconhecido MINUS: -")
            rec_term('MINUS')
        rec_Termo()

# Função principal do parser
def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_Expressao()
    if prox_simb.type != None:
        parserError(prox_simb)
    else:
        print("Expressão reconhecida com sucesso!")

# Teste do parser
if __name__ == "__main__":
    while True:
        try:
            # Solicita uma expressão ao usuário
            data = input("Digite uma expressão aritmética (ou 'sair' para terminar): ")
            if data.lower() == 'sair':
                print("Saindo...")
                break

            # Chama o parser para a expressão fornecida
            rec_Parser(data)

        except Exception as e:
            print(f"Erro: {e}")
