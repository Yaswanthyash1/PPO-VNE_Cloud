import networkx as nx

def plot_graph(graph, title="Graph"):
    import matplotlib.pyplot as plt
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)
    plt.title(title)
    plt.show()