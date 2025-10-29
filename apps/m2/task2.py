from bs4 import SoupStrainer
from bs4 import BeautifulSoup
import sys
import time
import os

start_time = time.time()

filename = sys.argv[1]
ext = os.path.splitext(filename)[1].lower() 
only_a_tags = SoupStrainer("a")

if ext == ".html":
    parser = "html.parser"
else:
    parser = "lxml"

soup = BeautifulSoup(open(filename),parser,parse_only=only_a_tags)
with open("task1.txt","w") as file:
    file.write(soup.prettify())

print(soup.prettify)