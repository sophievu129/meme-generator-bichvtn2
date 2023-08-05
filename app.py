"""Application to create meme."""
import os
import pathlib
import random
from io import BytesIO

import requests
from PIL import Image
from flask import Flask, request, render_template

from QuoteEngine import QuoteModel
from QuoteEngine.ingestor import Ingestor
from meme import MemeEngine

PROJECT_ROOT = str(pathlib.Path(__file__).parent.resolve()).replace("\\", "/").replace("//", "/")
meme_app = Flask(__name__)

meme = MemeEngine(PROJECT_ROOT+'/static')


def get_quote(list_file):
    """Get all quotes from list of quote files."""
    list_quotes = []
    for file in list_file:
        l_quotes = Ingestor().parse(str(file))
        for quote in l_quotes:
            list_quotes.append(quote)
    return list_quotes


def get_image(dir_path):
    """Get all image path from image directory."""
    list_imgs = []
    for images in os.listdir(dir_path):
        # check if the image ends with png
        if (images.endswith(".png")) or (images.endswith(".jpg")):
            list_imgs.append(dir_path + '/' + images)
    return list_imgs


def setup():
    """Load all resources."""
    dog_quote_files = [PROJECT_ROOT+'/_data/DogQuotes/DogQuotesTXT.txt',
                       PROJECT_ROOT+'/_data/DogQuotes/DogQuotesDOCX.docx',
                       PROJECT_ROOT+'/_data/DogQuotes/DogQuotesPDF.pdf',
                       PROJECT_ROOT+'/_data/DogQuotes/DogQuotesCSV.csv']
    panda_quote_files = [PROJECT_ROOT+'/_data/PandaQuotes/PandaQuotesTXT.txt',
                         PROJECT_ROOT+'/_data/PandaQuotes/PandaQuotesDOCX.docx',
                         PROJECT_ROOT+'/_data/PandaQuotes/PandaQuotesPDF.pdf',
                         PROJECT_ROOT+'/_data/PandaQuotes/PandaQuotesCSV.csv']
    dog_quotes = get_quote(dog_quote_files)
    pandas_quotes = get_quote(panda_quote_files)

    imgs_dog = get_image(PROJECT_ROOT + '/_data/photos/dog')
    imgs_panda = get_image(PROJECT_ROOT + '/_data/photos/panda')

    return [dog_quotes, pandas_quotes], [imgs_dog, imgs_panda]


quotes, imgs = setup()


@meme_app.route('/')
def meme_rand():
    """Generate a random meme."""
    num = random.randint(0, 1)
    img = random.choice(imgs[num])
    quote = random.choice(quotes[num])
    path = meme.make_meme(img, quote).split("\\")[-1].split("/")[-1]
    return render_template('meme.html', path=path)


@meme_app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@meme_app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # Get image url, body quote and author from form
    img_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    # Download and save image in to photos folder
    img_name = img_url.split("\\")[-1].split("/")[-1]
    img_path = PROJECT_ROOT + '/static/' + img_name
    try:   # For when running app locall
        response = requests.get(img_url)
        if response.status_code:
            fp = open(img_path, 'wb')
            fp.write(response.content)
            fp.close()
            img = Image.open(img_path)
            img.save(img_path)
    except Exception:   # For when running app in server
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        img.save(img_path)

    # Create user defined meme
    path = meme.make_meme(img_path, QuoteModel(body, author)).split("\\")[-1].split("/")[-1]

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    """Run meme generator application."""
    meme_app.run()
