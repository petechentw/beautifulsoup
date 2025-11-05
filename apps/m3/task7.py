from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer
import os
import sys


def add_class_attr(tag):
   
    if tag.name == "p":
        tag.attrs["class"] = "test"


replacer = SoupReplacer(xformer=add_class_attr)
filename = sys.argv[1]
ext = os.path.splitext(filename)[1].lower()
output_file = "apps/m3/output.html"

if ext == ".html":
    parser = "html.parser"
else:
    parser = "lxml"
    


with open(filename, "r", encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(open(filename), "html.parser", replacer=replacer)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

