from abc import ABC
from QuoteEngine import QuoteModel


class IngestorInterface(QuoteModel, ABC):

    def __init__(self, info, body: str, author: str):
        super().__init__(body, author)
        self.info = info
