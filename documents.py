from glob import glob
from PyPDF2 import PdfReader


class Documents:
    def __init__(self, path='documents/'):
        self.path = path

    def gather_documents(self):
        text = ''
        for file in glob(f'{self.path}/*pdf'):
            doc = PdfReader(file)
            for page in doc.pages:
                text += page.extract_text()
        return self.preprocess_documents(text)

    def preprocess_documents(self, text):
        # Remove breaklines
        text = text.replace('\n', ' ')

        # Remove non-ASCII characters
        text = ''.join(char for char in text if ord(char) < 128)
        return text


if __name__ == '__main__':
    docs = Documents()
    print(docs.gather_documents())
