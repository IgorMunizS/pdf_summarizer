import PyPDF2
import io



def extract_text_from_pdf(content: bytes):
    text = ""
    read_pdf = PyPDF2.PdfReader(io.BytesIO(content))
    number_of_pages = len(read_pdf.pages)
    for page_number in range(number_of_pages):  # use xrange in Py2
        page = read_pdf.pages[page_number]
        page_content = page.extract_text()
        text += page_content + "\n\n"

    return text
