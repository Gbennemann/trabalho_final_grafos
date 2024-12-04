import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations


# Classe Grafo
class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def add_vertex(self, vertice):
        if vertice in self.grafo.nodes:
            raise ValueError(f"O vértice '{vertice}' já existe no grafo.")
        self.grafo.add_node(vertice)

    def add_edge(self, vertice1, vertice2, peso):
        if not (vertice1 in self.grafo.nodes and vertice2 in self.grafo.nodes):
            raise ValueError("Ambos os vértices devem existir no grafo.")
        if self.grafo.has_edge(vertice1, vertice2):
            raise ValueError(f"Aresta entre '{vertice1}' e '{vertice2}' já existe.")
        if peso <= 0:
            raise ValueError("O peso da aresta deve ser um número positivo.")
        self.grafo.add_edge(vertice1, vertice2, weight=peso)

    def mostrar_grafo(self):
        if self.grafo.number_of_nodes() == 0:
            raise ValueError("O grafo está vazio. Adicione vértices e arestas antes de visualizá-lo.")
        pos = nx.spring_layout(self.grafo)
        nx.draw(self.grafo, pos, with_labels=True, node_color="skyblue", node_size=500)
        labels = nx.get_edge_attributes(self.grafo, "weight")
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        plt.show()

    def menor_caminho(self, inicio, fim):
        if inicio not in self.grafo.nodes:
            raise ValueError(f"O vértice de origem '{inicio}' não está no grafo.")
        if fim not in self.grafo.nodes:
            raise ValueError(f"O vértice de destino '{fim}' não está no grafo.")
        return nx.shortest_path(self.grafo, source=inicio, target=fim, weight='weight')

    def euleriano(self):
        if nx.is_eulerian(self.grafo):
            return list(nx.eulerian_circuit(self.grafo))
        return None

    def hamiltoniano(self):
        vertices = list(self.grafo.nodes)
        caminhos = permutations(vertices)
        melhor_custo = float("inf")
        melhor_caminho = None
        for caminho in caminhos:
            custo = 0
            valido = True
            for i in range(len(caminho) - 1):
                if self.grafo.has_edge(caminho[i], caminho[i + 1]):
                    custo += self.grafo[caminho[i]][caminho[i + 1]]["weight"]
                else:
                    valido = False
                    break
            if valido and custo < melhor_custo:
                melhor_custo = custo
                melhor_caminho = caminho
        return melhor_caminho, melhor_custo

    def arvore_minima(self):
        if self.grafo.number_of_edges() == 0:
            raise ValueError("O grafo não possui arestas para calcular a árvore de custo mínimo.")
        return nx.minimum_spanning_tree(self.grafo)


# Menu Interativo
def menu():
    g = Grafo()
    while True:
        print("\nMenu:")
        print("1. Adicionar vértice")
        print("2. Adicionar aresta")
        print("3. Mostrar grafo")
        print("4. Menor caminho")
        print("5. Problema Euleriano")
        print("6. Problema Hamiltoniano")
        print("7. Árvore de custo mínimo")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                vertice = input("Digite o nome do vértice: ").strip()
                if not vertice:
                    print("O nome do vértice não pode estar vazio.")
                else:
                    g.add_vertex(vertice)
                    print(f"Vértice '{vertice}' adicionado com sucesso.")

            elif opcao == "2":
                if len(g.grafo.nodes) < 2:
                    print("É necessário ter pelo menos dois vértices para adicionar uma aresta.")
                else:
                    v1 = input("Digite o primeiro vértice: ").strip()
                    v2 = input("Digite o segundo vértice: ").strip()
                    peso = input("Digite o peso da aresta: ")

                    try:
                        peso = float(peso)
                        g.add_edge(v1, v2, peso)
                        print(f"Aresta entre '{v1}' e '{v2}' com peso {peso} adicionada com sucesso.")
                    except ValueError:
                        print("Peso inválido. Digite um número válido.")
                    except Exception as e:
                        print(e)

            elif opcao == "3":
                g.mostrar_grafo()

            elif opcao == "4":
                if len(g.grafo.nodes) < 2:
                    print("O grafo precisa ter pelo menos dois vértices para calcular o menor caminho.")
                else:
                    print(f"Vértices disponíveis: {list(g.grafo.nodes)}")
                    inicio = input("Vértice inicial: ").strip()
                    fim = input("Vértice final: ").strip()
                    try:
                        print("Menor caminho:", g.menor_caminho(inicio, fim))
                    except ValueError as e:
                        print(e)

            elif opcao == "5":
                resultado = g.euleriano()
                if resultado:
                    print("Caminho Euleriano encontrado:", resultado)
                else:
                    print("O grafo não é Euleriano.")

            elif opcao == "6":
                caminho, custo = g.hamiltoniano()
                if caminho:
                    print(f"Caminho Hamiltoniano encontrado: {caminho} com custo {custo}")
                else:
                    print("Não foi possível encontrar um caminho Hamiltoniano.")

            elif opcao == "7":
                mst = g.arvore_minima()
                print("Árvore de custo mínimo encontrada:")
                for edge in mst.edges(data=True):
                    print(edge)
                nx.draw(mst, with_labels=True, node_color="lightgreen", node_size=500)
                plt.show()

            elif opcao == "8":
                print("Saindo...")
                break

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")


# Executa o menu
if __name__ == "__main__":
    menu()
