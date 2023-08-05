"""Class that generate meme from image and quote."""
import os
import pathlib
import random

from PIL import Image, ImageFont, ImageDraw
from QuoteEngine import QuoteModel

ROOT_DIR = str(pathlib.Path(__file__).parent.resolve()).replace("\\", "/").replace("//", "/")


class MemeEngine:
    """Generator for random Meme."""

    iterator = 1

    def __init__(self, output_dir=None):
        """Initialize a meme generator."""
        self.output_dir = output_dir

    @staticmethod
    def font(size=1, bold=False, italic=False):
        """Font for text in meme.

        Return to default Times New Roman font, or specific bold/ italic/ bold and italic.
        """
        font_dir = ROOT_DIR + "/../_data/font"
        if bold and italic:
            font_path = font_dir + "/font-times-new-roman/SVN-Times_New_Roman_Bold_Italic.ttf"
        elif bold:
            font_path = font_dir + "/font-times-new-roman/SVN-Times_New_Roman_Bold.ttf"
        elif italic:
            font_path = font_dir + "/font-times-new-roman/SVN-Times_New_Roman_Italic.ttf"
        else:
            font_path = font_dir + "/font-times-new-roman/SVN-Times_New_Roman.ttf"
        return ImageFont.truetype(font=font_path, size=size)

    def make_meme(self, img_path, quote: QuoteModel, width=500) -> str:
        """Make meme from an image and a quote.

        This will take a quote, which has text body and author,
        and put it in random place in the picture.

        :param img_path: path of image for meme.
        :param quote: quote in meme
        :param width: the required size of meme to resize.

        :return meme_path: path to generated meme.
        """
        body = quote.body
        author = "- " + quote.author
        # Get image
        filename = str(img_path).split("/")[-1].split(".")[0]
        pic = Image.open(img_path)

        # Resize image
        old_width, old_lentgh = pic.size
        img_fraction = float(width / old_width)
        length = int(old_lentgh*img_fraction)
        new_pic = pic.resize((width, length))

        # Prepare to edit meme
        meme = ImageDraw.Draw(new_pic)

        # Choose font size less 1 than found size and set font for body and author
        fontsize_author = 1
        text_size_w, text_size_l = self.get_text_size(fontsize_author, body, author)
        while (text_size_w < width) and (text_size_l < length):
            # iterate until the next text size is just larger than the criteria
            fontsize_author += 1
            text_size_w, text_size_l = self.get_text_size(fontsize_author, body, author)

        fontsize_author = fontsize_author - 1

        # Setup font for meme
        text_font_au = self.font(size=fontsize_author)
        text_font_body = self.font(size=fontsize_author * 2)

        # Set size text and locate the coordinates of text
        text_size_w, text_size_l = self.get_text_size(fontsize_author, body, author)
        x = random.randint(0, width-text_size_w)
        y = random.randint(0, length-text_size_l)

        # Add text to image
        meme.text((x, y), body, font=text_font_body, fill="white", stroke_fill="black", stroke_width=2)
        y_body = y + self.font(size=fontsize_author * 2).getsize(body)[1]
        meme.text((x, y_body), author, font=text_font_au, fill="white", stroke_fill="black", stroke_width=2)

        # Save new meme
        while True:
            meme_path = self.output_dir + "/" + filename + "_meme_" + str(self.iterator) + ".jpg"
            if os.path.exists(meme_path):
                self.iterator += 1
            else:
                break
        new_pic.save(meme_path)
        return meme_path

    @classmethod
    def get_text_size(cls, fontsize_author, body, author):
        """Return to text width and length when have font size for author.

        Body will have font size 2 times larger than author.
        :return tuple(text_width, text_length).
        """
        fontsize_body = fontsize_author * 2
        body_w = cls.font(size=fontsize_body).getsize(body)[0]
        body_l = cls.font(size=fontsize_body).getsize(body)[1]
        au_w = cls.font(size=fontsize_author).getsize(author)[0]
        au_l = cls.font(size=fontsize_author).getsize(author)[1]
        text_size_w = max(body_w, au_w)
        text_size_l = body_l + au_l
        return text_size_w, text_size_l
