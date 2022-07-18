from httpserver import app, csv_to_json
import json

def test_csv_to_json():
    test_csv_data = "time,meterusage\n2019-01-01 07:00:00,55.09\n2019-01-06 11:45:15,91.28\n"

    test_json_data = json.dumps([
        {
        "time": "2019-01-01 07:00:00", "meterusage": "55.09"
        },
        {
        "time": "2019-01-06 11:45:15", "meterusage": "91.28"
        },
    ])

    result = csv_to_json(test_csv_data)
    assert(csv_to_json(test_csv_data) == test_json_data)
    print("csv_to_json test passed")

