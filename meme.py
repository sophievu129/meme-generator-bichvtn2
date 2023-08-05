"""A generator to generate meme with random picture and random quote."""
import argparse
import os
import pathlib
import random

from MemeEngine.meme_generator import MemeEngine
from QuoteEngine import QuoteModel
from QuoteEngine.ingestor import Ingestor

PROJECT_ROOT = str(pathlib.Path(__file__).parent.resolve())\
    .replace("\\", "/").replace("//", "/")
DATA_ROOT = PROJECT_ROOT + '/_data/photos/dog'


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
    if path is None:
        images = DATA_ROOT
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name).
                    replace("\\", "/") for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = [PROJECT_ROOT + '/_data/DogQuotes/DogQuotesTXT.txt',
                       PROJECT_ROOT + '/_data/DogQuotes/DogQuotesDOCX.docx',
                       PROJECT_ROOT + '/_data/DogQuotes/DogQuotesPDF.pdf',
                       PROJECT_ROOT + '/_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine(PROJECT_ROOT+'/tmp')
    path = meme.make_meme(img, quote)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Random Meme."
    )
    parser.add_argument('--path', default=None,
                        type=str,
                        help="Path to an image file for meme.",
                        required=False)
    parser.add_argument('--body', default="New Meme Generated",
                        type=str,
                        help="Quote body to add to the image.",
                        required=False)
    parser.add_argument('--author', default="Me",
                        type=str,
                        help="Quote author to add to the image.",
                        required=False)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
