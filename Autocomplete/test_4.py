import three_main

corpus = "O sol brilha durante o dia enquanto a lua brilha durante a noite ilumina com a luz do luar a paisagem a descansar."
avl_tree = three_main.AVLTree()
palavras = corpus.split()
a=[]
for word in palavras:
    a.append(word.lower())  # Converta para minúsculas para evitar diferenças de maiúsculas/minúsculas

for palavra in palavras:
    avl_tree.add(palavra)
print(a)
avl_tree.print_tree()

prefixo = 'lu'
palavras_com_prefixo = avl_tree.find_words_with_prefix(prefixo)
print("Palavras com o prefixo '{}':".format(prefixo))
for palavra in palavras_com_prefixo:
    print(palavra)