# Words-autocomplete
# Projeto de Autocompletar Palavras usando Árvore AVL

Este projeto consiste em criar um sistema de autocompletar palavras usando uma árvore AVL. O sistema é capaz de sugerir palavras completas com base em um prefixo fornecido pelo usuário. O projeto foi desenvolvido como parte de um trabalho acadêmico na disciplina DCA0209 - ALGORITMOS E ESTRUTURAS DE DADOS II - T01 da Universidade Federal do Rio Grande do Norte.

# Equipe
- Pedro Henrique Bezerra Fernandes
- Pedro Vitor Bezerra Clemente

# Visão Geral
Neste projeto, utilizamos um corpus de texto como entrada e realizamos as seguintes etapas:

1.Pré-processamento do Corpus:
- Conversão de todo o texto para letras minúsculas.
- Remoção de pontuações e caracteres especiais.
- Divisão do texto em palavras.
- Opcional: remoção de palavras de parada.
2.Construção da Árvore AVL:
- Inserção de todas as palavras únicas do corpus em uma árvore AVL para otimizar a busca subsequente.
3.Autocompletar:
- Implementação de uma função que retorna palavras que começam com um determinado prefixo, percorrendo a árvore AVL. A função para de buscar assim que encontrar um nó que não corresponda ao prefixo.

## Exemplo de Uso

Aqui estão alguns exemplos de como usar o nosso sistema de autocompletar palavras usando uma árvore AVL:

1. **Exemplo 1:**
   - **Entrada:**
     - Corpus: "O sol brilha durante o dia enquanto a lua brilha durante a noite."
     - Prefixo: "du"
   - **Saída:**
     - Lista de Palavras: ["durante"]

2. **Exemplo 2:**
   - **Entrada:**
     - Corpus: "O gato caça o rato, enquanto o cachorro caça o gato."
     - Prefixo: "ca"
   - **Saída:**
     - Lista de Palavras: ["caça", "cachorro"]

1. **Exemplo de Código:**
```python
import three_main

Crie uma instância da árvore AVL e insira algumas palavras
avl_tree = three_main.AVLTree()
palavras = ["maçã", "banana", "laranja", "uva", "pera","peneira","umaia","lataria"]
for palavra in palavras:
avl_tree.add(palavra)

Encontre palavras que começam com o prefixo "la"
prefixo = "la"
palavras_com_prefixo = avl_tree.find_words_with_prefix(prefixo)

Imprima as palavras encontradas
print("Palavras com o prefixo '{}':".format(prefixo))
for palavra in palavras_com_prefixo:
print(palavra)

avl_tree.print_tree()
```
   
   Neste exemplo, mostramos como chamar a função de autocompletar no nosso código.

2. **Exemplo de Resultado:**
![Resultado no VSCode](https://github.com/Pedro1p0/Words-autocomplete/raw/main/Autocomplete/resul_AED.png)

   
   
   Este é o resultado da função de autocompletar, que retorna uma lista de palavras correspondentes.

# Explicaçao em video
[Assista ao vídeo](https://www.youtube.com/embed/98V-UI0NGlg)

<iframe width="560" height="315" src="https://www.youtube.com/embed/98V-UI0NGlg" frameborder="0" allowfullscreen></iframe>




