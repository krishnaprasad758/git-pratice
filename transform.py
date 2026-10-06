def transform_data(data):
    return [
        row for row in data
        if row.get("name") and row.get("email")
    ]