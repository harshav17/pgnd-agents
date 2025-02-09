import sys
from pathlib import Path

def setup_project_path():
    project_root = str(Path().absolute().parent)
    if project_root not in sys.path:
        sys.path.append(project_root)