"""
Heap é uma árvore binária quase completa representada num array.

Tipos:
    Max-Heap: cada nó >= seus filhos
    Min-Heap: cada nó <= seus filhos

Estrutura:
    "Quase completa" significa: todos os niveis estao completos execeto o último,
    que é preenchido da esquerda para a direita.

    É guardado em array: sem ponteiros, sem nós dinâmicos, espaço continuo -> eficiencia de cache
    + O(1) acesso.

    MAX-HEAP:
        Array: [20, 15, 10, 7, 9, 3, 2]

        Representação em árvore:
             20
               
         15     10
               
       7    9  3    2

   Importante:
    - Um heap não é ordenado. É apenas parcialmente ordenado:
        . O maior elemento está sempre na raiz no Max-Heap;
        . Mas não há relação entre elementos de ramos diferentes.

    Exemplo - válido como max-heap:
        [90, 50, 70, 10, 20, 30]

        - Mesmo que "70 > 50", isso não importa porque estão em subárvores diferentes.

    
    Operações básicas:
        Insert >> O(log n);
        Extract max/min >> O(log n);
        Build Heap >> O(n);
        Access root >> O(1)    
"""


def parent(i):
    return (i - 1) // 2 # (valido so para i > 0)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def in_bounds(i, n):
    return 0 <= i < n


def heapify_down(arr, n, i):
    """
    arr >> lista que representa o heap
    n >> tamanho valido do heap
    i >> indice que queremos ajustar

    Corrigir o nó da posição i se ele estiver menor do que alguns dos seus filhos,
    empurrando-o para baixo até que a propriedade do Max-Heap fique válida.
    """

    while True:
        l = left(i)
        r = right(i)
        largest = i

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


arr = [3, 19, 1, 14, 8, 7]
heapify_down(arr, len(arr), 0)
print(arr)