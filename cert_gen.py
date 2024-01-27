import PyPDF2
import re

# Open the PDF file
with open('CERTIFICATE.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Create a new PDF writer
    pdf_writer = PyPDF2.PdfWriter()

    # Process each page
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]

        # Get the page content as text
        page_text = page.extract_text()

        # Find and replace values in Jinja2-like brackets
        modified_text = re.sub(r'\{\{(.*?)\}\}', 'my_name', page_text)

        # Add a new page to the writer
        pdf_writer.add_page(page)

        # Add the modified text to the new page (experimental, might not work reliably)
        try:
            annotation = {
            "Contents": "This is a note annotation",
            "Rect": [0.1, 0.5, 0.3, 0.75],  # Coordinates for placement
            "Subtype": "/Text",  # Specify it's a text annotation
            }
            pdf_writer.add_annotation(0, annotation)  # Add to page 0
        except AttributeError:
            print("Warning: Adding text directly to pages is not supported by PyPDF2. Consider alternative libraries for direct text modification.")

# Save the modified PDF
with open('modified_pdf_file.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)
