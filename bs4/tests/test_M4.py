from bs4 import BeautifulSoup
from bs4 import NavigableString, Comment


# Test 1 — Soup is iterable 

def test_iter_basic():
    html = "<html><body><p>Hello</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")

    iterator = iter(soup)
    first = next(iterator)

    assert first == soup
    assert first.name == "[document]"



# Test 2 — iterate tags

def test_iter_tags():
    html = "<html><body><b>Bold</b></body></html>"
    soup = BeautifulSoup(html, "html.parser")

    names = [node.name for node in soup if hasattr(node, "name")]

    assert "html" in names
    assert "body" in names
    assert "b" in names



# Test 3 — Iteration string nodes

def test_iter_strings():
    html = "<p>Hello World</p>"
    soup = BeautifulSoup(html, "html.parser")

    strings = [node for node in soup if isinstance(node, NavigableString)]
    assert "Hello World" in strings



# Test 4 — Iterat comment nodes

def test_iter_comment():
    html = "<p><!--comment--></p>"
    soup = BeautifulSoup(html, "html.parser")

    comments = [node for node in soup if isinstance(node, Comment)]
    assert len(comments) == 1
    assert comments[0] == "comment"



# Test 5 — DFS ordering 

def test_iter_dfs_and_count():
    html = """
    <html>
      <body>
        <b>Bold Text</b>
        <p>Paragraph</p>
      </body>
    </html>
    """

    soup = BeautifulSoup(html, "html.parser")

    nodes = list(node for node in soup)

    # BS4 sees whitespace nodes .
    assert len(nodes) == 14  # expected from your earlier run

    # First DFS nodes
    assert nodes[0].name == "[document]"
   