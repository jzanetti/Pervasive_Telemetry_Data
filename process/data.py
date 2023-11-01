from datetime import datetime
from os import environ

from pandas import DataFrame
from requests import get as requests_get

SITE_TEMPLATE = "https://www.telemetry.net.au/api/v1/sites/{site_id}/samples"


def query_data(
    site_id: str,
    api_key: str,
    start_datetime: datetime,
    end_datetime: datetime,
    limit: int or None,
) -> dict:
    """Query the data from a site

    Args:
        site_id (str): Site ID, e.g., 12345
        api_key (str): The API key to be used
        start_datetime (datetime): Start datetime, e.g., 2023-09-18T08:20:00Z
        end_datetime (datetime): End datetime, e.g., 2023-10-18T08:20:00Z
        limit (int): The number of samples
    """
    url = SITE_TEMPLATE.format(site_id=site_id)
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key,
    }

    # Define the query parameters
    params = {
        "startTime": start_datetime.strftime("%Y%m%dT%H%M%S"),
        "endTime": end_datetime.strftime("%Y%m%dT%H%M%S"),
        "limit": limit,
    }

    # Filter out unused parameters
    params = {key: value for key, value in params.items() if value is not None}

    # Send the GET request
    response = requests_get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
    else:
        raise Exception(f"Error: {response.status_code}")

    return data


def create_table(data: dict, site_name: str) -> DataFrame:
    sampleDesc = data["sampleDesc"]
    sampleDesc_name = {k: v["name"] for k, v in sampleDesc.items()}
    sampleDesc_unit = {k: v["units"] for k, v in sampleDesc.items()}
    # sampleDesc_df = DataFrame.from_dict(sampleDesc, orient="index")

    combined_dict = {
        key: f"{sampleDesc_name[key]} {sampleDesc_unit[key]}".rstrip()
        for key in sampleDesc_name
        if key in sampleDesc_unit
    }

    samples_df = DataFrame(data["samples"])
    samples_df.rename(columns=combined_dict, inplace=True)

    samples_df["site"] = site_name

    return samples_df
