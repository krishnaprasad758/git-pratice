# transform.py

def transform_data(data):
    return [
        row for row in data
        if row.get("name")
    ]