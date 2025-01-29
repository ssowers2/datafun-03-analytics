# datafun-03-analytics
This project demonstrates how to fetch and process various types of data (Excel, JSON, text, and CSV) using Python.  
The repository includes:  Four example fetchers: Scripts to retrieve data from the web. Four example processors: Scripts to analyze and process the fetched data.
Project Workflow

Step 1. Set Up Your Project
Create a GitHub repo with default README.md (you'll need to manually add these example files).
Clone your new repo down to your machine.
Open the folder in VS Code.
Add a .gitignore file.
Install the required packages - see requirements.txt.
Full disclosure: We teach building repos from scratch because we assume students want to learn to create their own novel projects. However, if you want to get a local copy of this repo down to your machine, you can click the "Use this template" green button to copy it all into your account.

Step 2. Run the Examples
If you started with your own repo, copy the files from this GitHub as needed. If you cloned the template, you'll have the example files already.

Read, review, and run each example script. Open a terminal in the root project folder and run the appropriate command for your operating system. For example, these generally work on Windows. Adjust the commands to work for your machine, e.g. use python3 if Mac/Linux.

py fetch_scripts/example_get_csv.py
py fetch_scripts/example_get_excel.py
py fetch_scripts/example_get_json.py
py fetch_scripts/example_get_text.py

py process_scripts/example_process_csv.py
py process_scripts/example_process_excel.py
py process_scripts/example_process_json.py
py process_scripts/example_process_text.py
TODO: Replace the example commands with the actual commands used on your machine. Ensure all example scripts run without errors before proceeding.

Step 3. Create and Run Your Data Fetchers
Find data files on the web for each type (CSV, Excel, JSON, and text).
Create your own Python script to fetch each type of data and save it in a folder named data.
Name your scripts:
yourname_get_csv.py
yourname_get_excel.py
yourname_get_json.py
yourname_get_text.py
Implement your data-processing logic in small steps:
Fetch data for one file type.
Test, verify, and Git add-commit-push.
Step 4. Create and Run Your Data Processors
Determine a simple metric from each of your data files.
Create your own Python script to read the data, process it, and save it in a folder named data_processed.
Name your scripts:
yourname_process_csv.py
yourname_process_excel.py
yourname_process_json.py
yourname_process_text.py
Work incrementally, using git add-commit-push after each bit of progress.
Step 5. Update README.md to Describe Your Work
In your README.md, list each of your fetchers with a short description.
In your README.md, list each of your processors with a short description of what it does.
Include the execution commands to run your fetchers and processors.
Helpful Documentation
If you're unsure about any of the setup steps or tools, consult these resources:

requests library documentation
GitHub: Create and Clone a Repo
Set Up a Virtual Environment
Create a .gitignore File
Using Git: Add-Commit-Push
Tips
Use descriptive filenames for the data you fetch - and proper file extensions.
Work incrementally—verify each small step works before moving to the next.
The examples are required reading - use them to learn and understand first.
Test each script carefully before proceeding.
Use meaningful commit messages when pushing to GitHub to document your progress.
Review Commit History
Once your project is complete, review your commit history in GitHub under the Commits tab. Ensure your commit messages are clear and professional.

Finalize GitHub
Make sure the following requirements have been met:

 You have committed a useful .gitignore file.
 You have committed a useful logs/project_log.log file.
 All example scripts executed successfully.
 Four fetcher scripts created and executed.
 Four processor scripts created and functional.
 README.md includes explanations for fetchers and processors with commands for execution.
 Each Python file contains a docstring with its purpose and input/output details.
