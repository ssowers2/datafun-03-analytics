# datafun-03-analytics
This project demonstrates how to fetch and process various types of data (Excel, JSON, text, and CSV) using Python.  
The repository includes:  Four example fetchers: Scripts to retrieve data from the web. Four example processors: Scripts to analyze and process the fetched data.
Project Workflow

##Steps I took to initialize this project
1. Created a new public repository from scratch
2. Used Git to clone the new repository to my local machine
3. Added files such as .gitignore and requirements.txt
4. Created a Local Python Virtual Environment for my project
5. Installed desired dependencies and documented them in my requirements.txt file
6. Used Git to add, commit, and push commands to add new files to GitHub

##Systems Used
1. Windows 11
2. Windows PowerShell

## Project Structure
datafun-03-analytics/
│-- .venv/                 # Python virtual environment (ignored by Git)
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── share/
│   ├── pyvenv.cfg
│
│-- fetch_scripts/          # Scripts for fetching data
│   ├── example_get_csv.py
│   ├── example_get_excel.py
│   ├── example_get_json.py
│   ├── example_get_text.py
│
│-- process_scripts/        # Scripts for processing data
│   ├── example_process_csv.py
│   ├── example_process_excel.py
│   ├── example_process_json.py
│   ├── example_process_text.py
│
│-- .gitignore              # Git ignore file
│-- README.md               # Project documentation
│-- requirements.txt        # Dependencies for the project
│-- utils_logger.py         # Logging utility

##Helpful Links
https://github.com/denisecase/pro-analytics-01/tree/main/02-project-initialization
https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/REPEATABLE-WORKFLOW.md

FETCHERS
Pokémon CSV Fetcher:
Downloads a CSV file containing Pokémon species, games, and regions from a URL.
Saved As: fetched_data/pokemon_all_generations.csv
Execution Command: py data/sowers_get_csv.pyy

Sales Data Excel Fetcher:
Fetches an Excel file containing sales data from a website.
Saved As: fetched_data/adventure_works_sales.xlsx
Execution Command: py data/sowers_get_excel.py

People JSON Fetcher:
Fetches a JSON file containing demographic information of individuals.
Saved As: fetched_data/people.json
Execution Command: py data/sowers_get_json.py

Geographical Charactors Text Fetcher:
Fetches a text file listing ISO 8859-1 characters and their descriptions.
Saved As: fetched_data/geographical_characters.txt
Execution Command: py data/sowers_get_text.py

PROCESSORS
Pokémon CSV Processor:
Analyzes the Speed column in pokemon_all_generations.csv, computing statistics like min, max, mean, and standard deviation.
Processed Output: data_processed/pokemon_speed_stats.txt
Execution Command: py processed/sowers_process_csv.py

Sales Data Excel Processor:
Reads adventure_works_sales.xlsx and counts occurrences of the phrase "United States" in column C.
Processed Output: data_processed/adventure_works_usa_count.txt
Execution Command: py processed/sowers_process_excel.py

People JSON Processor:
Reads people.json and counts the number of male and female individuals.
Processed Output: data_processed/people_by_gender.txt
Execution Command: py processed/sowers_process_json.py

Geographical Characters ISO 8859-1 Text Processor:
Reads geographical_characters.txt and counts occurrences of the phrase "CAPITAL LETTER".
Processed Output: data_processed/capital_letters_word_count.txt
Execution Command: py processed/sowers_process_text.py