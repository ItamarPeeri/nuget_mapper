import json
import re

# Function to process lines and return project_info
def process_lines(lines):
    project_info = {
        "ProjectName": "",
        "Dependencies": []
    }
    current_section = None
    for line in lines:
        # Match the project name line
        if line.startswith("Project '"):
            project_info["ProjectName"] = line.split("'")[1].split("'")[0]
        # Determine if the line indicates a section change
        elif "Top-level Package" in line:
            current_section = "Top-level Package"
        elif "Transitive Package" in line:
            current_section = "Transitive Package"
        # Process package lines, filter by "wsc."
        elif line.strip().startswith(">"):
            parts = [part.strip() for part in re.split(r'\s{2,}', line.strip())]  # Splitting on whitespace, considering at least 2 spaces as a new column
            package_name = parts[0]
            package_name = package_name.split('> ')[1]
            if package_name.startswith("wsc."):
                resolved_version = parts[-1]
                package_info = {"Name": package_name, "Version": resolved_version, "Dependencies": []}
                # Assuming transitive dependencies are not detailed, hence not nested
                if current_section == "Top-level Package":
                    project_info["Dependencies"].append(package_info)

    return project_info

def convert_to_json(file_name, out_json_file_name):
    project_info_list = []

    with open(file_name, "r") as file:
        lines = file.readlines()
        project_lines = []
        for line in lines:
            if line.startswith("Project '") and project_lines:
                # Process the current project's lines and start a new project
                project_info_list.append(process_lines(project_lines))
                project_lines = [line]  # Start new project lines with the current line
            else:
                project_lines.append(line)
        # Don't forget to process the last project in the file
        if project_lines:
            project_info_list.append(process_lines(project_lines))

    # Write the list of project_infos to a JSON file
    with open(out_json_file_name, "w") as json_file:
        json.dump(project_info_list, json_file, indent=4)


# Initialize a list to hold all project infos
#project_info_list = []
#file_name = "packages_utf8.txt"
#out_json_file_name = 'dependencies_filtered.json'
#convert_to_json(file_name,out_json_file_name, project_info_list)
