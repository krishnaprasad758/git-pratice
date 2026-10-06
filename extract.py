# extract.py
import csv

def extract_data(filename):
    with open(filename, "r") as file:
        data = list(csv.DictReader(file))

    print(f"Row count: {len(data)}")
    return data