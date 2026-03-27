import pdfplumber
import re


def clean_text(text):
    """
    Clean and normalize extracted PDF text.
    """

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # normalize bullet characters
    text = re.sub(r'[•●▪]', '-', text)

    # normalize step formatting
    text = re.sub(r'(Step\s*\d+)', r'\n\1', text)

    # normalize bullet points
    text = re.sub(r'•|-', '\n- ', text)

    # remove trailing spaces
    text = re.sub(r' +\n', '\n', text)

    # remove multiple blank lines
    text = re.sub(r'\n{2,}', '\n\n', text)

    # remove weird spacing around punctuation
    text = re.sub(r'\s+([.,:])', r'\1', text)

    return text.strip()


def extract_text_from_pdf(file_path):
    """
    Extract and clean text from a PDF file.
    Works for both clean and messy PDFs.
    """

    raw_text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                raw_text += page_text + "\n"

    cleaned_text = clean_text(raw_text)

    return cleaned_text

