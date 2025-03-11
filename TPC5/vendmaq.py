import sys
import re
from datetime import datetime

def print_stock(stock_dict):
    for cod, data in stock_dict.items():
        print(f"Cod: {cod}, Nome: {data['nome']}, Quant: {data['quant']}, Preco: {data['preco']}")

    print("\n")

def parse_stock(stock_file):
    stock_dict = {}  

    try:
        with open(stock_file, 'r') as file:
            content = file.readlines()  
    except FileNotFoundError:
        print(f"Error: The file '{stock_file}' was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file '{stock_file}'.")
        return

    pattern = re.compile(r'{"cod": "(\w+)", "nome": "(.*)", "quant": (\d+), "preco": (.*)}')

    for line in content:
        match = pattern.match(line.strip()) 
        if match:
            cod, nome, quant, preco = match.groups()  
            stock_dict[cod] = {
                "nome": nome,
                "quant": int(quant), 
                "preco": float(preco) 
            }

    return stock_dict

def handle_inputs(stock_dict):
    print("QUE TU QUERES HUMANO\n")
    
    command = input("")
    
    if command == "LISTAR":
        print_stock(stock_dict)
    elif command == "SAIR":
        print("bye bye")
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <stock_file>")
        sys.exit(1)
    
    stock_file = sys.argv[1]
    stock_dict = parse_stock(stock_file)

    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{date}. EU FUI LIGADO (VOU DESTRUIR HUMANOS) STOCK ATUAL:\n ")
    print_stock(stock_dict)

    handle_inputs(stock_dict)


if __name__ == "__main__":
    main()
