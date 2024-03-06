import json
from graphviz import Digraph

def add_dependencies_to_graph(graph, dependencies, parent_node=None):
    for dependency in dependencies:
        dep_name = f'{dependency["Name"]} {dependency["Version"]}'
        graph.node(dep_name)
        if parent_node:
            graph.edge(parent_node, dep_name)
        # Since dependencies are only filled at the project level, no recursive call is needed here

def create_dependency_graph(json_file):
    with open(json_file, 'r') as file:
        projects = json.load(file)

    #graph = Digraph(comment="Projects Dependencies")

    for project in projects:
        graph = Digraph(comment="Projects Dependencies")

        project_name = project["ProjectName"]
        # Create a node for the project itself
        graph.node(project_name, project_name, shape='box', style='filled', color='lightgrey')
        # If there are dependencies, add them
        if project["Dependencies"]:
            add_dependencies_to_graph(graph, project["Dependencies"], parent_node=project_name)
        else:
            # Even if there are no dependencies, we ensure the project is displayed
            graph.node(project_name)

        graph.render('Results/' + project_name + '_dependency_graph', format='png', cleanup=True)

    #graph.render('multi_project_dependency_graph', format='png', cleanup=True)

# Replace 'dependencies_filtered.json' with the path to your JSON file
create_dependency_graph('dependencies_filtered.json')
