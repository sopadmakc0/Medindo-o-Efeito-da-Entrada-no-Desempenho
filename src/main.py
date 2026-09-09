
import time
import random
import statistics
import csv


class NodeBST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    
    def insert(self, key):
        if self.root is None:
            self.root = NodeBST(key)
            return
        
        atual = self.root
        while True:
            if key < atual.key:
                if atual.left is None:
                    atual.left = NodeBST(key)
                    break
                atual = atual.left
            else:
                if atual.right is None:
                    atual.right = NodeBST(key)
                    break
                atual = atual.right


class NodeAVL:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node: return 0
        return node.height

    def get_balance(self, node):
        if not node: return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def _insert(self, node, key):
        if not node:
            return NodeAVL(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)







def mede_tempo_insercao(tree_class, dados):
    
    arvore = tree_class()
    inicio = time.perf_counter()
    for valor in dados:
        arvore.insert(valor)
    fim = time.perf_counter()
    return (fim - inicio) * 1000 

def executar_experimento():
    tamanhos = [1000, 2000, 4000, 8000, 16000]
    algoritmos = [("BST", BST), ("AVL", AVL)]
    cenarios = ["Aleatorio", "Ordenado"]
    

    random.seed(42) 
    
    resultados = []

    print("Iniciando bateria de testes...\n")

    for cenario in cenarios:
        for nome_algo, classe_algo in algoritmos:
            for n in tamanhos:
                
                
                if cenario == "Aleatorio":
                    entrada = [random.randint(1, 100000) for _ in range(n)]
                else:
                    
                    entrada = list(range(1, n + 1)) 

                tempos_execucao = []
                
                
                for i in range(4):
                    tempo = mede_tempo_insercao(classe_algo, entrada)
                    if i > 0: 
                        tempos_execucao.append(tempo)
                
                
                mediana = statistics.median(tempos_execucao)
                
                print(f"Cenário: {cenario:9} | Algo: {nome_algo:3} | Tamanho: {n:5} | Mediana: {mediana:8.2f} ms")
                resultados.append([cenario, nome_algo, n, round(mediana, 2)])

    
    import os
    os.makedirs('../dados', exist_ok=True) 
    
    with open('../dados/resultados_medicoes.csv', mode='w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['Cenario', 'Algoritmo', 'Tamanho', 'Tempo_Mediano_ms'])
        writer.writerows(resultados)
        
    print("\nTestes finalizados! Resultados salvos em 'dados/resultados_medicoes.csv'")

if __name__ == "__main__":
    executar_experimento()
