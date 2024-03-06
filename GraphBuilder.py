import json
from graphviz import Digraph

# Function to read JSON input from a file
def read_json_input(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to add dependencies to the graph
def add_project_dependencies(graph, project_name, dependencies, projects_info, added_projects):
    for dep in dependencies:
        dep_id = f'{dep["Name"]} {dep["Version"]}'  # Unique identifier for each dependency
        if dep_id not in added_projects:
            graph.node(dep_id, label=f'{dep["Name"]}\n{dep["Version"]}')
            graph.edge(project_name, dep_id)
            added_projects.add(dep_id)
            # Check if this dependency is also a project and add its dependencies
            project_info_name = dep["Name"].split(".")[-1]
            if project_info_name in projects_info:
                add_project_dependencies(graph, dep_id, projects_info[project_info_name]["Dependencies"], projects_info, added_projects)

# Main function to create dependency graphs
def create_dependency_graphs(file_path, projects_to_draw):
    projects = read_json_input(file_path)
    projects_info = {project["ProjectName"]: project for project in projects}  # Mapping of project names to their info

    for project in projects:
        graph = Digraph(comment=project["ProjectName"])
        if project["ProjectName"] in projects_to_draw:
            graph.node(project["ProjectName"], label=project["ProjectName"], shape='box', style='filled', color='lightblue')
            add_project_dependencies(graph, project["ProjectName"], project["Dependencies"], projects_info, set([project["ProjectName"]]))

            # Save the graph as a PNG file named after the project
            file_name = f'Results/{project["ProjectName"].replace(".", "_").replace(" ", "_")}.png'
            graph.render(file_name, format='png', cleanup=True)

# Assuming the JSON input is saved in 'dependencies.json'
#create_dependency_graphs('dependencies_filtered.json')
