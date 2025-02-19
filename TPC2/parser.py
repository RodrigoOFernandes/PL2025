import re

def parse_csv_with_regex(file_path):
    # Regex para capturar linhas completas com exatamente 7 campos
    pattern = re.compile(r'^([^;\n]+(?:\n[^;\n]+)*;){6}\w+$', re.MULTILINE)
    
    # Ler o arquivo CSV inteiro
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Encontrar todas as correspondências no conteúdo
    matches = pattern.finditer(content)
    
    # Lista para armazenar as obras corretamente separadas
    obras = []
    
    # Processar as correspondências
    for match in matches:
        linha = match.group(0)  # Captura a string completa correspondente ao regex
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

# Caminho do arquivo CSV
csv_path = "obras.csv"

# Executar o parser
obras = parse_csv_with_regex(csv_path)

# 1. Lista ordenada alfabeticamente dos compositores
compositores = sorted(list(set(obra['compositor'] for obra in obras)))
print("Compositores ordenados alfabeticamente:")
for compositor in compositores:
    print(compositor)

# 2. Distribuição das obras por período
distribuicao_periodo = {}
for obra in obras:
    periodo = obra['periodo']
    if periodo in distribuicao_periodo:
        distribuicao_periodo[periodo] += 1
    else:
        distribuicao_periodo[periodo] = 1
print("\nDistribuição das obras por período:")
for periodo, quantidade in distribuicao_periodo.items():
    print(f"{periodo}: {quantidade} obras")

# 3. Dicionário com listas alfabéticas dos títulos das obras por período
obras_por_periodo = {}
for obra in obras:
    periodo = obra['periodo']
    titulo = obra['nome']
    if periodo in obras_por_periodo:
        obras_por_periodo[periodo].append(titulo)
    else:
        obras_por_periodo[periodo] = [titulo]

# Ordenar as listas de títulos alfabeticamente
for periodo in obras_por_periodo:
    obras_por_periodo[periodo].sort()

print("\nTítulos das obras por período:")
for periodo, titulos in obras_por_periodo.items():
    print(f"{periodo}:")
    for titulo in titulos:
        print(f"  - {titulo}")

