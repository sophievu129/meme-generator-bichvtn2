"""Quote models contain body, which is a quote, and author."""
from abc import ABC, abstractmethod
from typing import List
from xmlrpc.client import boolean


class QuoteModel:
    """Quote Model object."""

    def __init__(self, body: str, author: str):
        """Initiate a Quote model that contain body and author."""
        self._body = body
        self._author = author

    @property
    def body(self):
        """Return body of quote model."""
        return self._body

    @property
    def author(self):
        """Return author of quote model."""
        return self._author

    def __str__(self):
        """Return 'str(self)'."""
        return f"{self._body} - {self._author}"

    def __repr__(self):
        """Return 'repr(self)'."""
        return str({"body": self._body, "author": self._author})


class IngestorInterface(ABC):
    """Abstract class for ingestors."""

    def __init__(self, extension=None):
        """Initialize the ingestor."""
        self.extension = extension

    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        """Check whether the Ingestor can ingest the file.

        :param cls: the specific ingestor class
        :param path: string - path of file that need to ingest

        :return True|False whether the ingestor can ingest the file
        """
        path_ext = path.rsplit('.', 1)[-1]
        if cls().extension == path_ext:
            return True
        else:
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return list of model."""
        quote_list = []
        list_q = cls().ingest(path)
        for row in list_q:
            body = row[0]
            author = row[1]
            quote_list.append(QuoteModel(body, author))
        return quote_list

    @abstractmethod
    def ingest(self, path: str):
        """Abstract method for ingesting file.

        :return list of dictionary of quotes
        """
        pass
