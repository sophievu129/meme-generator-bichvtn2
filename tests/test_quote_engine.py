"""Check that Ingestor classes can be constructed and ingest on required file.

To run these tests from the project root, run:
    $ python -m unittest --verbose tests.test_quote_engine
"""
import pathlib
import unittest

from QuoteEngine.csv_ingestor import CsvIngestor
from QuoteEngine.docx_ingestor import DocxIngestor
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.pdf_ingestor import PdfIngestor
from QuoteEngine.txt_ingestor import TxtIngestor

# Paths to the test data files.

TESTS_ROOT = str(pathlib.Path(__file__).parent.resolve())\
    .replace("\\", "/").replace("//", "/")
TEST_DOG_QUOTES = "/../_data/DogQuotes"
TEST_SIMPLE_LINES = "/../_data/SimpleLines"


class TestCSVIngestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path_dog_quotes = TESTS_ROOT + TEST_DOG_QUOTES
        cls.path_simple_lines = TESTS_ROOT + TEST_SIMPLE_LINES

    def test_csv_ingestor_dog_quotes(self):
        doc = CsvIngestor()
        data = doc.ingest(self.path_dog_quotes + "/DogQuotesCSV.csv")
        print(data)
        self.assertIsInstance(data, list)
        for line in data:
            self.assertIsInstance(line, list)

    def test_csv_ingestor_simple_lines(self):
        doc = CsvIngestor()
        data = doc.ingest(self.path_simple_lines + "/SimpleLines.csv")
        print(data)
        self.assertIsInstance(data, list)
        for line in data:
            self.assertIsInstance(line, list)


class TestDocxIngestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path_dog_quotes = TESTS_ROOT + TEST_DOG_QUOTES
        cls.path_simple_lines = TESTS_ROOT + TEST_SIMPLE_LINES

    def test_docx_ingestor_dog_quotes(self):
        doc = DocxIngestor()
        data = doc.ingest(self.path_dog_quotes + "/DogQuotesDOCX.docx")
        print(data)
        self.assertIsInstance(data, list)
        for line in data:
            self.assertIsInstance(line, list)

    def test_docx_ingestor_simple_lines(self):
        doc = DocxIngestor()
        data = doc.ingest(self.path_simple_lines + "/SimpleLines.docx")
        print(data)
        self.assertIsInstance(data, list)
        for line in data:
            self.assertIsInstance(line, list)


class TestPdfIngestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path_dog_quotes = TESTS_ROOT + TEST_DOG_QUOTES
        cls.path_simple_lines = TESTS_ROOT + TEST_SIMPLE_LINES

    def test_pdf_ingestor_dog_quotes(self):
        doc = PdfIngestor()
        data = doc.ingest(self.path_dog_quotes + "/DogQuotesPDF.pdf")
        print(data)
        self.assertIsInstance(data, list)
        for line in data:
            self.assertIsInstance(line, list)

    def test_pdf_ingestor_simple_lines(self):
        doc = PdfIngestor()
        data = doc.ingest(self.path_simple_lines + "/SimpleLines.pdf")
        print(data)
        self.assertIsInstance(data, list)
        for line in data:
            self.assertIsInstance(line, list)


class TestTxtIngestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path_dog_quotes = TESTS_ROOT + TEST_DOG_QUOTES
        cls.path_simple_lines = TESTS_ROOT + TEST_SIMPLE_LINES

    def test_txt_ingestor_dog_quotes(self):
        doc = TxtIngestor()
        data = doc.ingest(self.path_dog_quotes + "/DogQuotesTXT.txt")
        print(data)
        self.assertIsInstance(data, list)
        for line in data:
            self.assertIsInstance(line, list)

    def test_txt_ingestor_simple_lines(self):
        doc = TxtIngestor()
        data = doc.ingest(self.path_simple_lines + "/SimpleLines.txt")
        print(data)
        self.assertIsInstance(data, list)
        for line in data:
            self.assertIsInstance(line, list)


class TestParseIngestor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path_dog_quotes = TESTS_ROOT + TEST_DOG_QUOTES + "/DogQuotes"

    def test_csv_ingestor(self):
        data = Ingestor().parse(self.path_dog_quotes + "CSV.csv")
        print(data)
        self.assertIsInstance(data, list)

    def test_docx_ingestor(self):
        data = Ingestor().parse(self.path_dog_quotes + "DOCX.docx")
        print(data)
        self.assertIsInstance(data, list)

    def test_pdf_ingestor(self):
        data = Ingestor().parse(self.path_dog_quotes + "PDF.pdf")
        print(data)
        self.assertIsInstance(data, list)

    def test_txt_ingestor(self):
        data = Ingestor().parse(self.path_dog_quotes + "TXT.txt")
        print(data)
        self.assertIsInstance(data, list)
