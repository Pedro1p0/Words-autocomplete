import three_main


# Cria uma instância da árvore AVL
avl_tree = three_main.AVLTree()

strings = ["maçã", "banana", "laranja", "uva", "pera", "peneira","arvore"]

for palavra in strings:
    avl_tree.add(palavra)

print(avl_tree.contains("laranja"))  # Deve retornar True

print("Altura da árvore:", avl_tree.get_height())

avl_tree.print_tree()