# Network Science Toolkit

A small collection of eight reusable Python functions from NETS7052 coursework (through Class 11). The toolkit covers network structure, paths, centrality, randomization, configuration models, community detection, modularity, and visualization. It can be used with any suitable NetworkX network, including networks whose nodes represent geographic areas.

## Requirements

- Python 3
- `networkx`
- `matplotlib`

Clone and install the package with pip:

```bash
git clone https://github.com/jxhow/netsci-structure-community-toolkit.git
cd netsci-structure-community-toolkit
python -m pip install .
```

Then import the functions from any working directory, for example:

```python
from network_toolkit import degree_distribution, louvain_partition
```

## Functions

### `degree_distribution(G)`

Returns the degree distribution of a NetworkX graph `G` as `{degree: fraction_of_nodes}`. Includes degree zero if there are isolated nodes. Degrees are returned in ascending order.

### `all_shortest_from(G, node)`

Returns `{node_id: shortest_path_distance}` from the specified source `node` to each node in `G`. It uses unweighted shortest paths. Unreachable nodes have distance `-1`.

### `closeness_centrality_from_scratch(G)`

Returns `{node_id: centrality_value}`. For each node, it divides `len(G) - 1` by the sum of the shortest-path distances to reachable nodes, returning zero if that sum is zero. This particular implementation does **not** apply NetworkX's usual disconnected-graph correction, so its values on disconnected graphs should not be interpreted as standard normalized closeness.

### `degree_preserving_randomization(G)`

Returns a copy of `G` randomized through NetworkX double-edge swaps, using `10 * G.number_of_edges()` swaps and random seed `42`. The original graph is unchanged, and each node's degree is preserved. Connectivity is not guaranteed to be preserved. The procedure may raise an error if valid swaps cannot be completed.

### `configuration_model_from_degree_sequence(degrees)`

Returns a NetworkX configuration-model graph from an iterable of nonnegative integer degrees. The sequence must have an even sum. The result is a multigraph, so self-loops and parallel edges may occur.

### `calculate_modularity(G, partition)`

Returns the modularity score of a partition of `G`, using NetworkX's modularity function. `partition` must be a dictionary in the form `{node_id: community_id}`, covering the graph's nodes.

### `louvain_partition(G)`

Detects communities with NetworkX's Louvain algorithm (seed `42`). Returns the partition as `{node_id: community_id}`. The numeric community labels are identifiers, not rankings.

### `plot_communities(G, partition, pos)`

Draws the NetworkX graph `G` with nodes colored according to `partition` (a `{node_id: community_id}` dictionary). `pos` is a dictionary of node positions, such as the result of `nx.spring_layout(G)` or known geographic coordinates. It displays the plot with Matplotlib and does not return a partition.

## Example

```python
import networkx as nx
from network_toolkit import louvain_partition, calculate_modularity, plot_communities

G = nx.karate_club_graph()
partition = louvain_partition(G)
print(calculate_modularity(G, partition))
plot_communities(G, partition, nx.spring_layout(G, seed=42))
```

For geographic networks, `pos` can be the map coordinates of nodes; no separate geographic detection algorithm is required to use these functions.
