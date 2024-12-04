# Documentação do Projeto - Teoria dos Grafos

### **Objetivo da Aplicação**
A aplicação desenvolvida tem como objetivo resolver problemas clássicos de grafos, utilizando os conceitos e algoritmos estudados no curso.
Dentre os problemas abordados estão o **problema do carteiro chinês (grafos Eulerianos)**, o **problema do caixeiro viajante (grafos Hamiltonianos)**, o **menor caminho entre dois vértices**, a **árvore expansiva de custo mínimo** e a **coloração de grafos**.

### **Conteúdos Abordados**
- **Representação Computacional de Grafos:** Matrizes de adjacência, incidência e custo.
- **Problema Euleriano (Carteiro Chinês):** Algoritmo de Fleury.
- **Problema Hamiltoniano (Caixeiro Viajante):** Solução por permutações de vértices.
- **Algoritmo de Dijkstra:** Para encontrar o menor caminho entre dois vértices.
- **Árvore Expansiva de Custo Mínimo:** Algoritmos de **Prim** e **Kruskal**.
- **Coloração de Grafos:** Atribuição de cores aos vértices.

---

## **Desenvolvimento**

### **Estrutura da Aplicação**
A aplicação foi construída utilizando **Python**, com a biblioteca **NetworkX** para manipulação de grafos e **Matplotlib** para visualização gráfica.

A estrutura principal da aplicação é a classe **Grafo**, que permite a criação de grafos e a implementação dos algoritmos relacionados aos problemas estudados.

#### **Funcionalidades Implementadas**

1. **Representação Computacional de Grafos:**
   - A classe **Grafo** utiliza matrizes como a **matriz de adjacência** e **matriz de custo** para armazenar os dados do grafo.

2. **Problema Euleriano (Carteiro Chinês):**
   - Implementação do **algoritmo de Fleury** para determinar se um grafo tem um ciclo Euleriano e, caso tenha, retorna o caminho correspondente.

3. **Problema Hamiltoniano (Caixeiro Viajante):**
   - Implementação de um método que encontra o **caminho Hamiltoniano**, ou seja, um caminho que passa por todos os vértices do grafo exatamente uma vez.

4. **Menor Caminho entre Vértices (Algoritmo de Dijkstra):**
   - O método **menor_caminho()** usa o algoritmo de **Dijkstra** para encontrar o caminho de menor custo entre dois vértices, considerando os pesos das arestas.

5. **Árvore Expansiva de Custo Mínimo:**
   - Implementação dos algoritmos **Prim** e **Kruskal** para calcular a árvore geradora mínima de um grafo.

6. **Coloração de Grafos:**
   - A aplicação resolve problemas de **coloração** de grafos, atribuindo cores aos vértices de modo que vértices adjacentes não tenham a mesma cor.

### **Interação com o Usuário**
A aplicação oferece um menu interativo no terminal que permite ao usuário:

- Adicionar vértices e arestas ao grafo.
- Visualizar o grafo gerado.
- Resolver problemas Eulerianos e Hamiltonianos.
- Calcular o menor caminho entre dois vértices.
- Encontrar a árvore de custo mínimo.
- Resolver problemas de coloração de grafos.

---

## **Conclusão**

O projeto foi uma aplicação prática dos conceitos estudados durante o curso de **Teoria dos Grafos**, permitindo resolver problemas clássicos de grafos como o **problema do carteiro chinês**, o **problema do caixeiro viajante**, o **menor caminho entre dois vértices**, a **árvore expansiva de custo mínimo** e a **coloração de grafos**. A implementação dos algoritmos estudados, como **Dijkstra**, **Fleury**, **Prim** e **Kruskal**, trouxe uma compreensão mais profunda de como os grafos podem ser manipulados computacionalmente.

A aplicação serviu como uma excelente ferramenta para entender a teoria por trás dos algoritmos e também para visualizar como esses problemas são resolvidos de forma prática. Com o uso de bibliotecas como **NetworkX** e **Matplotlib**, foi possível criar não apenas a lógica de resolução dos problemas, mas também uma interface visual para facilitar a compreensão.

---

## **Execução**
Para rodar a aplicação, basta garantir que as dependências estejam instaladas:

```bash
pip install networkx matplotlib
