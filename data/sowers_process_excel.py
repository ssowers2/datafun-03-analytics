"""
Process an Excel file to count occurrences of a specific word in a column.

"""
#####################################
# Import Modules
#####################################
import sys
import os
import pathlib
import openpyxl

# Making sure Python can find utils_logger.py in the root folder since the process_scripts are in their own folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "fetched_data"
processed_folder_name = "data_processed"

#####################################
# Define Functions
#####################################

def count_word_in_column(file_path: pathlib.Path, column_letter: str, word: str) -> int:
    """Count the occurrences of a specific word in a given column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        count = 0
        for cell in sheet[column_letter]:
            if cell.value and isinstance(cell.value, str):
                count += cell.value.lower().count(word.lower())
        return count
    except Exception as e:
        logger.error(f"There was an error reading Excel file: {e}")
        return 0

def process_excel_file():
    """Read an Excel file, count occurrences of a specific word in a specific column, and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "adventure_works_sales.xlsx")
    output_file = pathlib.Path(processed_folder_name, "adventure_works_usa_count.txt")
    column_to_check = "C"
    word_to_count = "United States"
    word_count = count_word_in_column(input_file, column_to_check, word_to_count)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Occurrences of '{word_to_count}' in column {column_to_check}: {word_count}\n")
    logger.info(f"Processed Excel file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")