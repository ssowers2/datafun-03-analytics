"""
Process a CSV file on pokemon_all_generations to analyze the Pokemon `Speed` column and save statistics.

"""

#####################################
# Import Modules
#####################################
import sys
import os
import pathlib
import csv
import statistics

# Making sure Python can find utils_logger.py in the root folder since the process_scripts are in their own folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "fetched_data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def analyze_Speed_speed(file_path: pathlib.Path) -> dict:
    """Analyze the 'speed' speed column to calculate min, max, mean, and stdev."""
    try:
        # initialize an empty list to store the speeds
        speed_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    speed = float(row["Speed"])  # Extract and convert to float
                    # append the speed to the list
                    speed_list.append(speed)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min": min(speed_list),
            "max": max(speed_list),
            "mean": statistics.mean(speed_list),
            "stdev": statistics.stdev(speed_list) if len(speed_list) > 1 else 0,
        }
        return stats
    except Exception as e:
        logger.error(f"There was an error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Speed, and save the results."""
    input_file = pathlib.Path(fetched_folder_name, "pokemon_all_generations.csv")
    output_file = pathlib.Path(processed_folder_name, "pokemon_speed_stats.txt")
    
    stats = analyze_Speed_speed(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Pokémon Speed Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
    
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")