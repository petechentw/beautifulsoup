from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

def run_tests():
    print("🧪 Running simple SoupReplacer tests...\n")

    
    # Simple tag replacement
    
    html = "<b>Hello</b>"
    replacer = SoupReplacer("b", "strong")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    print("Test 1 result:", soup)
    assert soup.find("strong") is not None
    print("✅\n")

    
    #  name_xformer
  
    html = "<b>Hello</b>"
    replacer = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    print("Test 2 result:", soup)
    assert soup.find("blockquote") is not None
    print("✅ \n")

   
    #  attrs_xformer

    html = "<p>Hi</p>"
    replacer = SoupReplacer(attrs_xformer=lambda tag: {"class": ["demo"]} if tag.name == "p" else tag.attrs)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    print("Test 3 result:", soup)
    assert soup.find("p")["class"] == ["demo"]
    print("✅ \n")

   
    # xformer (side effect)
    
    def add_id(tag):
        if tag.name == "p":
            tag.attrs["id"] = "newid"

    html = "<p>Hi</p>"
    replacer = SoupReplacer(xformer=add_id)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    print("Test 4 result:", soup)
    assert soup.find("p")["id"] == "newid"
    print("✅ \n")

   
    #  No transformers
    
    html = "<p>unchanged</p>"
    replacer = SoupReplacer()
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    print("Test 5 result:", soup)
    assert soup.find("p").text.strip() == "unchanged"
    print("✅ \n")

   

    #  Combined name_xformer + attrs_xformer

    html = "<b>Mix</b>"
    replacer = SoupReplacer(
        name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name,
        attrs_xformer=lambda tag: {"style": "color:red;"} if tag.name in ["b", "strong"] else tag.attrs,
    )
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    print("Test 6 result:", soup)
    tag = soup.find("strong")
    assert tag is not None and "style" in tag.attrs and "color:red" in tag["style"]
    print("✅\n")

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
