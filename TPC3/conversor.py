import re
import sys

def markdown_to_html(md_text):
    md_text = re.sub(r'^(?P<hlevel>#{1,3})\s+(?P<text>.+)$',
                      lambda m: f"<h{len(m.group('hlevel'))}>{m.group('text')}</h{len(m.group('hlevel'))}>",
                      md_text, flags=re.MULTILINE)
    
    md_text = re.sub(r'\*\*(?P<text>.*?)\*\*', r'<b>\g<text></b>', md_text)
    
    md_text = re.sub(r'\*(?P<text>.*?)\*', r'<i>\g<text></i>', md_text)
    
    def replace_list(match):
        items = match.group('items').split('\n')
        items = [f"<li>{item.strip()[3:]}</li>" for item in items]
        return "<ol>\n" + "\n".join(items) + "\n</ol>"
    
    md_text = re.sub(r'(?P<items>(?:\d+\.\s+.+\n?)+)', replace_list, md_text)
    
    md_text = re.sub(r'\[(?P<text>.*?)\]\((?P<url>.*?)\)', r'<a href="\g<url>">\g<text></a>', md_text)
    
    md_text = re.sub(r'!\[(?P<alt>.*?)\]\((?P<src>.*?)\)', r'<img src="\g<src>" alt="\g<alt>"/>', md_text)
    
    return md_text

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <ficheiro_markdown.md>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = input_file.replace('.md', '.html')
    
    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            md_text = md_file.read()
        
        html_text = markdown_to_html(md_text)
        
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_text)
        
        print(f"Ficheiro HTML gerado com sucesso: {output_file}")
    
    except FileNotFoundError:
        print(f"Erro: Ficheiro '{input_file}' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()