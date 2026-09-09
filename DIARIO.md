# Diário do Trabalho


## O que eu esperava antes de Medir
Como estou aplicando isso ao contexto de balanceamento de arvores onde o Par escolhido foi AVL e BTS, aminha hipótese principal seria que a árvore AVL seria superior no pior caso, mantendo a complexidade em O(n log n).

No cenário aleatório, eu esperava que a BST simples fosse um pouco mais rápida, pois a AVL precisaria gastar ciclos de CPU extras recalculando a altura dos nós e fazendo as rotações (LL, RR, LR, RL) que, numa entrada já aleatorizada, acabam sendo menos cruciais do que no pior caso.

## O que deu errado e como foi resolvido
Durante os Primeiros testes da BST com entrada ordenada (o pior caso), o meu programa em python encerrou a execução com um erro `RecursionError`.

Demorei um pouco para compreender a situação, mas percebi que a culpa não era do ambiente em si, mas sim que na prática da teoria estava funcionando: como os dados estavam ordenados (1,2,3...) a árvore virou uma "linha reta" infinita para a direita. Ao tentar inserir o 16.000° elemento usando uma função recursiva, a chamada tentou descer 16.000 níveis, estourando o limite da pilha de chamadas nativa do Python.

**A solução:** Tive que reescrever o método insert da minha classe BST pra ser iterativo(usando um laço while) em vez de recursivo. Assim, conseguimos rodar o pior caso sem estourar a memória da linguagem e assim eu pude coletar os tempos que provam a degeneração da árvore para O(n²).Esse erro acabou afirmando pra mim como um algoritmo não otimizado para pior caso quebra um sistema real
