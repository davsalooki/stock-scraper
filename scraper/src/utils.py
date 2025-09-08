import csv


def get_stock_id_to_name() -> dict[str, str]:
    with open("config/companies-list.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        return {row[0]: clean_stock_name(row[1]) for row in reader if row}


def clean_stock_name(name: str) -> str:
    """
    Cleans the stock name by removing the last word (usually the exchange code).

    There is a stock identifier at the end that needs to be removed.
    Example: "Universal Store Holdings Limited (ASX:UNI)" -> "Universal Store Holdings Limited"
    """
    return " ".join(name.split()[:-1])
