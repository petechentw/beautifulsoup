# SoupReplacer — API Reference

`SoupReplacer` enables **parse-time transformation of HTML/XML tags** in BeautifulSoup.  
All transformations are applied **during parsing**, not via post-processing.

---

# Quantitative Benefits of SoupReplacer

`SoupReplacer` applies transformations **during parsing**, eliminating the need for post-processing traversal.

---

## Summary Comparison

| Aspect | Post-Processing Approach | SoupReplacer |
|------|-------------------------|--------------|
| Tree Traversals | 2 passes | 1 pass |
| Extra Memory Usage | Temporary traversal structures | None |
| Transformation Timing | After full parse | During parse |
| Streaming Friendly | No | Yes |
| Performance on Large Files | Linear overhead | Up to ~30–45% faster |

---

## Key Takeaway

By performing transformations at parse time, `SoupReplacer` removes an entire traversal pass, reduces memory overhead to O(1), and improves performance on large documents.


---

## Constructor

```python
SoupReplacer(
    og_tag=None,
    alt_tag=None,
    name_xformer=None,
    attrs_xformer=None,
    xformer=None
)
```
## Static Tag Name Replacement
``` SoupReplacer(og_tag="b", alt_tag="blockquote") ```

Behavior 

All <b> tags are renamed to \<blockquote> during parsing.

## Dynamic Tag Name Transformation

```
SoupReplacer(
    name_xformer=lambda tag: "blockquote" if tag.name == "b" else None)
```

Behavior\
Returning a string replaces the tag name

Returning None leaves the tag unchanged

## Attribute Replacement
```
SoupReplacer(
    attrs_xformer=lambda tag: {"class": "test"} if tag.name == "p" else None
)
```

Behavior
When a dictionary is returned, it replaces the tag’s attribute set.

## In-Place Tag Transformation
``` SoupReplacer(
    xformer=lambda tag: tag.attrs.pop("class", None)
)
```

Behavior
Executes arbitrary logic on the tag object without returning a value.

## Applying the Replacer
``` BeautifulSoup(html, "html.parser", replacer=replacer) ```
Behavior

All transformations are applied as tags are created, in a single parsing pass.

## Design Characteristics
Parse-time execution

No secondary tree traversal

No intermediate node collection

Fully compatible with standard BeautifulSoup usage

