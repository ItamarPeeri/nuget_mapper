-------------
Installations:
-------------
install GraphViz using this link
https://graphviz.org/download/
(graphviz-10.0.1 (64-bit) EXE installer [sha256])

make sure during installation to add it to system Path
after added check it is ok using the following cmd:
	dot -V
if version is returned you are good to go

------
Config
------
open the config.txt file and set the following:
project_path -> your ZoomInCloud solution path
general_sln_dirs -> directories you want to add to your mapping - commons and utils are the main directories where most nugets are. feel free to add more
team_sln_dirs -> your teams sln directories
projects_to_draw -> name of the projects you want to draw (csproj name)

-------
execute
-------
open a powershell/cmd file
simply run main.exe

-------
Results
-------
images will be generated in "Results" folder where your application runs from