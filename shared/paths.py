from pathlib import Path

def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent.parent.parent

def get_data_dir() -> Path:
    """Returns data directory, creating it if it doesn't exist."""
    data_dir = get_project_root() / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir
