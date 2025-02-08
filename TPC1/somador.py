import sys

def parser(caminho_do_arquivo):
    try:
        somador = 0
        somar = True
        buffer = ""
        buffer_num = ""

        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo, open("resultado.txt", "w", encoding="utf-8") as resultado:
            conteudo = arquivo.read()
            for caractere in conteudo:
                if caractere.isalpha():
                    buffer += caractere 
                else:
                    buffer = ""

                if "Off" in buffer:
                    somar = False                
                elif "On" in buffer:
                    somar = True 

                if caractere.isdigit():
                    buffer_num += caractere
                else:
                    if buffer_num:
                        if somar:
                            somador += int(buffer_num)
                        buffer_num = ""

                if caractere == "=":
                    resultado.write(f"Soma até '=': {somador}\n")

            if somar and buffer_num:
                somador += int(buffer_num)

            resultado.write(f"Soma final: {somador}\n")

    except FileNotFoundError:
        print("Erro: o arquivo não foi encontrado")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 somador.py <caminho_do_arquivo>")
    else:
        caminho_do_arquivo = sys.argv[1]
        parser(caminho_do_arquivo)
