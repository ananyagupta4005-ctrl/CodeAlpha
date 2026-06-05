#   TASK 3: Task Automation with Python Scripts
#   Concepts: os, shutil, re, requests, file handling
#   All 3 tasks in one file!

import os
import shutil
import re
import requests

#   TASK 3A: Move all .jpg files to a new folder
#   Concepts used: os, shutil

def move_jpg_files(source_folder, destination_folder):
    """
    Moves all .jpg files from source_folder to destination_folder.
    If destination folder doesn't exist, it creates one automatically.
    """

    print("\n" + "=" * 50)
    print("  TASK A: Moving .jpg files")
    print("=" * 50)

    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"  Created folder: '{destination_folder}'")

    # Get list of all files in source folder
    all_files = os.listdir(source_folder)

    moved_count = 0

    # Loop through each file
    for filename in all_files:

        # Check if file ends with .jpg
        if filename.lower().endswith('.jpg'):

            # Build full path of source and destination
            source_path = os.path.join(source_folder, filename)
            dest_path   = os.path.join(destination_folder, filename)

            # Move the file
            shutil.move(source_path, dest_path)
            print(f"  Moved: {filename}")
            moved_count += 1

    if moved_count == 0:
        print("  No .jpg files found in source folder.")
    else:
        print(f"\n  Done! {moved_count} file(s) moved to '{destination_folder}'")

#   TASK 3B: Extract all email addresses from a .txt file
#   Concepts used: re (regex), file handling

def extract_emails(input_file, output_file):
    """
    Reads a .txt file, finds all email addresses using regex,
    and saves them to another file.
    """

    print("\n" + "=" * 50)
    print("  TASK B: Extracting Email Addresses")
    print("=" * 50)

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"  File '{input_file}' not found!")
        print("  Creating a sample input file for demo...")

        # Create a sample file with some emails for demo
        sample_text = """
        Hello, please contact us at support@example.com for help.
        You can also reach John at john.doe@gmail.com or
        the manager at manager_99@company.org for business queries.
        Invalid emails like @noname or missingat.com will be ignored.
        For billing, email billing@mywebsite.in or info@test.co.uk
        """
        with open(input_file, 'w') as f:
            f.write(sample_text)
        print(f"  Sample file '{input_file}' created!")

    # Read the input file
    with open(input_file, 'r') as f:
        content = f.read()

    # Regex pattern to match email addresses
    # Pattern: word chars + @ + word chars + . + 2-6 letter domain
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}'

    # Find all emails in the text
    emails_found = re.findall(email_pattern, content)

    # Remove duplicates
    emails_found = list(set(emails_found))

    if not emails_found:
        print("  No email addresses found in the file.")
        return

    # Save emails to output file
    with open(output_file, 'w') as f:
        f.write("Extracted Email Addresses\n")
        f.write("=" * 30 + "\n")
        for email in emails_found:
            f.write(email + "\n")

    # Print results
    print(f"  Found {len(emails_found)} email(s):")
    for email in emails_found:
        print(f"    -> {email}")
    print(f"\n  Saved to: '{output_file}'")

#   TASK 3C: Scrape the title of a fixed webpage
#   Concepts used: requests, string handling
# ============================================================

def scrape_webpage_title(url, output_file):
    """
    Fetches a webpage and extracts its <title> tag content.
    Saves the title to a text file.
    """

    print("\n" + "=" * 50)
    print("  TASK C: Scraping Webpage Title")
    print("=" * 50)

    print(f"  Fetching: {url}")

    try:
        # Send GET request to the URL
        response = requests.get(url, timeout=10)

        # Check if request was successful (status 200 = OK)
        if response.status_code == 200:

            # Use regex to find the <title> tag content
            title_pattern = r'<title[^>]*>(.*?)</title>'
            match = re.search(title_pattern, response.text, re.IGNORECASE)

            if match:
                title = match.group(1).strip()
                print(f"  Title found: {title}")

                # Save the title to output file
                with open(output_file, 'w') as f:
                    f.write(f"URL   : {url}\n")
                    f.write(f"Title : {title}\n")

                print(f"  Saved to: '{output_file}'")

            else:
                print("  No title tag found on the page.")

        else:
            print(f"  Failed to fetch page. Status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("  No internet connection. Please check your network.")
    except requests.exceptions.Timeout:
        print("  Request timed out. Try again later.")
    except Exception as e:
        print(f"  Error: {e}")


# ============================================================
#   MAIN — Run all 3 tasks
# ============================================================

def main():

    print("=" * 50)
    print("  TASK 3: Task Automation with Python Scripts")
    print("=" * 50)

    # ---- Task A: Move .jpg files ----
    # Change these folder names as per your system
    source      = "source_images"      # Folder with .jpg files
    destination = "moved_images"       # Folder to move them to

    # Create a demo source folder with fake .jpg file names for testing
    if not os.path.exists(source):
        os.makedirs(source)
        # Create some empty .jpg files for demo
        for name in ["photo1.jpg", "photo2.jpg", "document.pdf", "image3.jpg"]:
            open(os.path.join(source, name), 'w').close()
        print(f"\n  Demo folder '{source}' created with sample files.")

    move_jpg_files(source, destination)

    # ---- Task B: Extract emails ----
    extract_emails(
        input_file  = "sample_emails.txt",   # Input file with text
        output_file = "extracted_emails.txt"  # Output file for results
    )

    # ---- Task C: Scrape webpage title ----
    scrape_webpage_title(
        url         = "https://www.wikipedia.org",
        output_file = "scraped_title.txt"
    )

    print("\n" + "=" * 50)
    print("  All 3 tasks completed successfully!")
    print("=" * 50)


# Run the program
if __name__ == "__main__":
    main()
