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

O projeto foi uma aplicação prática dos conceitos estudados durante o curso de **Teoria dos Grafos**, permitindo resolver problemas clássicos de grafos como o **problema do carteiro chinês**, o **problema do caixeiro viajante**, o **menor caminho entre dois vértices**, a **árvore expansiva de custo mínimo** e a **coloração de grafos**. A implementação dos algoritmos estudados, como **Dijkstra**, **Fleury**, **Prim** e **Kruskal**, 
me trouxe uma compreensão mais "real" de como os grafos podem ser manipulados computacionalmente.

A aplicação serviu como uma excelente ferramenta para eu entender melhor a teoria por trás dos algoritmos e também para visualizar como esses problemas são resolvidos na prática. 
Com o uso de bibliotecas como a **NetworkX** e **Matplotlib**, foi possível criar não apenas a lógica de resolução dos problemas, mas também uma interface visual para facilitar a compreensão de quem poderá utilizar esse código no futuro.

---

## **Execução**

Para rodar a aplicação, você precisará do Python instalado em seu ambiente, assim como da biblioteca **NetworkX**. Siga as instruções abaixo para garantir que o ambiente esteja pronto para a execução.

### Pré-requisitos

1. **Python** (versão 3.x): Se ainda não tiver o Python instalado, faça o download e a instalação a partir do [site oficial do Python](https://www.python.org/downloads/).

2. **NetworkX**: Biblioteca necessária para manipulação de grafos. Caso ainda não tenha o **NetworkX** instalado, instale-o com o seguinte comando no terminal:

    ```bash
    pip install networkx
    ```

## Como Executar

Siga os passos abaixo para rodar a aplicação.

### Passo 1: Baixar o código

Primeiro, faça o download ou clone o repositório contendo o código da aplicação para seu ambiente local.

### Passo 2: Navegar até o diretório do código

No terminal, navegue até o diretório onde o código foi baixado. Utilize o seguinte comando para acessar o diretório do projeto:

```bash
cd /caminho/para/o/diretorio
