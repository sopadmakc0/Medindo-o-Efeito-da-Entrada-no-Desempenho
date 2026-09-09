# Medindo-o-Efeito-da-Entrada-no-Desempenho

Nome: João Gabriel Silva de Melo

# O que foi Investigado: 
O par que foi usado foi BST simples vs AVL e eles foram usados pra testar o tempo de inserção de dados para a construção de índices em banco de dados. O objetivo foi provar na prática como o pior caso (dados já ordenados) degrada o desempenho de uma árvore não balanceada e como a AVL resolve esse problema matematicamente através de rotações. Foram utilizados 5 tamanhos de entrada (1.000 a 16.000), medindo a mediana de 3 execuções válidas (descartando o warm-up) com semente fixa.


## o que encontrei:
<img width="596" height="551" alt="image" src="https://github.com/user-attachments/assets/274e726e-fc00-41bf-9dcd-06f51e152ba1" />


## 1. Cenário Aleatório(O mundo Ideal)
Ambas as árvores apresentaram um crescimento de tempo próximo à classe O(N log N). Ao dobrar o tamanho da entrada, o tempo de execução aumentou um pouco mais que o dobro (razão em torno de 2.1). A BST foi levemente mais rápida nesse cenário, pois apenas insere os dados, sem o overhead de checar o fator de balanceamento e executar rotações.

## 2. Cenário Ordenado(O Pior Caso)
Aqui a diferença foi brutal.
 A BST degenerou para uma lista encadeada (virou uma linha reta). Sua classe de crescimento passou a ser quadrática: O(N²). Como mostrado na tabela, quando dobramos a entrada (ex: de 8.000 para 16.000), o tempo multiplicou por quase 4x (razão ~4.0).
 A AVL manteve sua eficiência O(N log N). O tempo continuou subindo de forma linear-logarítmica (razão ~2.1x), pois a árvore se auto-balanceou em cada inserção, mantendo a altura mínima possível.

## Como Rodar
1. Certifique-se de ter o Python 3 instalado.
2. Navegue até a pasta raiz deste repositório.
3. Execute o script principal: `python src/main.py`
4. Os resultados brutos serão salvos automaticamente em `dados/resultados_medicoes.csv`.
