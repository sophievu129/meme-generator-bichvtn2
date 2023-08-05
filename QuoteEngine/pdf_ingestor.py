"""A ingestor to get quotes from pdf file."""
import os
import subprocess
from typing import List

from PyPDF2 import PdfReader
from QuoteEngine import IngestorInterface


class PdfIngestor(IngestorInterface):
    """Ingestor to work with pdf file."""

    def __init__(self):
        """Initialize pdf ingestor."""
        super().__init__("pdf")

    def ingest(self, path: str) -> List[List]:
        """Ingest text file.

        Return a list of quote, which is a list
        consist of first element as body,
        second element as author
        """
        data = []
        txt_path = path[:-4] + "_edit.txt"
        try:
            # This block is for run app local
            process = subprocess.Popen(f"pdftotext {path} {txt_path}")
            while True:
                if os.path.exists(txt_path):
                    file = open(txt_path, mode='r', encoding='utf-8-sig')
                    lines = file.readline().split("\"")[1:]
                    for i in range(0, len(lines), 2):
                        body = lines[i].replace("\"", "").strip()
                        author = lines[i+1].replace("-", "")\
                            .replace("\n", "").strip()
                        data.append([body, author])
                    file.close()
                    break
            while True:
                try:
                    process.kill()
                    os.remove(txt_path)
                    break
                except Exception as e:
                    print(e)
                    pass
        except Exception as e:
            # This is for deploy web app in Heroku
            reader = PdfReader(path)
            for page in reader.pages:
                lines = page.extract_text().split('"')[1:]
                for i in range(0, len(lines), 2):
                    body = lines[i].replace("\"", "").strip()
                    author = lines[i + 1].replace("-", "")\
                        .replace("\n", "").strip()
                    data.append([body, author])

        return data
