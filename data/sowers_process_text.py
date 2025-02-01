"""
Process a text file to count occurrences of the word "CAPITAL LETTER" and save the result.

"""

#####################################
# Import Modules
#####################################
import sys
import os
import pathlib

# Making sure Python can find utils_logger.py in the root folder since the process_scripts are in their own folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "fetched_data"
processed_folder_name: str = "processed_data"

#####################################
# Define Functions
#####################################

def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
        with file_path.open('r') as file:
            content: str = file.read()
            return content.lower().count(word.lower())
    except Exception as e:
        logger.error(f"There was an error reading the text file: {e}")
        return 0

def process_text_file():
    """Read a text file, count occurrences of 'CAPITAL LETTER', and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "geographical_characters.txt")
    output_file = pathlib.Path(processed_folder_name, "capital_letters_word_count.txt")
    word_to_count: str = "CAPITAL LETTER"
    word_count: int = count_word_occurrences(input_file, word_to_count)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Occurrences of '{word_to_count}': {word_count}\n")
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")