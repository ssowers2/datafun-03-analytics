"""
This script fetches a text file containing the ISO 8859-1 character set from a website
and saves it as `geographical_characters.txt` in the fetched_data folder by:

Defining a URL pointing to the text file containing character descriptions.
Fetching the text file using requests.get(), ensuring the URL is valid.
Handling errors in case of network issues or invalid responses.
Writing the downloaded text to a local file inside the fetched_data directory.
Logging progress and errors using utils_logger.py for debugging.

"""

#####################################
# Import Modules at the Top
#####################################
import sys
import os
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

def fetch_txt_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch text data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the text file to fetch.

    Returns:
        None

    Example:
        fetch_txt_file("data", "geographical_characters.txt", "https://www.w3.org/TR/2003/REC-PNG-20031110/iso_8859-1.txt")
    """
    if not url:
        logger.error("The URL provided is empty or was not found. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching text data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
        logger.info(f"The text file was fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_txt_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write text data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): Text content to write to the file.

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        logger.info(f"The data was written to {file_path}")
    except IOError as io_err:
        logger.error(f"There was an error writing to file {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching text data.
    """
    txt_url = "https://www.w3.org/TR/2003/REC-PNG-20031110/iso_8859-1.txt"
    logger.info("Starting text fetch demonstration...")
    fetch_txt_file(fetched_folder_name, "geographical_characters.txt", txt_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()