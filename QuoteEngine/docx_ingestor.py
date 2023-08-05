"""A ingestor to get quotes from docx file."""

import docx
from typing import List
from QuoteEngine import IngestorInterface


class DocxIngestor(IngestorInterface):
	"""Ingestor to work with csv file."""

	def __init__(self):
		"""Initialize csv ingestor."""
		super().__init__("docx")

	def ingest(self, path: str) -> List[List]:
		"""Ingest docx file.

		Return a list of quote, which is a list consist of first element as body,
		second element as author
		"""
		data = []
		doc = docx.Document(path)
		for para in doc.paragraphs:
			quote = para.text.rsplit('-', 1)
			if len(quote) != 2:
				continue
			body = quote[0].replace('\"', "").strip()
			author = quote[1].strip()
			data.append([body, author])
		return data
