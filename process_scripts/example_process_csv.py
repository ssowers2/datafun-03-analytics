"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "example_data"
processed_folder_name: str = "example_processed"

#####################################
# Define Functions
#####################################

def analyze_ladder_score(file_path: pathlib.Path) -> dict:
    """Analyze the Ladder score column to calculate min, max, mean, and stdev."""
    try:
        # initialize an empty list to store the scores
        score_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    score = float(row["Ladder score"])  # Extract and convert to float
                    # append the score to the list
                    score_list.append(score)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min": min(score_list),
            "max": max(score_list),
            "mean": statistics.mean(score_list),
            "stdev": statistics.stdev(score_list) if len(score_list) > 1 else 0,
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Ladder score, and save the results."""
    input_file = pathlib.Path(fetched_folder_name, "2020_happiness.csv")
    output_file = pathlib.Path(processed_folder_name, "happiness_ladder_score_stats.txt")
    
    stats = analyze_ladder_score(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Ladder Score Statistics:\n")
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