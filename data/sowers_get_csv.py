"""

This script downloads a CSV file containing Pokémon species, games, and regions from a URL and saves it as pokemon_all_generations.csv inside the fetched_data folder by:

Fetching a text file containing the ISO 8859-1 character set from the web.  
Saving the text file locally as geographical_characters.txt in the fetched_data folder.  
Logging each step of the process (fetching, writing, success, errors).  
Handling potential errors like missing URLs or failed requests. 

"""
#####################################
# Import Modules at the Top
#####################################
import sys
import os
import requests
import pathlib

# Making sure Python can find the utils_logger.py file in the root folder since the scripts are in their own folder.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "fetched_data"

#####################################
# Define Functions
#####################################

def fetch_csv_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch CSV data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the CSV file to fetch.

    Returns:
        None

    Example:
        fetch_csv_file("data", "data.csv", "https://example.com/data.csv")
    """
    if not url:
        logger.error("The URL provided is empty or was not found. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching CSV data from {url} is in progress...")
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: CSV file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_csv_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write CSV data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): CSV content as a string.

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing CSV data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        logger.info(f"SUCCESS: CSV data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing CSV data to {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching the CSV data.
    """
    csv_url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
    logger.info("Initiating CSV data fetch demonstration...")
    fetch_csv_file(fetched_folder_name, "pokemon_all_generations.csv", csv_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()