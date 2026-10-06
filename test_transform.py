from transform import transform_data


def test_transform_removes_null_values():

    data = [
        {
            "name": "Krish",
            "email": "krish@example.com",
            "age": "25"
        },
        {
            "name": "",
            "email": "test@example.com",
            "age": "24"
        }
    ]

    result = transform_data(data)

    assert len(result) == 1
    assert result[0]["name"] == "Krish"