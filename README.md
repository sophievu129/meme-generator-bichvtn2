# Meme Generator App Project

Meme generator app is a flask app for creating meme.
This app can run locally or in website publicly (for web app it will only available at the end of August, 2023.
## Source code structure

Source code of the app contains these folders and files:
- app.py : file to run app to generate memes.
- meme.py : file to generate memes using command lines.
- _data: directory that contains all data, included: quotes and images and font.
- QuoteEngine: module for ingest different type of quote file, return a list of QuoteModel objects. QuoteModel object have body and author attributes.
- MemeEngine: module to make meme with a picture and a text.
- static: folder to save new generated memes when running app.
- templates: templates for Meme Generator App.
- tests: unit test folder.
- tmp: folder to save new generated memes using command line.
- Procfile, runtime.txt: files for running web app in Heroku.

## Preparation environment

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required packages, which are stored inside requirements.txt.

```bash
pip install -r requirements.txt
```
Python version must be 3.9 to run app. Specified version is saved in file runtime.txt.

## Generate meme using command line

Using this command to see the format:
```bash
python meme.py -h

usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]
                                                                 
Generate Random Meme.                                            
                                                                 
optional arguments:                                              
  -h, --help       show this help message and exit               
  --path PATH      Path to an image file for meme.               
  --body BODY      Quote body to add to the image.               
  --author AUTHOR  Quote author to add to the image. 
```
Example:
```bash
# Generate default meme.
python meme.py
# Generate meme with specified picture and quote.
python meme.py --path _data/photos/dog/xander_1.jpg --body Hi --author Bich
python meme.py --path _data/photos/dog/xander_1.jpg --body "Hi there" --author Bich
```

## Run app locally

Run meme generator app locally. You can one of below commands:
```bash
# This will run without specify host, port and will not enable debugging.
python app.py
# This will enable debug, and also custom host and port, and will reload app if there
# is any change in the source code.
python -m flask run --host 0.0.0.0 --port 3000 --reload --debug
```

## Run public web app

Go to the link below to use web app. The web app available only until the end of August, 2023.

[https://meme-generator-bichvtn2-d15e33629fd8.herokuapp.com/](https://meme-generator-bichvtn2-d15e33629fd8.herokuapp.com/)

## Contact

Bich Vu - BichVTN2@fpt.com