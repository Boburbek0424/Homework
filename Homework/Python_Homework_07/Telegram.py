import os

BOT_TOKEN = "7831376301:AAHBfUeIHzfb7w272XC3vWpywmSlaGml4O4"

# Directory to temporarily store files
DOWNLOAD_DIR = "./downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Function to extract the first page's text and convert it to an image
def extract_first_page_as_image(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        first_page = reader.pages[0]
        text = first_page.extract_text()

        # Create an image with the extracted text
        img = Image.new("RGB", (600, 800), "white")
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), text[:1000], fill="black")  # Limit text length
        return img
    except Exception as e:
        print(f"Error extracting first page: {e}")
        return None

