import sys
import re
from datetime import datetime

def print_stock(stock_dict):
    print("maq:\n")
    print("cod | nome | quantidade | preço")
    print("---------------------------------")
    for cod, data in stock_dict.items():
        print(f"{cod} {data['nome']} {data['quant']} {data['preco']:.2f}")
    print()

def parse_stock(stock_file):
    stock_dict = {}
    try:
        with open(stock_file, 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{stock_file}' was not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Could not read the file '{stock_file}'.")
        sys.exit(1)

    pattern = re.compile(r'\{"cod": "(\w+)", "nome": "(.*?)", "quant": (\d+), "preco": ([\d.]+)\}')

    for line in content:
        match = pattern.match(line.strip())
        if match:
            cod, nome, quant, preco = match.groups()
            stock_dict[cod] = {"nome": nome, "quant": int(quant), "preco": float(preco)}
    return stock_dict

def save_stock(stock_file, stock_dict):
    with open(stock_file, 'w') as file:
        file.write('{\n "stock": [\n')
        for cod, data in stock_dict.items():
            file.write(f'{{"cod": "{cod}", "nome": "{data["nome"]}", "quant": {data["quant"]}, "preco": {data["preco"]:.2f}}}\n')
        file.write('    ]\n}')

def calcular_troco(saldo):
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]  
    troco = {}
    centavos = int(saldo * 100)
    for moeda in moedas:
        if centavos >= moeda:
            troco[moeda] = centavos // moeda
            centavos %= moeda
    return troco

def handle_inputs(stock_dict, stock_file):
    saldo = 0.0
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    while True:
        command = input(">> ")
        if command == "LISTAR":
            print_stock(stock_dict)
        elif command.startswith("MOEDA"):
            valores = re.findall(r'\d+[ec]', command)
            for v in valores:
                if 'e' in v:
                    saldo += int(v.replace('e', ''))
                elif 'c' in v:
                    saldo += int(v.replace('c', '')) / 100
            print(f"maq: Saldo = {int(saldo)}e{int((saldo*100) % 100)}c")
        elif command.startswith("SELECIONAR"):
            match = re.match(r'SELECIONAR (\w+)', command)
            if match:
                cod = match.group(1)
                if cod in stock_dict and stock_dict[cod]["quant"] > 0:
                    preco = stock_dict[cod]["preco"]
                    if saldo >= preco:
                        saldo -= preco
                        stock_dict[cod]["quant"] -= 1
                        print(f"maq: Pode retirar o produto dispensado \"{stock_dict[cod]['nome']}\"")
                        print(f"maq: Saldo = {int(saldo*100) // 100}e{int(saldo*100) % 100}c")
                    else:
                        print("maq: Saldo insufuciente para satisfazer o seu pedido")
                        print(f"maq: Saldo = {int(saldo*100) // 100}e{int(saldo*100) % 100}c; Pedido = {int(preco*100) // 100}e{int(preco*100) % 100}c")
                else:
                    print("maq: Produto inexistente ou esgotado")
        elif command == "SAIR":
            troco = calcular_troco(saldo)
            troco_str = ", ".join([f"{v}x {k//100}e{int(k%100)}c" if k >= 100 else f"{v}x {k}c" for k, v in troco.items()])
            if troco_str:
                print(f"maq: Pode retirar o troco: {troco_str}.")
            print("maq: Até à próxima")
            save_stock(stock_file, stock_dict)
            break

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <stock_file>")
        sys.exit(1)
    
    stock_file = sys.argv[1]
    stock_dict = parse_stock(stock_file)
    
    print(f"maq: {datetime.today().strftime('%Y-%m-%d')}, Stock carregado, Estado atualizado.")
    handle_inputs(stock_dict, stock_file)

if __name__ == "__main__":
    main()
