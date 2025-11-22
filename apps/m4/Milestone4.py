from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer
import sys

def main():
    if len(sys.argv) != 2:
        
        return

    with open(sys.argv[1], encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    count = 0
    for node in soup:
        count += 1

    print("Total nodes:", count)

if __name__ == "__main__":
    main()