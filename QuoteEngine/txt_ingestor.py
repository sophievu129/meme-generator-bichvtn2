"""A ingestor to get quotes from txt file."""

from typing import List
from QuoteEngine import IngestorInterface


class TxtIngestor(IngestorInterface):
	"""Ingestor to work with txt file."""

	def __init__(self):
		"""Initialize pdf ingestor."""
		super().__init__("txt")

	def ingest(self, path: str) -> List[List]:
		"""Ingest text file.

		Return a list of quote, which is a list consist of first element as body,
		second element as author
		"""
		data = []
		file = open(path, mode='r', encoding='utf-8-sig')
		for line in file.readlines():
			line = line.replace("\n","").replace("\"", "").strip().rsplit('-', 1)
			if len(line) == 2:
				line[0] = line[0].strip()
				line[1] = line[1].strip()
				data.append(line)
		file.close()
		return data
