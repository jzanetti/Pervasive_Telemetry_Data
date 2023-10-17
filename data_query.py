import requests

api_key = "3Y0eC7WevYe1r7gUYPlT4w"
headers = {
    "Authorization": f"Bearer {api_key}",
}

telemetry_url = "https://www.telemetry.net.au"


query_parameters = {
    "start_time": "2023-10-01T00:00:00Z",
    "end_time": "2023-10-02T00:00:00Z",
    # "sensor_id": "sensor_123",
}

response = requests.get(telemetry_url, params=query_parameters, headers=headers)

data = response.json()

print(response)
print(data)
