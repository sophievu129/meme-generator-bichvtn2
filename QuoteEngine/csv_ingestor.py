"""A ingestor to get quotes from csv file."""

import pandas as pd
from typing import List
from QuoteEngine import IngestorInterface


class CsvIngestor(IngestorInterface):
    """Ingestor to work with csv file."""

    def __init__(self):
        """Initialize csv ingestor."""
        super().__init__("csv")

    def ingest(self, path: str) -> List[List]:
        """Ingest csv file.

        Return a list of quote, which is a list
        consist of first element as body,
        second element as author
        """
        df = pd.read_csv(path)
        list_quote = df.values.tolist()
        for row in list_quote:
            row[0] = row[0].replace("\"", "").strip()
        return list_quote
