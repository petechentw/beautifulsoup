from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer
import os
import sys
def main():
    filename = sys.argv[1]
    ext = os.path.splitext(filename)[1].lower()


    if ext == ".html":
        parser = "html.parser"
    else:
        parser = "lxml"
    


    b_to_blockquote = SoupReplacer("b", "blockquote")

  
    soup = BeautifulSoup(open(filename), "html.parser",replacer=b_to_blockquote)




    print(soup.prettify())

    

if __name__ == "__main__":
    main()