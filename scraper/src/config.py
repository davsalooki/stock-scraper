import yaml


def load_config() -> None:
    """Load configuration from YAML file."""
    CONFIG_FILE = "config/scraper.yaml"
    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)

CONFIG = load_config()