import re

def parse_csv_with_regex(file_path):
    pattern = re.compile(r'([^;\n]*(?:\n[^;\n]+)*;){6}.+$', re.MULTILINE)
    
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()[1:]  # Skip the first line
    
    matches = pattern.finditer("".join(content))
    
    obras = []
    
    for match in matches:
        linha = match.group(0)
        fields = linha.strip().split(';')  
        if len(fields) == 7:  
            obras.append({
                'nome': fields[0],
                'desc': fields[1],
                'anoCriacao': fields[2],
                'periodo': fields[3],
                'compositor': fields[4],
                'duracao': fields[5],
                '_id': fields[6]
            })
    
    return obras

csv_path = "obras.csv"
obras = parse_csv_with_regex(csv_path)

compositores = sorted(list(set(obra['compositor'] for obra in obras)))
distribuicao_periodo = {}
obras_por_periodo = {}

for obra in obras:
    periodo = obra['periodo']
    titulo = obra['nome']
    
    distribuicao_periodo[periodo] = distribuicao_periodo.get(periodo, 0) + 1
    
    if periodo in obras_por_periodo:
        obras_por_periodo[periodo].append(titulo)
    else:
        obras_por_periodo[periodo] = [titulo]

for periodo in obras_por_periodo:
    obras_por_periodo[periodo].sort()

with open("resultados.txt", "w", encoding="utf-8") as f:
    f.write("Compositores ordenados alfabeticamente:\n")
    f.writelines(f"{compositor}\n" for compositor in compositores)
    
    f.write("\nDistribuição das obras por período:\n")
    f.writelines(f"{periodo}: {quantidade} obras\n" for periodo, quantidade in distribuicao_periodo.items())
    
    f.write("\nTítulos das obras por período:\n")
    for periodo, titulos in obras_por_periodo.items():
        f.write(f"{periodo}:\n")
        f.writelines(f"  - {titulo}\n" for titulo in titulos)
