from graphviz import Digraph
from gym_factory.objects import *


def representation(object, rankdir):
    rep = ""
    if isinstance(object, Processor):
        if rankdir == "TB":
            rep = r'{} | [ {} | {} ] | [ {} | {} ]'.format(object.name, "Setup Time", "Process Time", object.setup_time, object.process_time)
        elif rankdir == "LR":
            rep = r'{} | [ {} | {} ] | [ {} | {} ]'.format(object.name, "Setup Time", object.setup_time, "Process Time", object.process_time)
    elif isinstance(object, Source):
        if rankdir == "TB":
            rep = r'{} | [ {} | {} ] | [ {} | {} ]'.format(object.name, "Setup Time", "Process Time", "--", "--")
        elif rankdir == "LR":
            rep = r'{} | [ {} | {} ] | [ {} | {} ]'.format(object.name, "Setup Time", "--", "Process Time", "--")
    elif isinstance(object, Sink):
        if rankdir == "TB":
            rep = r'{} | [ {} | {} ] | [ {} | {} ]'.format(object.name, "Setup Time", "Process Time", "--", "--")
        elif rankdir == "LR":
            rep = r'{} | [ {} | {} ] | [ {} | {} ]'.format(object.name, "Setup Time", "--", "Process Time", "--")

    return rep.replace("[", "{").replace("]", "}")


def plot_model(model, filename):
    s = Digraph(name=model.name, filename=filename, node_attr={'shape': 'Mrecord'})
    s.graph_attr['rankdir'] = 'TB'
    s.attr(label="{}\n{}".format(model.name, model.description))

    # Create node of objects
    for obj in model.objects:
        s.node(obj.name.lower(), representation(obj, s.graph_attr['rankdir']))

    # Create edges between nodes
    for obj in model.objects:
        print(obj.name)
        if isinstance(obj, Source) or isinstance(obj, type(None)):
            continue
        print(obj.input)
        s.edge(obj.input.name.lower(), obj.name.lower())

    s.view()