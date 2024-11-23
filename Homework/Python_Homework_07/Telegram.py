import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
from PyPDF2 import PdfReader
from PIL import Image
from io import BytesIO

# Bot token from BotFather
BOT_TOKEN = "7831376301:AAHBfUeIHzfb7w272XC3vWpywmSlaGml4O4"

# Download directory for incoming files
DOWNLOAD_DIR = "./downloads"

# Ensure the directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Function to extract the first page of a PDF as an image
def extract_first_page_as_image(pdf_path):
    try:
        # Open the PDF file
        reader = PdfReader(pdf_path)
        first_page = reader.pages[0]
        text = first_page.extract_text()
        # For demonstration, create an image with text
        img = Image.new("RGB", (600, 800), color="white")
        from PIL import ImageDraw
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), text[:1000], fill="black")  # Limiting text to 1000 characters
        return img
    except Exception as e:
        print(f"Error extracting first page: {e}")
        return None

# Handler for incoming PDF files
async def handle_document(update: Update, context: CallbackContext):
    # Check if the document is a PDF
    file = update.message.document
    if file.mime_type != "application/pdf":
        await update.message.reply_text("Please send a valid PDF file.")
        return

    # Download the PDF file
    file_id = file.file_id
    new_file = await context.bot.get_file(file_id)
    pdf_path = os.path.join(DOWNLOAD_DIR, file.file_name)
    await new_file.download_to_drive(pdf_path)

    # Extract the first page and convert it to an image
    img = extract_first_page_as_image(pdf_path)
    if img:
        # Convert the image to bytes and send it back
        bio = BytesIO()
        bio.name = "first_page.jpg"
        img.save(bio, "JPEG")
        bio.seek(0)
        await context.bot.send_photo(chat_id=update.message.chat_id, photo=bio)
    else:
        await update.message.reply_text("Failed to extract the first page from the PDF.")

# Start command handler
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Send me a PDF file, and I'll send you the first page as an image.")

# Main function to start the bot
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.PDF, handle_document))

    # Start polling
    application.run_polling()

if __name__ == "__main__":
    main()
