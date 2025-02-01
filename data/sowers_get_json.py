"""
This script fetches JSON data from a web URL and saves it as people.json in a folder called fetched_data by: 

Importing needed modules (requests, json, pathlib, etc.).
Defining a function fetch_json_file() to download the JSON file and save it locally.
Handling errors (e.g., HTTP request failures).
Logging each step to track progress.
Executing main function when the script runs.

"""
#####################################
# Import Modules at the Top
#####################################
import sys
import os
import json
import pathlib
import requests

# Making sure Python can find utils_logger.py in the root folder since the fetch_scripts are in their own folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "fetched_data"

#####################################
# Define Functions
#####################################

def fetch_json_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch JSON data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the JSON file to fetch.

    Returns:
        None

    Example:
        fetch_json_file("data", "data.json", "https://example.com/data.json")
    """
    if not url:
        logger.error("The URL provided is empty or was not found. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching JSON data from {url} in progress...")
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
        logger.info(f"A JSON file was fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_json_file(folder_name: str, filename: str, json_data: dict) -> None:
    """
    Write JSON data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        json_data (dict): JSON data to write to the file.

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing JSON data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            json.dump(json_data, file, indent=4)
        logger.info(f"JSON data was written to {file_path}")
    except IOError as io_err:
        logger.error(f"There was an error writing JSON data to {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching JSON data.
    """
    json_url = "https://filesamples.com/samples/code/json/sample4.json"
    logger.info("Starting JSON fetch demonstration...")
    fetch_json_file(fetched_folder_name, "people.json", json_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()