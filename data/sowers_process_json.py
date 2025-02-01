"""
Process a JSON file to count the number of male and female people and save the result.

JSON file is in the format where it is a list of people with keys:"firstName", "lastName"
"gender", "age", and "number"

{
    "people": [
        {
            "firstName": "Joe",
            "lastName": "Jackson",
            "gender": "male",
            "age": 28,
            "number": "7349282382"
        },
        {
            "firstName": "James",
            "lastName": "Smith",
            "gender": "male",
            "age": 32,
            "number": "5678568567"
        },
        {
            "firstName": "Emily",
            "lastName": "Jones",
            "gender": "female",
            "age": 24,
            "number": "456754675"
        }
    ]
}

"""

#####################################
# Import Modules
#####################################
import sys
import os
import pathlib
import json

# Making sure Python can find utils_logger.py in the root folder since the process_scripts are in their own folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "fetched_data"
processed_folder_name = "processed_data"

#####################################
# Define Functions
#####################################

def count_people_by_gender(file_path: pathlib.Path) -> dict:
    """Count the number of male versus female people from a JSON file."""
    try:
        with file_path.open('r', encoding='utf-8') as file:
            # Use the json module load() function 
            # to read data file into a Python dictionary
            people_dictionary = json.load(file)  
            # initialize an empty dictionary to store the gender counts
            gender_counts_dictionary = {}
            # people_list is a list of dictionaries in the JSON file
            people_list: list = people_dictionary.get("people", [])
            for people_dictionary in people_list:  
                gender = people_dictionary.get("gender", "Unknown")
                gender_counts_dictionary[gender] = gender_counts_dictionary.get(gender, 0) + 1
            return gender_counts_dictionary
    except Exception as e:
        logger.error(f"There was an error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count people by gender and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, "people.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "people_by_gender.txt")
    
    gender_counts = count_people_by_gender(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("People By Gender:\n")
        for gender, count in gender_counts.items():
            file.write(f"{gender}: {count}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")