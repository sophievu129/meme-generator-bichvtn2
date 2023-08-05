"""Check that MemeGenerator can be constructed and generate meme.

To run these tests from the project root, run:
    $ python -m unittest --verbose tests.test_meme_generator
"""
import os.path
import pathlib
import random
import unittest

from MemeEngine.meme_generator import MemeEngine
from QuoteEngine.ingestor import Ingestor


# Paths to the test data files.

TESTS_ROOT = str(pathlib.Path(__file__).parent.resolve()).replace("\\", "/").replace("//","/")
TEST_DOG_PHOTO = "/../_data/photos/dog"
TEST_PANDA_PHOTO = "/../_data/photos/panda"


class TestMemeGenerate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path_meme_dir = TESTS_ROOT
        cls.path_dog_photo = TESTS_ROOT + TEST_DOG_PHOTO
        cls.path_panda_photo = TESTS_ROOT + TEST_PANDA_PHOTO
        cls.path_dog_quotes = TESTS_ROOT + "/../_data/DogQuotes"
        cls.path_panda_quotes = TESTS_ROOT + "/../_data/PandaQuotes"

        cls.file_dogs = ['/xander_1.jpg',
                         '/xander_2.jpg',
                         '/xander_3.jpg',
                         '/xander_4.jpg']
        list_dog_quotes = ['/DogQuotesCSV.csv',
                           '/DogQuotesDOCX.docx',
                           '/DogQuotesPDF.pdf',
                           '/DogQuotesTXT.txt']
        cls.dog_quotes = []
        for file in list_dog_quotes:
            file_quote = cls.path_dog_quotes + file
            quotes = Ingestor().parse(file_quote)
            for quote in quotes:
                cls.dog_quotes.append(quote)

        cls.file_pandas = ['/qizi_funny_1.jpg',
                           '/aibao_pretty_1.jpg',
                           '/aibao_cute_1.jpg',
                           '/fubao_cute_1.jpg',
                           '/fubao_cute_2.jpg',
                           '/fubao_cute_3.jpg',
                           '/fubao_cute_4.jpg',
                           '/fubao_cute_5.jpg',
                           '/fubao_funny_1.jpg',
                           '/fubao_funny_2.jpg',
                           '/fubao_funny_3.jpg',
                           '/lebao_cool_1.jpg',
                           '/lebao_cool_2.jpg',
                           '/lebao_cool_3.jpg',
                           '/lebao_cool_4.jpg',
                           '/lebao_cool_5.jpg',
                           '/lebao_funny_1.jpg',
                           '/lebao_funny_2.jpg',
                           '/lebao_funny_3.jpg',
                           '/panda_cute_1.jpg',
                           '/panda_funny_1.jpg',
                           '/panda_love_1.jpg',
                           '/panda_love_2.jpg']
        list_panda_quotes = ['/PandaQuotesTXT.txt',
                             '/PandaQuotesDOCX.docx']
        cls.panda_quotes = []
        for file in list_panda_quotes:
            file_quote = cls.path_panda_quotes + file
            quotes = Ingestor().parse(file_quote)
            for quote in quotes:
                cls.panda_quotes.append(quote)

    def test_generate_dog_meme(self):
        meme_generator = MemeEngine(self.path_meme_dir)
        filename = random.choice(self.file_dogs)
        img_path = self.path_dog_photo + filename
        quote = random.choice(self.dog_quotes)

        meme_path = meme_generator.make_meme(img_path, quote, 500)

        self.assertTrue(os.path.exists(meme_path))

    def test_generate_panda_meme(self):
        meme_generator = MemeEngine(self.path_meme_dir)
        filename = random.choice(self.file_pandas)
        img_path = self.path_panda_photo + filename
        quote = random.choice(self.panda_quotes)

        meme_path = meme_generator.make_meme(img_path, quote, 500)
        self.assertTrue(os.path.exists(meme_path))
