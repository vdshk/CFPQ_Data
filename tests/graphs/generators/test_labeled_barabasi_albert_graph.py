import random

import pytest

import cfpq_data

seed = 42
random.seed(seed)

g1 = cfpq_data.labeled_barabasi_albert_graph(100, 1, seed=seed, verbose=False)
g2 = cfpq_data.labeled_barabasi_albert_graph(100, 3, seed=seed, verbose=False)


@pytest.mark.parametrize(
    "graph,expected_nodes,expected_edges", [(g1, 100, 198), (g2, 100, 582)]
)
def test_labeled_barabasi_albert_graph(graph, expected_nodes, expected_edges):
    assert (
        graph.number_of_nodes() == expected_nodes
        and graph.number_of_edges() == expected_edges
    )
