import os

from ConfigParser import parse_config
from DotnetDependencyParser import convert_to_json
from DotnetPackagesFileCreator import run_dotnet_packages
from GraphBuilder import create_dependency_graphs
from Ut8Convertor import convert_file_to_utf8

config_file_name = 'config.txt'

config_parameters = parse_config(config_file_name)

# Access the parsed parameters
project_path = config_parameters['project_path']
general_sln_dirs = config_parameters['general_sln_dirs']
team_sln_dirs = config_parameters['team_sln_dirs']
projects_to_draw = config_parameters['projects_to_draw']

script_dir = os.path.dirname(os.path.abspath(__file__))
original_file_path = os.path.join(script_dir, 'packages.txt')
new_file_path = os.path.join(script_dir, 'packages_utf8.txt')
dependencies_json_path = os.path.join(script_dir, 'dependencies_filtered.json')

#projects_to_draw = ['ImagesCommon', 'EncodeCommon', 'FrameAccurateCommon',
#                     'MediaAssetsCommon', 'MultipleAudioChannels',
#                     'AssetUtils', 'VideoEditorClient', 'SegmentCreator',
#                     'VideoServerCommon', 'StorageUtils', 'ZoomInJobs']

run_dotnet_packages(project_path, general_sln_dirs + team_sln_dirs)
convert_file_to_utf8(original_file_path, new_file_path)
convert_to_json(new_file_path, dependencies_json_path)
create_dependency_graphs(dependencies_json_path, projects_to_draw)
