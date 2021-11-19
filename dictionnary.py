import requests
import os
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import urllib.request



imgURL = "http://laceliah.cowblog.fr/images/Striplife/agoraphobe.jpg"

r = requests.get(imgURL).content


with open("agoraphobe.jpg", "wb+") as f:
    f.write(r)


