import csv

def get_ticker_list() -> list[str]:
    with open("config/companies-list.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        return [row[0] for row in reader if row]
