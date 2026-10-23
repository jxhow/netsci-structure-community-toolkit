from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt


def degree_distribution(G):
    counts = Counter(dict(G.degree()).values())
    return {k: counts[k] / len(G) for k in sorted(counts)}


def all_shortest_from(G, node):
    distances = {u: -1 for u in G}
    distances.update(nx.single_source_shortest_path_length(G, node))
    return distances


def closeness_centrality_from_scratch(G):
    centrality = {}
    for node in G:
        distances = nx.single_source_shortest_path_length(G, node)
        total = sum(distances.values())
        centrality[node] = (len(G) - 1) / total if total else 0
    return centrality


def degree_preserving_randomization(G):
    randomized = G.copy()
    nx.double_edge_swap(randomized, nswap=10 * G.number_of_edges(),
                        max_tries=100 * G.number_of_edges(), seed=42)
    return randomized


def configuration_model_from_degree_sequence(degrees):
    return nx.configuration_model(degrees)


def calculate_modularity(G, partition):
    communities = {}
    for node, community in partition.items():
        communities.setdefault(community, set()).add(node)
    return nx.community.modularity(G, list(communities.values()))


def louvain_partition(G):
    communities = nx.community.louvain_communities(G, seed=42)
    return {node: i for i, group in enumerate(communities) for node in group}


def plot_communities(G, partition, pos):
    nx.draw(G, pos=pos, node_color=[partition[node] for node in G],
            cmap=plt.cm.tab20, node_size=5, width=0.1)
    plt.show()
