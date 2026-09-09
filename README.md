# Medindo-o-Efeito-da-Entrada-no-Desempenho

Nome: João Gabriel Silva de Melo

# O que foi Investigado: 
O par que foi usado foi BST simples vs AVL e eles foram usados pra testar o tempo de inserção de dados para a construção de índices em banco de dados. O objetivo foi provar na prática como o pior caso (dados já ordenados) degrada o desempenho de uma árvore não balanceada e como a AVL resolve esse problema matematicamente através de rotações. Foram utilizados 5 tamanhos de entrada (1.000 a 16.000), medindo a mediana de 3 execuções válidas (descartando o warm-up) com semente fixa.


# o que encontrei:
Cenario,Algoritmo,Tamanho,Tempo_Mediano_ms
Aleatorio,BST,1000,0.44
Aleatorio,BST,2000,1.05
Aleatorio,BST,4000,2.47
Aleatorio,BST,8000,5.73
Aleatorio,BST,16000,14.43
Aleatorio,AVL,1000,4.15
Aleatorio,AVL,2000,8.36
Aleatorio,AVL,4000,18.91
Aleatorio,AVL,8000,37.58
Aleatorio,AVL,16000,84.38
Ordenado,BST,1000,12.29
Ordenado,BST,2000,44.02
Ordenado,BST,4000,185.81
Ordenado,BST,8000,707.82
Ordenado,BST,16000,2901.75
Ordenado,AVL,1000,4.01
Ordenado,AVL,2000,8.49
Ordenado,AVL,4000,16.92
Ordenado,AVL,8000,38.2
Ordenado,AVL,16000,76.15

Cenario,Algoritmo,Tamanho,Tempo_Mediano_ms
Aleatorio,BST,1000,0.45
Aleatorio,BST,2000,1.05
Aleatorio,BST,4000,2.61
Aleatorio,BST,8000,5.63
Aleatorio,BST,16000,11.95
Aleatorio,AVL,1000,3.65
Aleatorio,AVL,2000,12.73
Aleatorio,AVL,4000,28.35
Aleatorio,AVL,8000,37.0
Aleatorio,AVL,16000,80.13
Ordenado,BST,1000,11.18
Ordenado,BST,2000,45.09
Ordenado,BST,4000,191.2
Ordenado,BST,8000,697.99
Ordenado,BST,16000,2836.48
Ordenado,AVL,1000,4.38
Ordenado,AVL,2000,8.66
Ordenado,AVL,4000,19.47
Ordenado,AVL,8000,42.13
Ordenado,AVL,16000,87.93

# 1. Cenário Aleatório(O mundo Ideal)
Ambas as árvores apresentaram um crescimento de tempo próximo à classe O(N log N). Ao dobrar o tamanho da entrada, o tempo de execução aumentou um pouco mais que o dobro (razão em torno de 2.1). A BST foi levemente mais rápida nesse cenário, pois apenas insere os dados, sem o overhead de checar o fator de balanceamento e executar rotações.

# 2. Cenário Ordenado(O Pior Caso)
Aqui a diferença foi brutal.
 A BST degenerou para uma lista encadeada (virou uma linha reta). Sua classe de crescimento passou a ser quadrática: O(N²). Como mostrado na tabela, quando dobramos a entrada (ex: de 8.000 para 16.000), o tempo multiplicou por quase 4x (razão ~4.0).
 A AVL manteve sua eficiência O(N log N). O tempo continuou subindo de forma linear-logarítmica (razão ~2.1x), pois a árvore se auto-balanceou em cada inserção, mantendo a altura mínima possível.

# Como Rodar
1. Certifique-se de ter o Python 3 instalado.
2. Navegue até a pasta raiz deste repositório.
3. Execute o script principal: `python src/main.py`
4. Os resultados brutos serão salvos automaticamente em `dados/resultados_medicoes.csv`.
