import os
import zipfile
import json
from bs4 import BeautifulSoup 

def clean_html_data(raw_content):
    """ Clean up HTML content within specified tags by using BeautifulSoup. """
    try:
        soup = BeautifulSoup(raw_content, 'html.parser')
        # Retrieve plain text from HTML with spaces separating elements
        return soup.get_text(separator=' ', strip=True)
    except Exception as error:
        return f"Error parsing HTML content: {str(error)}"

def find_and_clean_text(section_content):
    """ Locate the content within specific <TEXT>...</TEXT> tags. """
    open_tag = '<TEXT>'
    close_tag = '</TEXT>'
    try:
        open_pos = section_content.index(open_tag) + len(open_tag)
        close_pos = section_content.index(close_tag)
        html_section = section_content[open_pos:close_pos]
        return clean_html_data(html_section)
    except ValueError:
        return "Could not locate <TEXT> tags"

def consolidate_reports_to_json(zip_file_path, json_output_file):
    """ Consolidate and merge reports into a JSON file from the given zip archive. """
    with zipfile.ZipFile(zip_file_path, 'r') as archive:
        # Identify folders matching the target pattern
        all_dirs = [item for item in archive.namelist() if item.endswith('/')]
        relevant_dirs = [directory for directory in all_dirs if directory.startswith('AMZN/10-K/') and directory.count('/') == 3]
        collected_reports = {}

        # Extract the 'full-submission.txt' from each relevant directory
        for directory in relevant_dirs:
            submission_path = os.path.join(directory, 'full-submission.txt')
            if submission_path in archive.namelist():
                with archive.open(submission_path) as submission:
                    content = submission.read().decode('utf-8')
                    cleaned_content = find_and_clean_text(content)
                    directory_id = directory.strip('/')
                    collected_reports[directory_id] = cleaned_content

        # Write the consolidated reports into a JSON file
        with open(json_output_file, 'w') as output:
            json.dump(collected_reports, output, indent=4)

# Define the input and output paths for our task
zip_file_path = r'C:\Users\Shubh\Downloads\SEC-EDGAR_Analyis_App-main\SEC-EDGAR_Analyis_App-main\Data Integration\AMZN.zip'
json_output_file = 'AMZN.json'

# Run the consolidation process into the JSON file
consolidate_reports_to_json(zip_file_path, json_output_file)

# Read the JSON file and write it to a text file in a human-readable format
with open(json_output_file, 'r') as json_data:
    reports = json.load(json_data)

# Save the collected JSON data to a .txt file
with open('AMZN.txt', 'w') as text_output:
    json.dump(reports, text_output, indent=4)
