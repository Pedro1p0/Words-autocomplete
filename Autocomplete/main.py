import three_main
# Lista de palavras a serem removidas
palavras_removidas = set(["e", "ou", "mas", "a", "o"])

# Função para carregar o arquivo, separar em palavras e remover stop words
def process_text_file(file_path):
    #lendo o arquivo
    with open(file_path, 'r', encoding='utf-8') as file:
        # Ler o conteúdo do arquivo em uma string
        text = file.read()

        # Converte todo o texto para minúsculas
        text = text.lower()

        # Remove pontuação e caracteres especiais
        import string
        text = ''.join(char for char in text if char not in string.punctuation)

        # Divide o texto em palavras usando espaços como delimitadores
        palavras = text.split()

        # Remova as stop palavras
        palavras_filtradas = [word for word in palavras if word not in palavras_removidas]

        return palavras_filtradas

# capitulo de a arte da guerra
file_path = 'arte_da_guerra.txt'
palavras_filtradas = process_text_file(file_path)

# Imprima as palavras filtradas
for word in palavras_filtradas:
    print(word)

# Inicia a arvore
avl_tree = three_main.AVLTree()

# Preenche a arvore
for palavra in palavras_filtradas:
    avl_tree.add(palavra)

# printa a arvore
avl_tree.print_tree()

# Buscar o préfixo ou palavra
prefixo = 'lu'
palavras_com_prefixo = avl_tree.find_words_with_prefix(prefixo)
print("Palavras com o prefixo '{}':".format(prefixo))
for palavra in palavras_com_prefixo:
    print(palavra)