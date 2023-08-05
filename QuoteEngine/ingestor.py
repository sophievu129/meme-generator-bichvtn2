"""Ingestor class that will ingest any file that have extension csv, docx, pdf, txt."""
from QuoteEngine import IngestorInterface
from QuoteEngine.csv_ingestor import CsvIngestor
from QuoteEngine.docx_ingestor import DocxIngestor
from QuoteEngine.pdf_ingestor import PdfIngestor
from QuoteEngine.txt_ingestor import TxtIngestor


class Ingestor(IngestorInterface):
	"""Ingestor class that will ingest any file that have extension csv, docx, pdf, txt."""

	def __init__(self):
		"""Initialize ingestor."""
		super().__init__()
		self.type_to_ingest = {
			"csv": CsvIngestor(),
			"docx": DocxIngestor(),
			"pdf": PdfIngestor(),
			"txt": TxtIngestor()
		}

	def ingest(self, path: str):
		"""Return to the desired ingestor."""
		extension = path.split('.')[-1]
		ingestor = self.type_to_ingest.get(extension)
		try:
			if ingestor.can_ingest(path):
				return ingestor.ingest(path)
			else:
				raise TypeError(f"Can't not ingest {extension} file.")
		except Exception as e:
			print(e)
