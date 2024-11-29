import PyPDF2
from deep_translator import GoogleTranslator
from tkinter import Tk, messagebox

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from the provided PDF file.

    Parameters:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error while reading the PDF: {e}"

def translate_text(input_text, target_lang='hi'):
    """
    Translates the given text into a target language using deep-translator.

    Parameters:
        input_text (str): Text to be translated.
        target_lang (str): Target language code (default is Hindi 'hi').

    Returns:
        str: Translated text.
    """
    try:
        # Using GoogleTranslator from deep-translator
        translated_text = GoogleTranslator(source='auto', target=target_lang).translate(input_text)
        return translated_text
    except Exception as e:
        return f"Error during translation: {e}"

def show_translation_in_new_window(translated_text):
    """
    Displays the translated text in a new window using tkinter.

    Parameters:
        translated_text (str): The translated text to display.
    """
    window = Tk()
    window.title("Translated Text")

    # Display the translated text in a message box
    messagebox.showinfo("Translated Text", translated_text)

    # Close the window after the message box is dismissed
    window.mainloop()

def main():
    """
    Main function to handle PDF translation and display in a new window.
    """
    # Input file path
    pdf_path = input("Enter the path of the PDF file: ")
    print(f"Attempting to read file at: {pdf_path}")
    
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    if "Error" in pdf_text:
        print(pdf_text)  # If error occurred during PDF reading
    else:
        print(f"Extracted Text: {pdf_text[:500]}...")  # Print the first 500 characters of the extracted text for verification

        # Translate the text
        translated_text = translate_text(pdf_text)

        # Show the translated text in a new window
        show_translation_in_new_window(translated_text)

if __name__ == "__main__":
    main()
