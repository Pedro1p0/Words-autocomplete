import three_main


# Cria uma instância da árvore AVL
avl_tree = three_main.AVLTree()
avl_tree2 = three_main.AVLTree()
# Insira valores na árvore
valores = [10, 5, 15, 3, 7, 12, 18]
valores2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for valor in valores:
    avl_tree.add(valor)


for valor in valores2:
    avl_tree2.add(valor)

# Verifique se a árvore contém valores específicos
print(avl_tree.contains(5))  # Deve retornar True
print(avl_tree.contains(8))  # Deve retornar False

# Verifique a altura da árvore
print("Altura da árvore:", avl_tree.get_height())



avl_tree.print_tree()

avl_tree2.print_tree()