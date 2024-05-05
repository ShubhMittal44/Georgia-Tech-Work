# Import necessary libraries
from sec_edgar_downloader import Downloader
import shutil

# Initialize a downloader instance
# Replace with a suitable directory path for your local environment
dl = Downloader("Shubh", "sm3674@g.rit.edu")

# Get all 10-K filings for Amazon (ticker: AMZN) between Jan 1, 1995, and Dec 31, 2023
dl.get("10-K", "AMZN", after="1994-12-31", before="2024-01-01")

# Specify the folder where the downloaded filings are stored
download_folder = 'sec-edgar-filings'

# Compress the downloaded filings into a ZIP file
shutil.make_archive('AMZN', 'zip', download_folder)

# The ZIP file will now be stored locally in the same directory where the script is executed
print(f"ZIP file 'AMZN.zip' has been successfully created in the current directory.")
