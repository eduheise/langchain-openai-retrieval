from glob import glob
from PyPDF2 import PdfReader


class Documents:
    def __init__(self, path='documents/') -> None:
        """
        Initialize the Documents class.

        Args:
            path (str): The path to the directory containing PDF documents.
        """
        self.path = path

    def gather_documents(self) -> str:
        """
        Gather text content from all PDF documents in the specified directory.

        Returns:
            str: Preprocessed text content from all PDF documents.
        """
        text = ''
        for file in glob(f'{self.path}/*pdf'):
            doc = PdfReader(file)
            for page in doc.pages:
                text += page.extract_text()
        return self.preprocess_documents(text)

    def preprocess_documents(self, text) -> str:
        """
        Preprocess the extracted text from documents.

        Args:
            text (str): The text content extracted from documents.

        Returns:
            str: Preprocessed text with breaklines removed and non-ASCII characters removed.
        """
        # Removing breaklines
        text = text.replace('\n', ' ')

        # Removing non-ASCII characters
        text = ''.join(char for char in text if ord(char) < 128)
        return text


if __name__ == '__main__':
    docs = Documents()
    print(docs.gather_documents())
