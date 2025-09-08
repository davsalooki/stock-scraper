import yaml

from .utils import get_stock_id_to_name


def load_config() -> None:
    """Load configuration from YAML file."""
    CONFIG_FILE = "config/scraper.yaml"
    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)


CONFIG = load_config()

STOCK_ID_TO_NAME = get_stock_id_to_name()

STOCK_ID_LIST = STOCK_ID_TO_NAME.keys()
