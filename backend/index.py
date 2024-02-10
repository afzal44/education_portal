from spire.pdf.common import *
from spire.pdf import *
from datetime import datetime
import random
from PyPDF2.generic import RectangleObject
from PyPDF2 import PdfReader, PdfWriter


def crop_pdf_borders(input_file, output_file, margins):
  """
  Crops the borders of a PDF based on specified margins.

  Args:
      input_file (str): Path to the input PDF file.
      output_file (str): Path to save the cropped PDF file.
      margins (tuple): A tuple containing margins in (left, top, right, bottom) order.
                        Values are in points (1 point = 1/72 inch).

  Raises:
      ValueError: If margins are invalid or outside page dimensions.
  """
  with open(input_file, "rb") as file:
    reader = PdfReader(file)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
      page = reader.pages[page_num]
      mediabox = page.mediabox
      print(f"mediabox: {mediabox}")
      page.cropbox = RectangleObject((40, 7, 840, 560))
      new_page = writer.add_page(page)

      # Add the cropped page to the writer
      # writer.add_page(new_page)

    with open(output_file, "wb") as outfile:
      writer.write(outfile)


def generate_random_id(prefix='WCEI-', length=10):
    random_numbers = [random.randint(0, 9) for _ in range(length - len(prefix))]
    random_string = ''.join(map(str, random_numbers))
    return f"{prefix}{random_string}"


def replace_placeholders(page, replacements):
    replacer = PdfTextReplacer(page)

    for placeholder, value in replacements.items():
        replacer.ReplaceAllText(placeholder, value)

def get_user_input():
    full_name = input("Enter full name: ")
    course_name = "Basics of computer"
    id_value = generate_random_id()
    date_value = datetime.now().strftime("%Y-%m-%d")
    return {
        "{{Full_Name}}": full_name,
        "{{Date}}": date_value,
        "{{id}}": id_value,
        "{{Course_Name}}": course_name
    }

if __name__ == "__main__":
    # Create an object of the PdfDocument class
    doc = PdfDocument()
    
    # Load a PDF file
    doc.LoadFromFile("./pdf/pdf_file.pdf")

    # Get user input for dynamic values
    replacements = get_user_input()

    # Iterate through the pages in the document
    for i in range(doc.Pages.Count):
        # Get the current page
        page = doc.Pages[i]

        # Replace placeholders on the current page
        replace_placeholders(page, replacements)

    # Save the resulting file
    output_filename = f"./output/{replacements['{{id}}']}.pdf"
    doc.SaveToFile(output_filename)

    # Close the document
    doc.Close()
    # Example usage
    input_file = output_filename
    output_file = "cropped_pdf.pdf"
    margins = (0, 7, 800, 600)  # Example margins in points
    crop_pdf_borders(input_file, output_file, margins)

