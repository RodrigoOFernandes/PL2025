import re

def main():
    compositores = set()  
    periodos_interesse = {"Barroco", "Clássico", "Medieval", "Renascimento", "Século XX", "Contemporâneo", "Romântico"}
    periodos_count = {periodo: 0 for periodo in periodos_interesse}  
    periodos_obras = {periodo: [] for periodo in periodos_interesse}  
    
    with open("obras.csv", 'r', encoding="utf-8") as file: 
        data = file.read()  
        regex = r'^(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?)$'
        
        lines = re.findall(regex, data, re.MULTILINE | re.DOTALL)
        
        for line in lines[1:]:  
            nome_obra = line[0].strip()
            periodo = line[3].strip()  
            compositor = line[4].strip() 
            
            if periodo in periodos_interesse:
                compositores.add(compositor)
                
                if periodo in periodos_count:
                    periodos_count[periodo] += 1
                else:
                    periodos_count[periodo] = 1
                
                if periodo in periodos_obras:
                    periodos_obras[periodo].append(nome_obra)
                else:
                    periodos_obras[periodo] = [nome_obra]
    
    compositores_ordenados = sorted(compositores)
    
    for periodo in periodos_obras:
        periodos_obras[periodo].sort()
    
    with open("resultado.txt", 'w', encoding="utf-8") as output_file:
        output_file.write("Lista ordenada alfabeticamente dos compositores musicais:\n")
        for compositor in compositores_ordenados:
            output_file.write(compositor + "\n")
        
        output_file.write("\nDistribuição das obras por período:\n")
        for periodo, count in periodos_count.items():
            output_file.write(f"{periodo}: {count} obras\n")
        
        output_file.write("\nDicionário de períodos com títulos de obras ordenados:\n")
        for periodo, obras in periodos_obras.items():
            output_file.write(f"{periodo}: {', '.join(obras)}\n")

if __name__ == "__main__":
    main()