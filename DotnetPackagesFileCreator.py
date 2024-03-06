import subprocess
import os


def run_dotnet_packages(project_path, folders):

    # Path to the combined packages.txt file, located in the same directory as this Python script
    script_location = os.path.dirname(os.path.realpath(__file__))
    combined_packages_file_path = os.path.join(script_location, 'packages.txt')

    # Open the combined packages.txt file in write mode to ensure it's empty before starting
    with open(combined_packages_file_path, 'w') as combined_file:
        combined_file.write("")  # Clear existing contents

    # Iterate over each folder and run the dotnet command
    for folder in folders:
        full_folder_path = f'{project_path}\\{folder}'
        print(f"Processing {full_folder_path}...")
        # Ensure the directory exists
        if not os.path.isdir(full_folder_path):
            print(f"Directory does not exist: {full_folder_path}")
            continue

        try:
            # Execute the dotnet list package command
            # Output is directly appended to the combined packages.txt file
            subprocess.run(f"dotnet list {full_folder_path} package --include-transitive >> {combined_packages_file_path}",
                           shell=True, check=True, cwd=full_folder_path)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while processing {full_folder_path}: {e}")

    print(f"Aggregated package list written to {combined_packages_file_path}")