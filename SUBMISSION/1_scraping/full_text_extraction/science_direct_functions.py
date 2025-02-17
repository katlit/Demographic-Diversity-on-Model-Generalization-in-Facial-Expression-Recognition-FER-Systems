import re
from difflib import SequenceMatcher
import pdfplumber

DELETE_JAVASCRIPT_TEXT = """
JavaScript is disabled on your browser. Please enable JavaScript to use all
the features on this page. Skip to main contentSkip to article
ScienceDirect
* Journals & Books
* Help
* Search
Gergo Gyori
IT University of Copenhagen
* View **PDF**
* Download full issue
Search ScienceDirect"""

def remove_empty_lines(text):
    """
    Removes empty lines from the given text.
    """
    lines = text.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    return '\n'.join(non_empty_lines)

def delete_after_references(text):
    """
    Deletes everything after the "## References" part of the given text.
    """
    references_index = text.find("## References")
    if references_index != -1:
        return text[:references_index]
    else:
        return text

def get_sentences(text):
    """
    Splits the given text into a list of sentences.
    """
    return [sentence.strip() for sentence in text.split('\n') if sentence.strip()]


def _delete_parts_from_text(text, parts_to_delete):
    """
    Removes the specified parts from the beginning of the text.
    """
    parts_to_delete = get_sentences(parts_to_delete)
    for part in parts_to_delete:
        if text.startswith(part):
            text = text[len(part):].strip()
    return text

def delete_parts_from_text(text, parts_to_delete):
    parts_to_delete = get_sentences(parts_to_delete)
    for part in parts_to_delete:
        text = text.replace(part, '')
    return text

def extract_text_from_pdf(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() if page.extract_text() else ''
            return text
    except Exception as e:
        print(f"Failed to extract text from {pdf_file}: {e}")
        return ""

def extract_numbers(filename):
    """
    Extracts the numbers from a filename.
    
    Args:
        filename (str): The filename to extract numbers from.
    
    Returns:
        int: The extracted number.
    """
    match = re.search(r"\d+", filename)
    if match:
        return int(match.group())
    else:
        return None

def extract_title_from_pdf(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            first_page_text = pdf.pages[0].extract_text()
            
            # Check if the title line starts with '## Title:'
            title_line = first_page_text.split('\n')[0]  # Assumes title is the first line
            
            if title_line.startswith("## Title:"):
                title = title_line.replace("## Title:", "").strip()
            else:
                title = title_line.strip()
                
            return title
    except Exception as e:
        print(f"Failed to extract title from {pdf_file}: {e}")
        return ""


# Helper function to find the closest matching title in Scrape_df
def find_closest_title(pdf_title, title_list):
    closest_title = None
    highest_ratio = 0
    for title in title_list:
        ratio = SequenceMatcher(None, pdf_title, title).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            closest_title = title
    return closest_title if highest_ratio > 0.8 else None  # Threshold for similarity


