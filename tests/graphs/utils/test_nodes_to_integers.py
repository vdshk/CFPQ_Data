import pytest

import cfpq_data

g1 = cfpq_data.graph_from_dataset("foaf", verbose=False)
g2 = cfpq_data.graph_from_dataset("core", verbose=False)


@pytest.mark.parametrize(
    "graph",
    [
        g1,
        g2,
    ],
)
def test_nodes_to_integers(graph):
    actual = list(cfpq_data.nodes_to_integers(graph, verbose=False).nodes())

    expected = list(range(graph.number_of_nodes()))

    assert actual == expected
