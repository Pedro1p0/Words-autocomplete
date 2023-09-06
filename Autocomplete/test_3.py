import three_main
# Crie uma instância da árvore AVL e insira algumas palavras
avl_tree = three_main.AVLTree()
palavras = ["maçã", "banana", "laranja", "uva", "pera","peneira","umaia","lataria"]
for palavra in palavras:
    avl_tree.add(palavra)

# Encontre palavras que começam com o prefixo "la"
prefixo = "la"
palavras_com_prefixo = avl_tree.find_words_with_prefix(prefixo)

# Imprima as palavras encontradas
print("Palavras com o prefixo '{}':".format(prefixo))
for palavra in palavras_com_prefixo:
    print(palavra)


avl_tree.print_tree()